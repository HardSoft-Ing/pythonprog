#!python
# Author: schaitbe
#
# The script updates the tools which are included by the "svn:externals properties"  in a 
# Tools-Configuration like the "CommonPrjTools" to latest revision. The tools to be updated
# must exists in a "tags" repository relative the the Tools-Configuration repository. The 
# tools to be considered for update also must be entered into list "LstToolTagsSubUrls"
# below.
#
# Arguments argv[1]:
# The file-path to the svn managed tools directory (e.g. CommonPrjTools), which 
# contains includes multiple tools via svn:externals properties. If omitted the 
# the current DIR will be used. 
# The script supports the tools listed by LstToolTagsSubUrls below.
# 
#
# TODO::schaitbe: 
# - automatic scan all tools included by a "tags" repository to avoid 
#   to maintaining the list "LstToolTagsSubUrls".

import os
import sys
import subprocess
import re
import tempfile





# --- Constants ---------------------------------------------------------------


# List of "tags" Sub-URLs of those tools being included by svn:externals. 
# Note: the Sub-URLs are based on variable "baseUrlToolsRepo". If a Sub-URL = "Sle79ToolsRep/tags"
# and the baseUrlToolsRepo = "https://agb-svr-svn01.agb.infineon.com/svn/" the absolute tool's
# "tags-URL" expands to = "https://agb-svr-svn01.agb.infineon.com/svn/Sle79ToolsRep/tags", which 
# is expected to exists.
LstToolTagsSubUrls = [
    "Sle79ToolsRep/tags",
    "Sle70ToolsRep/tags",
    "Sle90ToolsRep/tags",
    "ScmToolsRep/tags"
]    



# --- Globals   ---------------------------------------------------------------

# Open the system null-file for redirecting shell-output to be muted. 
g_fDevNul = open(os.devnull); 

# The Tools-DIR: by default we use the current DIR of this script.
g_dirToolsRepo = ".";



# --- Functions ---------------------------------------------------------------


##
# Returns the Base-URL of the given svn repository DIR. 
# Example:
# If URL: https://agb-svr-svn01.agb.infineon.com/svn/DevToolsRep/config/CommonPrjTools 
# the function returns "https://agb-svr-svn01.agb.infineon.com/svn/"
#
def getSvnBaseUrl(svnToolsDir):
    svnInfo=subprocess.check_output(["svn", "info", svnToolsDir], universal_newlines=True);
    for line in svnInfo.splitlines():
        # Get for "URL:" element. Note, we use raw strings (r') for the regex to avoid escaping,
        # see python "re" documentation. 
        matchURL = re.match(r'URL:\s+(https.+svn/).+', line); 
        if matchURL != None:
            return matchURL.group(1);
    
    return None;

##
# The function returns latest revision of the tool contained in the tags-repository 
# addressed by svnToolTagsUrl.
# @param svnToolTagsUrl the svn URL of the tool's tags-repository to be evaluated, 
#        example SDK70: "https://agb-svr-svn01.agb.infineon.com/svn/Sle70ToolsRep/tags".
# @returns the (string, int)-tuple "(toolPath, revNum)"  which are the values of the elements "Path:" and 
# "Last Changed Rev:" of command "svn info --depth=immediates svnToolTagsUrl". If svnToolTagsUrl can't 
# resolved the function returns None. 
#
def getTagsRepoNewestRelease(svnToolTagsUrl):
    matchPath = None;
    matchRev = None;
    revNum = 0;
    toolPath = '';
    try:
        # call 'svn info' and suppress stderr output
        svnInfo=subprocess.check_output(["svn", "info", "--depth=immediates", svnToolTagsUrl], stderr = g_fDevNul, universal_newlines=True);
    except:
        return None;
    # Use splitlines() to iterate svnInfo line by line.
    for line in svnInfo.splitlines():
        # Note, the matches are reset to None 
        if matchPath is None:
            matchPath = re.match(r'Path\s*:\s*(.*)', line);
        if matchRev is None:
            matchRev = re.match(r'Last Changed Rev\s*:\s*(.*)', line);
        # Check that a pair of revision-match and path-match was found.
        if (matchPath is not None) and (matchRev is not None):
            # Skip svn path-element "tags" which always is contained in the repository but not of interest! 
            if matchPath.group(1) != 'tags':
                # Sort out highest version number
                getrev = int(matchRev.group(1));
                if getrev > revNum:
                    revNum = getrev;
                    toolPath = matchPath.group(1);
            
            # Reset matches for next search iteration.
            matchPath = matchRev = None;
            
    # Note, if required someday we can even return toolPath and revNum as tuple
    return (toolPath, revNum)
    #return toolPath;

##
# Converts a Unix formatted cygwin file-path into a Windows path.     
#
def toWinPath(filePath):    
    if sys.platform == 'cygwin':
        filePath = (subprocess.check_output(["cygpath", "-w" ,filePath], universal_newlines=True)).strip('\n');
    return filePath
    
##
# Asks the user to accept the found tool-tag or to replace by a tag entered
# by the user.
# @param toolTag the tag to be altered
# @param revNum the revision number of the tool referenced by toolTag.
# @return - value of toolTag if newest version is accepted. 
#         - an alternative tool-tag from user 
#         - 'None' if the user enters "no" or "NO" to keep current version.
#
def checkAcceptNewestRev(toolTag, revNum):
        # TODO::schaitbe: check if user wants to accept this version or likes to overwrite it. 
    getToolTag = input("\nUse newest tool-revision "+ str(revNum) + ", tag: " + toolTag + '\n' +
                  " - type \"no\" + [ENTER] to keep current tool version\n"
                  " - press [ENTER] to accept newest tool version\n" 
                  " - type your tool-tag + [ENTER] to select your tool version: ");
                           
    if (getToolTag == ""):
        getToolTag = toolTag;
    # Check if user entered "no" to keep current.     
    chkNo = getToolTag.lower().strip();
    if (chkNo == "no"):
        return None;
        
    return getToolTag;
    
    

# --- Main Program ------------------------------------------------------------


# Use DIR supplied by user as tools DIR.
if len(sys.argv) > 1:
    g_dirToolsRepo = sys.argv[1];

baseUrlToolsRepo = getSvnBaseUrl(g_dirToolsRepo);
    
# Get svn:externals properties as multi-line string of the selected tools repository.
svnCMToolsProps = subprocess.check_output(["svn", "propget", "svn:externals", g_dirToolsRepo], universal_newlines=True);

# Replace old svn:externals properties with newest tools found. 
for subUrlTool in LstToolTagsSubUrls:
    # Get path-string of newest tool.
    toolPath, revNum = getTagsRepoNewestRelease(baseUrlToolsRepo + subUrlTool);
    if (toolPath == None):
        continue;
    
    # Ask user if he wants a different tool-tag than the latest found.
    toolPath = checkAcceptNewestRev(toolPath, revNum);        
    if (toolPath == None):
        continue;

    # Substitute the tool-path string in current svn:externals contained in svnCMToolsProps.
    # Note: we use raw-strings (r'\1') for getting the found regex-groups in sub() as otherwise it 
    # must be escaped as '\\1', which looks a bit confusing. 
    svnCMToolsProps = re.sub('('+subUrlTool+'/)[^ ]+(\s+.+)', r'\1' + toolPath + r'\2', svnCMToolsProps);

# Write the changed svn.external properties to temp-file since a multi-line property can't 
# be set by "svn propset" directly and thus must be read from a file.  
fSvnExtProps = tempfile.NamedTemporaryFile('w+', delete=True);
fSvnExtProps.write(svnCMToolsProps);
fSvnExtProps.flush(); # we must flush to immediately get file content.    
# Reset file pointer to allow read it from start as long as it is opened.
fSvnExtProps.seek(0);

# Windows application "svn" needs a Win file-path
pathSvnExtProps = toWinPath(fSvnExtProps.name)
# Update SKDs via "svn propset"
try:
    subprocess.check_call(["svn", "propset", "svn:externals", g_dirToolsRepo, "-F", pathSvnExtProps]);
except subprocess.CalledProcessError as e:
    print ("# cmd:", e.cmd)
    print ("# output:", e.output)

# Display the new svn:external properties. 
input('\n' +
    "Updated svn:external properties:\n" +
    "--------------------------------\n" + 
# Display new svn:externals stored in file
    fSvnExtProps.read() +
    "Press [ENTER] to continue");


# Close and remove tmp-file    
fSvnExtProps.close();    
    
# --- The implicit tools update is currently not needed but shall be kept
 
#askUpdate = input("Run tools updates now?\n" + 
#                  "Press Y/y + ENTER to confirm, press ENTER only to abort\n");

# Check if user wants to update the SDKs right now.
#if (askUpdate.lower() == 'y'):
#    subprocess.check_call(["svn", "update", g_dirToolsRepo]);




