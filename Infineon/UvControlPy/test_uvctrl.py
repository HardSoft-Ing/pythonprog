'''
Created on 16.06.2016

@author: schaitbe

@purpose: Unit-Test for class LibUvCtrl of uvctrl/libuvctrl.py 
          Note: the test expects an uVision SDK70/SDK90 instance to be started with 
          a "ready to run" chip mask.
'''
import os
from uvctrl.libuvctrl import *


# --------------------------------- Type definitions --------------------------

# --------- Constants -----------
# If True dbg_break_callfunc() stops after a command execution and 
# must be resumed via the "ENTER" key. If False not break happens.
_DBG_BREAK_ = True

# --------- Functions -----------

def dbg_break_callfunc(arg_f, *argv):
    """
    Simple "printf-debugging" support:
    Calls function "arg_f" with random count of parameters passed by "*argv"
    and returns its result.
    """
    # Invoke function with argument-list argv
    # Note: argv gets expanded via "*"
    res = arg_f(*argv)
    if _DBG_BREAK_:
        input("break on %s(), press Enter" % (arg_f.__name__))
    
    return res
        

# --------------------------------- Test-Code ----------------------------------


IFX_UVSCDLL90_PATH = os.environ['SysDevToolPath']+r'SDK90\UV4\UVSC.dll'
uvctrl = LibUvCtrl(IFX_UVSCDLL90_PATH)

# Call uvsc_init() with default IP port.
dbg_break_callfunc(uvctrl.uvsc_init, IFX_UVSCPORT, True)
dbg_break_callfunc(uvctrl.uvsc_dbg_enter)
dbg_break_callfunc(uvctrl.uvsc_dbg_start_execution)
# A 2'nd call of uvsc_dbg_start_execution() should not fail
uvctrl.uvsc_dbg_start_execution()
dbg_break_callfunc(uvctrl.uvsc_dbg_stop_execution)
# A 2'nd call of uvsc_dbg_stop_execution() should not fail
uvctrl.uvsc_dbg_stop_execution()
# Execute debug-commands "log off", "coverage asm" with "echo" in uVision (True).
dbg_break_callfunc(uvctrl.uvsc_dbg_exec_cmd, "log off; coverage asm", True)
dbg_break_callfunc(uvctrl.uvsc_dbg_exit)
# Get output of last debug-command which is "coverage asm".
resstr = dbg_break_callfunc(uvctrl.uvsc_get_cmd_output)

if resstr != None:
    print(resstr) 

uvctrl.uvsc_close_connection()    

input("Enter")
