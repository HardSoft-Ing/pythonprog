import os
import argparse
# Import uvsc definitions and ctypes 
#from uvctrl.libuvctrl import *
import uvctrl.libuvctrl as uvc

#from ctypes import *

# Module to test class LibUvCtrl

# --------------------------------- Type definitions --------------------------

# --------- Constants -----------
_DBG_BREAK_ = False

# --------- Functions -----------

def dbg_break_callfunc(arg_f, *argv):
    """
    Simple "printf-debugging" support:
    Calls function "arg_f" with any count of parameters delivered by *argv
    and returns its value. 
    """
    
    if _DBG_BREAK_:
        input("Run %s(), press Enter" % (arg_f.__name__))
    
    # Invoke function with argument-list argv
    # Note: argv gets expanded via "*"
    res = arg_f(*argv)
    
    return res
        
# --- Global definitions

def get_uvctrl_args():

    argparser = argparse.ArgumentParser()
    
    # --- Define parameter options
    
    argparser.add_argument("-p", "--port",    help="Use socket <port> to connect to uVision.", type = int)
    # Note: "type" is assigned to "open" which checks the file-path given by --dllpath to be existing and which 
    # returns the option dllpath as "TextIOWrapper" object, see python argparse lib for details.  
    argparser.add_argument("-d", "--dllpath", help="Optional UVSCOCK Dll-Path. If missing the default DLL is used.", type = open)
    argparser.add_argument("-g", "--uvdebug", help="This options runs uvcontrol with the UVSOCK debug dump printed on console.", action = "store_true" )
    
    # --- Define action options
    argparser.add_argument("-e", "--enter", help="Enter the debugger", action = "store_true")  
    argparser.add_argument("-x", "--exit",  help="Exit the debugger",  action = "store_true")  
    argparser.add_argument("-r", "--run",   help="Run the debugger", action = "store_true")  
    argparser.add_argument("-s", "--stop",  help="Stop the debugger",  action = "store_true")
    argparser.add_argument("-ex", "--execcmd", help="Execute 'Debug Command' in uVision 'Command Window'" )
    argparser.add_argument("-t", "--reset", help="Reset the target", action = "store_true")  
    argparser.add_argument("-ck","--close", help="Close uVision", action = "store_true")  
   
    # Parse provided command line arguments.  
    argsres = argparser.parse_args()
    return argsres


def open_uvsc(uvscdllpath, uvscport, uvscdbgout):
    
    libuvctrl = uvc.LibUvCtrl(uvscdllpath)
    libuvctrl.uvsc_init(uvscport, uvscport, uvscdbgout)
    return libuvctrl
    

def main_run_uvctrl_cmd():
    
    uvsc_args = get_uvctrl_args()
    
    # --- Get optional arguments
    
    uvscport = uvc.IFX_UVSCPORT
    if uvsc_args.port:
        uvscport = uvsc_args.port

    uvscdll = uvc.UVSCDLL_PATH
    if uvsc_args.dllpath:
        # Since the "type" of the argument-entry "--dllpath" is assigned to open() 
        # we obtain a "TextIOWrapper" object with property "name" which stores the file-path.
        uvscdll = uvsc_args.dllpath.name         
    
    uvscdbgout = uvsc_args.uvdebug              
    
   
    # --- Run uvcontrol commands
    
    uvsc_obj = open_uvsc(uvscdll, uvscport, uvscdbgout)
    try:
        if uvsc_args.enter:
            uvsc_obj.uvsc_dbg_enter() 
            
        if uvsc_args.exit:
            uvsc_obj.uvsc_dbg_exit()
            
        if uvsc_args.run:
            uvsc_obj.uvsc_dbg_start_execution()
    
        if uvsc_args.stop:
            uvsc_obj.uvsc_dbg_stop_execution()
    
        if uvsc_args.execcmd:
            uvsc_obj.uvsc_dbg_exec_cmd(uvsc_args.execcmd,True)
            result = uvsc_obj.uvsc_get_cmd_output()
            if not result == None:
                print(result)
             
            
        if uvsc_args.reset:
            uvsc_obj.uvsc_dbg_reset()
        
        if uvsc_args.close:
            uvsc_obj.uvsc_close_connection(True)
            uvsc_obj = None

    finally:        
        # Always close connection before exit. 
        if uvsc_obj:
            uvsc_obj.uvsc_close_connection(False)        
    
    
main_run_uvctrl_cmd()

