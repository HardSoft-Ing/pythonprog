'''
Created on 16.06.2016

@author: schaitbe
'''
# Import "os" services
import os
import sys

# Import all from uvsc_defs without module name-space
from uvctrl.uvsc_defs import *

import uvctrl.uvsc_defs as uvdefs


# --- IFX domein constants here
# Default ip-port used by the IFX department.  
IFX_UVSCPORT = 4823
# Get .\keil_uvsc\UVSC.dll relative to this module. 
UVSCDLL_PATH =  os.path.dirname(uvdefs.__file__)+r'\keil_uvsc\UVSC.dll'
UVSC_HDL_INVALID = -1 

# class UvConnect(Structure):
#     # Must use initializer _fields_ to define class members for classes derived 
#     # from Structure. Note, don't use _init_() as it don't works for such classes.  
#     _fields_ = [('msg', c_char_p)]
#      
#     def printMsg(self, msg):
#         print("xxx UvConnect.printMsg(): " + msg)
# 
# uvConnect = UvConnect(b"Hello UV-Sock") 

# --- static void uvsc_cb_getdisconnected(void *cb_custom, UVSC_CB_TYPE type, UVSC_CB_DATA *data)
def uvsc_cb_getdisconnected(cb_custom, cbType, pData):
    strCbType = None
    # Check if UVSC has "disconnected" (e.g. uVsion has closed).  
    if cbType.value == UVSC_CB_TYPE.UVSC_CB_DISCONNECTED:
        # cast cb_custom from *void to *c_long required! 
        cintp_uvscHandle = cast(cb_custom, POINTER(c_long))
        # Mark the LibUvCtrl instance as "disconnected" if its handle matches the 
        # disconnected uVsion GUI as reported by pData.    
        if (pData[0].iConnHandle == cintp_uvscHandle[0]):      
            cintp_uvscHandle[0] = UVSC_HDL_INVALID
            #print ("xxxxx invalidated cintp_uvscHandle" )
        



# We must create a fixed object reference of callback uvsc_cb_getdisconnected()
# to prevent python's GC from cleaning up the callback object.  
fncref_uvsc_cb = uvsc_cb_t(uvsc_cb_getdisconnected)

# --- static void uvsc_log_callback(const char *msg, int msgLen)
def uvsc_log_callback(msg, msgLen):
    # The UVSC log goes to stderr only. 
    print("xxx UVSC_Debug_Out:", msg, file=sys.stderr)

g_fncref_log_cb = log_cb_t(uvsc_log_callback)        


class UvCtrlError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class LibUvCtrl(object):
    # Constructor  
    def __init__(self, uvscdll_path = UVSCDLL_PATH):
        """ Ties this LibUvCtrl instance to an USCV.DLL instance
            @param uvscdll_path: path of the UVSC.DLL to be load.    
        """
        # Load uvsc.dll
        self.uvscdll = CDLL(uvscdll_path) 
        self.cint_uvscHandle = c_long(UVSC_HDL_INVALID)
        # shall set to "auto-port" for subsequent following UVSC-initialization
        self.cint_uvscPort = c_long(UVSC_PORT_AUTO)
        
    # --- Class private members
    
    # TODO::schaitbe: make this function an UVSC call-wrapper such that it invokes 
    # the given UVSC function with variadic arguments and checks its result.
    # Besides it shall run _check_uvsc_connected_() in advance.      
    def _check_uvsc_result_(self, result, msg):
        if result != UVSC_STATUS.UVSC_STATUS_SUCCESS:
            raise UvCtrlError("UVSC-DLL error of function : " + msg + ", result = " + str(result))  
    
    def _check_uvsc_connected_(self):
        if self.cint_uvscHandle.value == UVSC_HDL_INVALID:
            raise UvCtrlError("UVSC disconnected!")  

    # --- Class public API 
             
    def uvsc_init(self, uvsc_min_port = UVSC_MIN_AUTO_PORT, uvsc_max_port = UVSC_MAX_AUTO_PORT, uvsc_dbgout = False, uvsc_cmdexe = NULLPTR):
        """ Establishes an UVSC IP connection, if an uVision GUI is running.      
            @param uvsc_min_port: the minimum IP port required by USCV.dll if an uVision instance via 
                   uvsc_cmdexe shall be set (uvsc_cmdexe!= NULLPTR) 
            @param uvsc_max_port: the maximum IP port required by USCV.dll if an uVision instance via 
                   uvsc_cmdexe shall be set (uvsc_cmdexe!= NULLPTR) 
            @param uvsc_dbgout: if "True" the UVSC debug-log will be dumped to stderr.
            @param uvsc_cmdexe: the full path to the uVision executable (is usually UV4.exe). If set to NULLPTR 
                   then uvsc_min_port and uvsc_max_port shall be set both to the port-value of the external started 
                   uVision instance. 
        """
        # convert unicode to bytes format for UVSC API. 
        if uvsc_cmdexe != None: 
           uvsc_cmdexe = uvsc_cmdexe.encode('utf-8')
           
        # Disable UVSC logging-callback if no debug output is required.  
        fncref_log_cb = NULLPTR 
        if uvsc_dbgout:
            fncref_log_cb = g_fncref_log_cb
            
        result = self.uvscdll.UVSC_Init(uvsc_min_port, uvsc_max_port)
        self._check_uvsc_result_(result, "UVSC_Init()")
        
        result = self.uvscdll.UVSC_OpenConnection(NULLPTR, byref(self.cint_uvscHandle), byref(self.cint_uvscPort),
                        uvsc_cmdexe, UVSC_RUNMODE.UVSC_RUNMODE_NORMAL, fncref_uvsc_cb, byref(self.cint_uvscHandle), NULLPTR, xBOOL(False), fncref_log_cb)
                        
        self._check_uvsc_result_(result, "UVSC_OpenConnection()")
    
    def uvsc_dbg_exec_cmd(self, cmd, bEcho = 0):
        """ Issues a "Debug Command" into the uVision "Command Window".  
            @param cmd: a string containing the uVsion "Debug Command" to be executed.  
            @param bEcho: if 1 the "Debug Command" and its response are echoed in 
                          the uVision Command Window. 
        """
        
        self._check_uvsc_connected_()                        
        # EXECCMD needs bytes, thus we convert "cmd" from unicode to utf-8 bytes!
        cmd_b = cmd.encode('utf-8')
        objLen = sizeof(EXECCMD)
        # Initialize struct EXECCMD: 
        # Note, ctypes knows how to initialize "sub-structs" likewise a C compiler 
        # if passing struct-init-data appropriately grouped in tuples. But also a 
        # the more descriptive initialization can be used: 
        # "EXECCMD(bEcho, 0, (c_uint* 7)(), SSTR(objLen, cmd_b))"  
        execCmd = EXECCMD(bEcho, 0, (c_uint* 7)(), (objLen, cmd_b))
        # _UVSC_FUNC_ UVSC_STATUS UVSC_DBG_EXEC_CMD(int iConnHandle, EXECCMD *pCmd, int objLen)
        result = self.uvscdll.UVSC_DBG_EXEC_CMD(self.cint_uvscHandle, byref(execCmd), objLen)
        self._check_uvsc_result_(result, "UVSC_DBG_EXEC_CMD()")
        
             
    def uvsc_get_cmd_output(self):
        """ Returns the result of the last command issued 
            by uvsc_dbg_exec_cmd().
            @return:  result string of last command of uvsc_dbg_exec_cmd(). 
        """

        self._check_uvsc_connected_()
        cmdLen = c_int(0)
        #_UVSC_FUNC_ UVSC_STATUS UVSC_GetCmdOutputSize(int iConnHandle, int *pCmdOutputSize)
        result = self.uvscdll.UVSC_GetCmdOutputSize(self.cint_uvscHandle, byref(cmdLen))
        self._check_uvsc_result_(result, "UVSC_GetCmdOutputSize()")
        if cmdLen.value > 0:
            pCmdOutput = create_string_buffer(cmdLen.value)
            result = self.uvscdll.UVSC_GetCmdOutput(self.cint_uvscHandle, pCmdOutput, cmdLen.value)
            self._check_uvsc_result_(result, "UVSC_GetCmdOutput()")
            # Convert utf-8 byte-string to python's platform string to correctly interpret escape-chars like "\n"! 
            return pCmdOutput.value.decode('utf-8')
        
        return None
    
    def uvsc_dbg_getstatus(self):
        """ Get debugger execution status.
            @return:  the execution status. 1:= the target is executing, 
                      0:= the target is stopped.    
        """ 
        
        self._check_uvsc_connected_()
        cint_status = c_int()
        result = self.uvscdll.UVSC_DBG_STATUS(self.cint_uvscHandle, byref(cint_status))
        self._check_uvsc_result_(result, "UVSC_DBG_ENTER()")
        return cint_status.value
    
    # TODO::schaitbe  uvsc_dbg_enter() should not fail if invoked multiple times.  
    # Use  UVSC_GetLastError() to detect such situations.              
    def uvsc_dbg_enter(self):
        """ Enter debug mode. 
        """
        self._check_uvsc_connected_()
        result = self.uvscdll.UVSC_DBG_ENTER(self.cint_uvscHandle)
        self._check_uvsc_result_(result, "UVSC_DBG_ENTER()")

    # TODO::schaitbe  uvsc_dbg_exit() should not fail if invoked multiple times.  
    # Use  UVSC_GetLastError() to detect such situations.              
    def uvsc_dbg_exit(self):
        """ Exit debug mode.
        """
        self._check_uvsc_connected_()
        result = self.uvscdll.UVSC_DBG_EXIT(self.cint_uvscHandle)
        self._check_uvsc_result_(result, "UVSC_DBG_EXIT()")
            

    def uvsc_dbg_start_execution(self):
        """ Start debugger execution. If debugging is already started nothing will be done!  
        """
        # Enter debug mode only, if not already running.
        if self.uvsc_dbg_getstatus() == 0:
            result = self.uvscdll.UVSC_DBG_START_EXECUTION(self.cint_uvscHandle)
            self._check_uvsc_result_(result, "UVSC_DBG_START_EXECUTION()")


    def uvsc_dbg_stop_execution(self):
        """ Stop debugger execution.  If debugging is already stopped nothing will be done!  
        """
        
        if self.uvsc_dbg_getstatus() == 1:
            result = self.uvscdll.UVSC_DBG_STOP_EXECUTION(self.cint_uvscHandle)
            self._check_uvsc_result_(result, "UVSC_DBG_STOP_EXECUTION()")
            

    def uvsc_dbg_reset(self):
        """ Use this function to reset the target processor or simulation.
            This is the equivalent of clicking the 'Peripherals-->Reset CPU' menu item in uVision.  
        """
        self._check_uvsc_connected_()
        result = self.uvscdll.UVSC_DBG_RESET(self.cint_uvscHandle)
        self._check_uvsc_result_(result, "UVSC_DBG_RESET()")


    def uvsc_close_connection(self, terminate = False):
        """ Closes the current UVSC IP connection.  
            @param terminate:  
                   - if True the uVision GUI gets closed too. 
                   - if False only the UVSC IP-connection is closed.
        """
        
        self._check_uvsc_connected_()
        result = self.uvscdll.UVSC_CloseConnection(self.cint_uvscHandle, xBOOL(terminate))
        self._check_uvsc_result_(result, "UVSC_CloseConnection()")
        
        return None

    
    #_UVSC_FUNC_ UVSC_STATUS UVSC_CloseConnection(int iConnHandle, xBOOL terminate)
    


# _UVSC_FUNC_ UVSC_STATUS UVSC_GetCmdOutput(int iConnHandle, char *pCmdOutput, int cmdOutputLen)