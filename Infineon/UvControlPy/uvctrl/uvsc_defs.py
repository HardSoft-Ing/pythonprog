'''
Created on 16.06.2016

@author: schaitbe
'''
from ctypes import *
import ctypes
# --------------------------------- Type definitions --------------------------

# --------- Constants -----------

# --- Put Keil-UVSC constants here

# /** Auto port
#   *
#   * This define is used to indicate that automatic port selection is 
#   * wanted.
#   */
UVSC_PORT_AUTO = 0

# /** Minimum auto port value
#   *
#   * The minimum port passed to #UVSC_Init must not be less than this.
#   */
UVSC_MIN_AUTO_PORT =  1
# 
# /** Maximum auto port value
#   *
#   * The maximum port passed to #UVSC_Init must not be more than this.
#   */
UVSC_MAX_AUTO_PORT = 65535


# --- Define Keil scalar-data types.  

# - Define custom scalar-ctypes here. To do this the following must be obeyed:
#   > custom ctypes must be derived from ctypes._SimpleCData
#   > the size and type coding is defined via class member _type_. Refer
#     to the appropriate ctypes for the correct type coding, e.g. scalar
#     c_short is defined as: _type_ = "h".      


# xBOOL as c_ubyte:  _type_="B".   
# Use with Python "True"/"False" e.g. xBOOL(True)
class xBOOL(ctypes._SimpleCData):
    _type_="B"

# xU64 as c_ulonglong:  _type_="Q".   
class xU64(ctypes._SimpleCData):
    _type_="Q"

# xI64 as c_longlong:  _type_="q".   
class xI64(ctypes._SimpleCData):
    _type_="q"


# --- Define Keil enum classes.  

#     Note: below enum definitions provide no type safety but can be used instead  
#     of c_int when actually an enum type is required.  


# Enum UVSC_RUNMODE as c_int
class UVSC_RUNMODE(c_int):
    UVSC_RUNMODE_NORMAL   = 0 #///< Normal uVision operation
    UVSC_RUNMODE_LABVIEW  = 1 #///< LabVIEW operation       
 
# Enum UVSC_STATUS as c_int     
class UVSC_STATUS(c_int):
    UVSC_STATUS_SUCCESS             = 0  #///< Success
    UVSC_STATUS_FAILED              = 1  #///< General failure
    UVSC_STATUS_NOT_SUPPORTED       = 2  #///< Request for an unsupported operation
    UVSC_STATUS_NOT_INIT            = 3  #///< UVSC not initialised
    UVSC_STATUS_TIMEOUT             = 4  #///< Operation timed-out
    UVSC_STATUS_INVALID_CONTEXT     = 5  #///< Function called from an invalid context (most likely the callback function)
    UVSC_STATUS_INVALID_PARAM       = 6  #///< Function called with one or more invalid parameters
    UVSC_STATUS_BUFFER_TOO_SMALL    = 7  #///< Function called with a buffer that was not big enough to hold the result from uVision
    UVSC_STATUS_CALLBACK_IN_USE     = 8  #///< Function cannot be used when the callback is in use
    UVSC_STATUS_COMMAND_ERROR       = 9  #///< The command failed - call #UVSC_GetLastError to get more information on how the command failed

# Enum PGCMD as c_int
class PGCMD (c_int):
# Enum class    
    UV_PROGRESS_INIT    =  1 #///< Initialize progress bar with optional label (in %-mode)
    UV_PROGRESS_SETPOS  =  2 #///< Set progress bar percentage (0...100)
    UV_PROGRESS_CLOSE   =  3 #///< Close the progress bar
    UV_PROGRESS_INITTXT =  4 #///< Initialize progress bar (in text mode)
    UV_PROGRESS_SETTEXT =  5 #///< Set inside bar text in text mode

# Enum ENTPJOB as c_int  
class ENTPJOB (c_int):
    UV_TPENUM_MEMBERS  =  1  # ///< Enumerate symbols' structure members: name, offset, size

# Enum UV_STATUS as c_int
class UV_STATUS (c_int):
    UV_STATUS_SUCCESS             = 0  #///< Operation successful: No error
    UV_STATUS_FAILED              = 1  #///< Operation failed: Generic / unknown error
    UV_STATUS_NO_PROJECT          = 2  #///< Operation failed: No project is currently open
    UV_STATUS_WRITE_PROTECTED     = 3  #///< Operation failed: The current project is write protected
    UV_STATUS_NO_TARGET           = 4  #///< Operation failed: No target is selected for the current project
    UV_STATUS_NO_TOOLSET          = 5  #///< Operation failed: No toolset is selected for the current target
    UV_STATUS_NOT_DEBUGGING       = 6  #///< Operation failed: The debugger is not running, this operation is only possible in debug mode
    UV_STATUS_ALREADY_PRESENT     = 7  #///< Operation failed: The group / file is already present in the current project
    UV_STATUS_INVALID_NAME        = 8  #///< Operation failed: One of the specified group / file / project name(s) is invalid
    UV_STATUS_NOT_FOUND           = 9  #///< Operation failed: File / group not found in the current project
    UV_STATUS_DEBUGGING           = 10 #///< Operation failed: The debugger is running, this operation is only possible when not in debug mode
    UV_STATUS_TARGET_EXECUTING    = 11 #///< Operation failed: The target is executing, this operation is not possible when target is executing
    UV_STATUS_TARGET_STOPPED      = 12 #///< Operation failed: The target is stopped, this operation is not possible when target is stopped
    UV_STATUS_PARSE_ERROR         = 13 #///< Operation failed: Error parsing data in request
    UV_STATUS_OUT_OF_RANGE        = 14 #///< Operation failed: Data in request is out of range
    UV_STATUS_BP_CANCELLED        = 15 #///< Operation failed: Create new breakpoint has been cancelled
    UV_STATUS_BP_BADADDRESS       = 16 #///< Operation failed: Invalid address in create breakpoint
    UV_STATUS_BP_NOTSUPPORTED     = 17 #///< Operation failed: Type of breakpoint is not supported (by target)
    UV_STATUS_BP_FAILED           = 18 #///< Operation failed: Breakpoint creation failed (syntax error, nested command etc.)
    UV_STATUS_BP_REDEFINED        = 19 #///< Breakpoint Info: A breakpoint has been redefined
    UV_STATUS_BP_DISABLED         = 20 #///< Breakpoint Info: A breakpoint has been disabled
    UV_STATUS_BP_ENABLED          = 21 #///< Breakpoint Info: A breakpoint has been enabled
    UV_STATUS_BP_CREATED          = 22 #///< Breakpoint Info: A breakpoint has been created
    UV_STATUS_BP_DELETED          = 23 #///< Breakpoint Info: A breakpoint has been deleted
    UV_STATUS_BP_NOTFOUND         = 24 #///< Operation failed: Breakpoint with @a nTickMark cookie not found.
    UV_STATUS_BUILD_OK_WARNINGS   = 25 #///< Build Info: A build was successful, but with warnings
    UV_STATUS_BUILD_FAILED        = 26 #///< Build Info: A build failed with errors
    UV_STATUS_BUILD_CANCELLED     = 27 #///< Build Info: A build was cancelled
    UV_STATUS_NOT_SUPPORTED       = 28 #///< Operation failed: Requested operation is not supported
    UV_STATUS_TIMEOUT             = 29 #///< Operation failed: No response to the request occurred within the timeout period (UVSOCK Client DLL only)
    UV_STATUS_UNEXPECTED_MSG      = 30 #///< Operation failed: An unexpected message type was returned (UVSOCK Client DLL only)
    UV_STATUS_VERIFY_FAILED       = 31 #///< Operation failed: The code downloaded in the target differs from the current binary
    UV_STATUS_NO_ADRMAP           = 32 #///< Operation failed: The specified code address does not map to a file / line
    UV_STATUS_INFO                = 33 #///< General Info: This is an information only message. It may contain warning information pertinent to a later error condition.
    UV_STATUS_NO_MEM_ACCESS       = 34 #///< Operation failed: Memory access is blocked (most likely target does not support memory access while running)
    UV_STATUS_FLASH_DOWNLOAD      = 35 #///< Operation failed: The target is downloading FLASH, this operation is not possible when FLASH is downloading
    UV_STATUS_BUILDING            = 36 #///< Operation failed: A build is in progress, this operation is not possible when build is in progress
    UV_STATUS_HARDWARE            = 37 #///< Operation failed: The debugger is debugging hardware, this operation is not possible when debugging a hardware target
    UV_STATUS_SIMULATOR           = 38 #///< Operation failed: The debugger is debugging a simulation, this operation not possible when debugging a simulated target
    UV_STATUS_BUFFER_TOO_SMALL    = 39 #///< Operation failed: Return buffer was too small (UVSOCK Client DLL only)

# Enum  VTT_TYPE as c_int  
class VTT_TYPE (c_int):
    VTT_void    =  0    #///< val.u64
    VTT_bit     =  1    #///< val.ul & 1
    VTT_char    =  2    #///< val.sc
    VTT_uchar   =  3    #///< val.uc
    VTT_int     =  4    #///< val.i
    VTT_uint    =  5    #///< val.ul
    VTT_short   =  6    #///< val.i16
    VTT_ushort  =  7    #///< val.u16
    VTT_long    =  8    #///< val.l
    VTT_ulong   =  9    #///< val.ul
    VTT_float   = 10    #///< val.f
    VTT_double  = 11    #///< val.d
    VTT_ptr     = 12    #///< val.ul
    VTT_union   = 13    #///< Unused
    VTT_struct  = 14    #///< Unused
    VTT_func    = 15    #///< Unused
    VTT_string  = 16    #///< Unused
    VTT_enum    = 17    #///< Unused
    VTT_field   = 18    #///< Unused
    VTT_int64   = 19    #///< val.i64
    VTT_uint64  = 20    #///< val.u64
  
# Enum STOPREASON as c_int
class STOPREASON (c_int):
    STOPREASON_UNDEFINED =  0x0000 #///< Unknown / undefined stop reason
    STOPREASON_EXEC      =  0x0001 #///< Hit execution breakpoint
    STOPREASON_READ      =  0x0002 #///< Hit read access breakpoint
    STOPREASON_HIT_WRITE =  0x0004 #///< Hit write access breakpoint
    STOPREASON_HIT_COND  =  0x0008 #///< Hit conditional breakpoint
    STOPREASON_HIT_ESC   =  0x0010 #///< ESCape key has been pressed
    STOPREASON_HIT_VIOLA =  0x0020 #///< Memory access violation occurred (simulator only)
    STOPREASON_TIME_OVER =  0x0040 #///< Interval time set by #UV_DBG_SET_CALLBACK or #UV_DBG_WAKE elapsed
    STOPREASON_UNDEFINS  =  0x0080 #///< Undefined instruction occurred
    STOPREASON_PABT      =  0x0100 #///< (Instruction) prefetch abort occurred
    STOPREASON_DABT      =  0x0200 #///< Data abort occurred
    STOPREASON_NONALIGN  =  0x0400 #///< Non-aligned access occurred (simulator only)
  
 
# /** UVSC callback type
#  *
#  * Indicates the type of message retuned in the UVSC callback function #uvsc_cb
#  * configured through #UVSC_OpenConnection.
#  */
# Enum UVSC_CB_TYPE as c_int
class UVSC_CB_TYPE (c_int):
    UVSC_CB_ERROR                   = 0   #///< Error notification (not used)
    UVSC_CB_ASYNC_MSG               = 1   #///< Asynchronous message received (called from UVSC internal thread)  
    UVSC_CB_DISCONNECTED            = 2   #///< uVision has disconnected (called from UVSC internal thread)
    UVSC_CB_BUILD_OUTPUT_MSG        = 3   #///< Called from the #UVSC_PRJ_BUILD function - indicates a line of build output (called from API function callers own thread)  
    UVSC_CB_PROGRESS_BAR_MSG        = 4   #///< Called from function that cause a progress bar in uVision - indicates the progress bar state (called from API function callers own thread)  
    UVSC_CB_CMD_OUTPUT_MSG          = 5   #///< Called from the #UVSC_DBG_EXEC_CMD function - indicates a line of command output (called from API function callers own thread)  

 
  
    

# /** Maximum transfer size of a single UVSOCK packet (bytes)
#   *
#   * No UVSOCK packet may be larger than @a SOCK_NDATA bytes. This includes both the packet header and packet data.
#   */
# #define SOCK_NDATA  32768              
SOCK_NDATA = 32768


# A cytpes null-pointer is just "None" 
NULLPTR = None;




# typedef struct sstr  {    
#   int               nLen;   ///< Length of name (including NULL terminator)
#   char        szStr[256];   ///< NULL terminated name string
# } SSTR;
class SSTR(Structure):
    _fields_ = [("nLen", c_int),
                ("szStr", c_char * 256)]
    
# typedef struct execCmd  {
#   UINT         bEcho : 1;   ///< 1:=echo command and response in uVision Command Window, 0:=no echo
#   UINT               :31;   ///< Reserved
#   UINT           nRes[7];   ///< Reserved
#   SSTR              sCmd;   ///< Command to execute
# } EXECCMD;
class EXECCMD(Structure):
    _fields_ = [("bEcho", c_uint, 1),
                ("_pad0_", c_uint, 31),
                ("nRes", c_uint * 7),
                ("sCmd", SSTR)]

# typedef struct prjdat  { 
#   UINT              nLen;   ///< Length of @a szNames including NULL terminators
#   UINT             nCode;   ///< Informational code
#   char        szNames[1];   ///< Information ('string 1',0 [,'string 2',0] ... [,'string N',0])
# } PRJDATA;
class PRJDATA (Structure):
    _fields_ = [("nLen", c_uint),
                ("nCode", c_uint),
                ("szNames", POINTER(c_char))]
    

# typedef struct amem  {
#   xU64             nAddr;   ///< Address to read / write
#   UINT            nBytes;   ///< Number of bytes read / write
#   xU64           ErrAddr;   ///< Unused
#   UINT              nErr;   ///< Unused
#   xUC8         aBytes[1];   ///< @a nBytes of data read or to be written
# } AMEM;
class AMEM (Structure):
    _fields_ = [("nAddr", xU64),
                ("nBytes", c_uint),
                ("ErrAddr", xU64),
                ("nErr", c_uint),
                ("aBytes", POINTER(c_byte))]


# typedef struct serio  {
#   xWORD16       nChannel;   ///< 0:=UART#1, 1:=UART#2, 2:=UART#3, 3:=Debug (printf) output 
#   xWORD16       itemMode;   ///< 0:=Bytes, 1:=WORD16
#   DWORD            nMany;   ///< number of items (BYTE or WORD16)
#   union  {
#     xUC8       aBytes[1];   ///< @a nMany Bytes follow here.
#     xWORD16    aWords[1];   ///< @a nMany Word16 follow here.
#   } s;                      ///< @a nMany data items.
# } SERIO;
# Embedded union of SERIO
class _S_SERIO (Union):
    _fields_ = [("aBytes", POINTER(c_byte)),
                ("aWords", POINTER(c_ushort))]
class SERIO (Structure):
    _fields_ = [("nChannel", c_ushort),
                ("itemMode", c_ushort),
                ("nMany", c_ulong),
                ("s", _S_SERIO)]

# typedef struct ipathreq  {
#   UINT        bFull : 1;    ///< 1:=want full path(s), 0:=want relative path(s)
#   UINT              :31;    ///< Reserved
#   UINT          nRes[7];    ///< Reserved
# } iPATHREQ;

class iPATHREQ (Structure):
    _fields_ = [("bFull", c_uint, 1),
                ("_pad0_", c_uint, 31),
                ("nRes", c_uint * 7)]

# typedef struct iUVSC_PSTAMP  {
#   xU64              nAdr;   ///< Address of code shown in uVision (for testing purposes).
#   INT64            ticks;   ///< ULINKpro Isolation Adapter ticks since last RESET.
#   double           delta;   ///< Time difference (sec) between \ref ticks and the measurement timestamp.
#   double            time;   ///< Absolute time value (sec) in uVision of a \ref ticks and \ref delta pair.
#   UINT           nRes[7];   ///< Reserved.
# } UVSC_PSTAMP;
class UVSC_PSTAMP (Structure):
    _fields_ = [("nAdr", xU64),
                ("ticks", c_longlong),
                ("delta", c_double),
                ("time", c_double),
                ("nRes", c_uint * 7)]
    

# typedef struct istkenum  {
#   UINT        bFull : 1;     ///< Unused, kept for backward compatibility
#   UINT        bExtended : 1; ///< Get extended information:  nVars, nTotal, iTask (see STACKENUM) <b>Extended stack mode only</b> 
#   UINT        bModified : 1; ///< Enumerate only modified frames <b>Extended stack mode only</b> 
#   UINT                  :29; ///< Reserved
#   UINT          nTask;       ///< Task ID: reserved for RTX case, otherwise ignored
#   UINT          nRes[6];     ///< Reserved
# } iSTKENUM;
class iSTKENUM (Structure):
    _fields_ = [("bFull", c_uint, 1),
                ("bExtended", c_uint, 1),
                ("bModified", c_uint, 1),
                ("_pad0_", c_uint, 29),
                ("nTask", c_uint),
                ("nRes", c_uint * 6)]

# typedef struct pgress  {
#   PGCMD              job;   ///< PGCMD command
#   UINT              perc;   ///< Percentage completed (Used on #UV_PROGRESS_SETPOS only)
#   UINT           nRes[8];   ///< Reserved
#   char        szLabel[1];   ///< Progress label (0 or labelname on #UV_PROGRESS_INIT / #UV_PROGRESS_INITTXT / #UV_PROGRESS_SETTEXT)
# } PGRESS;
class PGRESS (Structure):
    _fields_ = [("job", PGCMD), 
                ("perc", c_uint),
                ("nRes", c_uint * 8),
                ("szLabel", c_char_p)]


# typedef struct enumtpm  {
#   ENTPJOB            Job;   ///< Type of symbol enumeration to perform
#   UINT             nOffs;   ///< Member Offset within type
#   UINT             nSize;   ///< Member Size
#   UINT           nRes[8];   ///< Reserved
#   char         szID[512];   ///< 'Symbol' / 'Member name'
# } ENUMTPM;
class ENUMTPM (Structure):
    _fields_ = [("Job", ENTPJOB), 
                ("nOffs", c_uint),
                ("nSize", c_uint),
                ("nRes", c_uint * 8),
                ("szID", c_char * 512)]


# typedef struct iInterval  {  
#   UINT    bAutoStart : 1;   ///< 1:=start the target if it is not running, 0:=do not start the target
#   UINT       bCycles : 1;   ///< 1:=interval is in cycles, 0:=interval is in seconds
#   UINT  bSetInterval : 1;   ///< 1:=set the callback interval in this message, 0:=don't set a callback
#   UINT               :29;   ///< Reserved
#   float         fSeconds;   ///< Wake interval in seconds (if bCycles:=0)
#   xI64           iCycles;   ///< Wake interval in cycles (if bCycles:=1)
#   UINT           nRes[7];   ///< Reserved
# } iINTERVAL;
class iINTERVAL (Structure):
    _fields_ = [("bAutoStart", c_uint, 1),  
                ("bCycles", c_uint, 1),
                ("bSetInterval", c_uint, 1),
                ("_pad0_", c_uint, 29),
                ("fSeconds", c_float ),
                ("iCycles", xI64),
                ("nRes", c_uint * 7)]

# typedef struct tag_UVSOCK_OPTIONS {
#   DWORD bExtendedStack : 1; ///< Extended stack mode: allows task enumeration, read/write variables and expressions 
#   DWORD                :31; ///< reserved
# } UVSOCK_OPTIONS;
class UVSOCK_OPTIONS (Structure):
    _fields_ = [("bExtendedStack", c_ulong, 1), 
                ("_pad0_", c_ulong, 31)]


# typedef struct _tag_UVSOCK_ERROR_RESPONSE  {
#   UINT                   nRes1;    ///< Reserved
#   UINT                   nRes2;    ///< Reserved
#   UINT                  StrLen;    ///< Length of error string (including terminator) in bytes
#   BYTE     str [SOCK_NDATA-20];    ///< Error description
# } UVSOCK_ERROR_RESPONSE;
class UVSOCK_ERROR_RESPONSE (Structure):
    _fields_ = [("nRes1", c_uint), 
                ("nRes2", c_uint), 
                ("StrLen", c_uint), 
                ("str", c_char * (SOCK_NDATA-20))]


# typedef struct cycts  {
#   xU64            cycles;   ///< Execution time in cycles
#   double          tStamp;   ///< Execution time in seconds
# } CYCTS;
class CYCTS (Structure):
    _fields_ = [("cycles", xU64), 
                ("tStamp", c_double)]


# typedef struct tval  {
#   VTT_TYPE         vType;   ///< Indicates the type of data in @a v
#   union  {                 
#     unsigned long     ul;   ///< #VTT_ulong
#     signed char       sc;   ///< #VTT_char
#     unsigned char     uc;   ///< #VTT_uchar
#     signed short     i16;   ///< #VTT_short
#     unsigned short   u16;   ///< #VTT_ushort
#     signed long        l;   ///< #VTT_long
#     int                i;   ///< #VTT_int
#     xI64             i64;   ///< #VTT_int64
#     xU64             u64;   ///< #VTT_uint64
#     float              f;   ///< #VTT_float
#     double             d;   ///< #VTT_double
#   } v;                      ///< Data type of this union depends on @a vType
# } TVAL;
# Embedded union of TVAL
class _V_TVAL (Union):
    _fields_ = [("ul", c_ulong),
                ("sc", c_byte),
                ("uc", c_ubyte),
                ("i16", c_short),
                ("u16", c_ushort),
                ("l", c_long),
                ("i", c_int),
                ("i64", xI64),
                ("u64", xU64),
                ("f", c_float),
                ("d", c_double)]
class TVAL (Structure):
    _fields_ = [("vType", VTT_TYPE),
                ("v", _V_TVAL)]

# typedef struct vset_t  {
#   TVAL               val;   ///< Value of VTREG or register index
#   SSTR               str;   ///< Name of VTREG or expression
# } VSET;
class VSET (Structure):
    _fields_ = [("val", TVAL), 
                ("str", SSTR)]

# typedef struct extvers  {
#   UINT            iV_Uv3;   ///< 'UV3 Version' starts at &szBuffer [iV_Uv3V]
#   UINT           iV_Sock;   ///< 'UVSOCK Version' starts at &szBuffer [iV_Sock]
#   UINT          nRes[30];   ///< Reserved (for extra version information)
#   char       szBuffer[3];   ///< Version strings (0, 'uVision=Vx.y',0, 'UVSOCK=Vx.y',0, [Reserved] ,0)
# } EXTVERS;
class EXTVERS (Structure):
    _fields_ = [("iV_Uv3", c_uint), 
                ("iV_Sock", c_uint), 
                ("nRes", c_uint * 30), 
                ("szBuffer", c_char * 3)]



# typedef struct bpreason  {
#   UINT             nRes1;   ///< Reserved
#   UINT             nRes2;   ///< Reserved
#   UINT            StrLen;   ///< Unused
#   STOPREASON     eReason;   ///< Reason for stopping execution
#   xU64               nPC;   ///< Address of PC when stopped
#   xU64              nAdr;   ///< Address of break reason (i.e. memory access address, or breakpoint address)
#   int             nBpNum;   ///< Breakpoint number (-1:=undefined)
#   UINT         nTickMark;   ///< Time of breakpoint creation, used to identify individual breakpoints (0 if @a nBpNum is undefined)
#   UINT           nRes[4];   ///< Reserved
# } BPREASON;
class BPREASON (Structure):
    _fields_ = [("nRes1", c_uint),  
                ("nRes2", c_uint), 
                ("StrLen", c_uint), 
                ("eReason", STOPREASON),  # enum STOPREASON 
                ("nPC", xU64), 
                ("nAdr", xU64), 
                ("nBpNum", c_int * 8),
                ("nTickMark", c_uint), 
                ("nRes", c_uint * 4)]
# typedef struct dbgtgtopt {
#   DWORD      target :  1;   ///< Target type (#UV_TARGET_HW:=Target is hardware, #UV_TARGET_SIM:=Target is simulator)
#   DWORD             : 31;   ///< Reserved
#   DWORD         nRes[10];   ///< Reserved
# } DBGTGTOPT;
class DBGTGTOPT (Structure):
    _fields_ = [("target", c_ulong, 1),  
                ("_pad0", c_ulong, 31), 
                ("nRes", c_ulong * 10)]


# typedef struct _tag_UVSOCK_CMD_RESPONSE  {
#   UV_OPERATION             cmd;    ///< Command or asynchronous operation to which this is a response
#   UV_STATUS             status;    ///< Status code indicating if the command was successful or not
#   union {
#     UVSOCK_ERROR_RESPONSE  err;    ///< Returned if status is not #UV_STATUS_SUCCESS or if from #ASYNC_MSG
#     UINT                  nVal;    ///< Returned by #UV_PRJ_ACTIVE_FILES / #UV_GEN_GET_VERSION / #UV_DBG_STATUS
#     CYCTS                 time;    ///< Returned by #UV_DBG_TIME_INFO
#     AMEM                  amem;    ///< Returned by #UV_DBG_MEM_READ / #UV_DBG_MEM_WRITE / #UV_DBG_DSM_READ
#     SERIO               serdat;    ///< Returned by #UV_DBG_SERIAL_OUTPUT / #UV_DBG_SERIAL_GET
#     VSET                  vset;    ///< Returned by #UV_DBG_VTR_GET / #UV_DBG_CALC_EXPRESSION
#     BKRSP                  brk;    ///< Returned by #UV_DBG_BP_ENUMERATED / #UV_DBG_CHANGE_BP
#     TRNOPT              trnopt;    ///< Returned by #UV_PRJ_GET_OPTITEM
#     SSTR                   str;    ///< Returned by #UV_PRJ_ENUM_GROUPS_ENU / #UV_PRJ_ENUM_FILES_ENU / #UV_PRJ_ENUM_TARGETS_ENU / #UV_PRJ_GET_CUR_TARGET / #UV_PRJ_GET_OUTPUTNAME/ #UV_PRJ_SET_OUTPUTNAME
#     EXTVERS              evers;    ///< Returned by #UV_GEN_GET_EXTVERSION
#     ENUMTPM                tpm;    ///< Returned by #UV_DBG_ENUM_SYMTP_ENU
#     AFLMAP                aflm;    ///< Returned by #UV_DBG_ADR_TOFILELINE
#     BPREASON             StopR;    ///< Returned by #UV_DBG_STOP_EXECUTION
#     STACKENUM            stack;    ///< Returned by #UV_DBG_ENUM_STACK_ENU
#     TASKENUM              task;    ///< Returned by #UV_DBG_ENUM_TASKS
#     AVTR                   vtr;    ///< Returned by #UV_DBG_ENUM_VTR_ENU
#     UVLICINFO          licinfo;    ///< Returned by #UV_GEN_CHECK_LICENSE
#     DBGTGTOPT        dbgtgtopt;    ///< Returned by #UV_PRJ_GET_DEBUG_TARGET
#     UVSC_PSTAMP powerScaleData;    ///< Returned by #UV_DBG_POWERSCALE_SHOWCODE / #UV_DBG_POWERSCALE_SHOWPOWER
#     REGENUM            regEnum;    ///< Returned by #UV_DBG_ENUM_REGISTERS
#     VARINFO            varInfo;    ///< Returned by #UV_DBG_EVAL_WATCH_EXPRESSION, #UV_DBG_ENUM_VARIABLES
#     MENUENUM           viewInfo;   ///< Returned by #UV_DBG_EVAL_WATCH_EXPRESSION, #UV_DBG_ENUM_VARIABLES
#     char             strbuf[1];    ///< Returned by #UV_DBG_READ_REGISTERS 
#   };    
# } UVSOCK_CMD_RESPONSE;
# Embedded union of  UVSOCK_CMD_RESPONSE
class _U_UVSOCK_CMD_RESPONSE (Union):
    _fields_ = [("err", UVSOCK_ERROR_RESPONSE),
                ("nVal", c_uint),
                ("time", CYCTS),
                ("amem", AMEM),
                ("serdat", SERIO),
                ("vset", VSET),
# Skipped!                
#     BKRSP                  brk;    ///< Returned by #UV_DBG_BP_ENUMERATED / #UV_DBG_CHANGE_BP
#     TRNOPT              trnopt;    ///< Returned by #UV_PRJ_GET_OPTITEM
                ("str", SSTR),
                ("evers", EXTVERS),
                ("tpm", ENUMTPM),
# Skipped!
#     AFLMAP                aflm;    ///< Returned by #UV_DBG_ADR_TOFILELINE                
                ("StopR", BPREASON),
# Skipped!
#     STACKENUM            stack;    ///< Returned by #UV_DBG_ENUM_STACK_ENU
#     TASKENUM              task;    ///< Returned by #UV_DBG_ENUM_TASKS
#     AVTR                   vtr;    ///< Returned by #UV_DBG_ENUM_VTR_ENU
#     UVLICINFO          licinfo;    ///< Returned by #UV_GEN_CHECK_LICENSE
                ("dbgtgtopt", DBGTGTOPT),
                ("powerScaleData", UVSC_PSTAMP),
# Skipped!
#     REGENUM            regEnum;    ///< Returned by #UV_DBG_ENUM_REGISTERS
#     VARINFO            varInfo;    ///< Returned by #UV_DBG_EVAL_WATCH_EXPRESSION, #UV_DBG_ENUM_VARIABLES
#     MENUENUM           viewInfo;   ///< Returned by #UV_DBG_EVAL_WATCH_EXPRESSION, #UV_DBG_ENUM_VARIABLES
                ("strbuf", POINTER(c_char))]
class UVSOCK_CMD_RESPONSE (Structure):
    _anonymous_ = ("_u",) # union _u (type _U_UVSOCK_CMD_RESPONSE) is embedded as anonymous.
    _fields_ = [("cmd", c_int), # enum  UV_OPERATION
                ("status", UV_STATUS), 
                ("_u", _U_UVSOCK_CMD_RESPONSE)]


#
# typedef union _tag_UVSOCK_CMD_DATA {
#   BYTE        raw [SOCK_NDATA];    ///< Command-dependent raw data
# 
#   // Request message, and / or legacy format asynchronous data  
#   PRJDATA              prjdata;    ///< Sent in #UV_PRJ_LOAD / #UV_PRJ_ADD_GROUP / #UV_PRJ_SET_TARGET / #UV_PRJ_ADD_FILE / #UV_PRJ_DEL_GROUP / #UV_PRJ_DEL_FILE / #UV_SET_OUTPUTNAME. Returned by #UV_PRJ_BUILD_OUTPUT / #UV_PRJ_BUILD_COMPLETE / #UV_RTA_MESSAGE
#   AMEM                    amem;    ///< Sent in #UV_DBG_MEM_READ / #UV_DBG_MEM_WRITE / #UV_DBG_DSM_READ
#   SERIO                 serdat;    ///< Sent in #UV_DBG_SERIAL_GET / #UV_DBG_SERIAL_PUT
#   VSET                    vset;    ///< Sent in #UV_DBG_VTR_GET / #UV_DBG_VTR_SET / #UV_DBG_CALC_EXPRESSION
#   TRNOPT                trnopt;    ///< Sent in #UV_PRJ_GET_OPTITEM / #UV_PRJ_SET_OPTITEM
#   SSTR                    sstr;    ///< Sent in #UV_PRJ_ENUM_FILES. Returned by #UV_DBG_CMD_OUTPUT
#   BKPARM                bkparm;    ///< Sent in #UV_DBG_CREATE_BP
#   BKCHG                  bkchg;    ///< Sent in #UV_DBG_CHANGE_BP
#   DBGTGTOPT          dbgtgtopt;    ///< Sent in #UV_PRJ_SET_DEBUG_TARGET
#   ADRMTFL              adrmtfl;    ///< Sent in #UV_DBG_ADR_TOFILELINE
#   iSHOWSYNC          ishowsync;    ///< Sent in #UV_DBG_ADR_SHOWCODE
#   iVTRENUM            ivtrenum;    ///< Sent in #UV_DBG_ENUM_VTR
#   EXECCMD              execcmd;    ///< Sent in #UV_DBG_EXEC_CMD
#   iPATHREQ            iPathReq;    ///< Sent in #UV_PRJ_GET_OUTPUTNAME / #UV_PRJ_GET_CUR_TARGET
#   UVSC_PSTAMP   powerScaleData;    ///< Sent in #UV_DBG_POWERSCALE_SHOWPOWER
#   iSTKENUM            iStkEnum;    ///< Sent in #UV_DBG_ENUM_STACK
#   PGRESS                pgress;    ///< Sent in #UV_PRJ_CMD_PROGRESS
#   ENUMTPM              enumtpm;    ///< Sent in #UV_DBG_ENUM_SYMTP
#   iINTERVAL          iInterval;    ///< Sent in #UV_DBG_WAKE
#   UINT                    nVal;    ///< Sent in #UV_DBG_STEP_HLL_N, UV_DBG_STEP_INTO_N, UV_DBG_STEP_INSTRUCTION_N 
#   xU64                nAddress;    ///< Sent in #UV_DBG_RUN_TO_ADDRESS 
#   UVSOCK_OPTIONS     uvSockOpt;    ///< Sent in #UV_GEN_SET_OPTIONS  
# 
#   // Command response, or new format asynchronous message data
#   UVSOCK_CMD_RESPONSE   cmdRsp;    ///< Command response formatted data
# } UVSOCK_CMD_DATA;
# 
class UVSOCK_CMD_DATA (Union):
    _fields_ = [("raw", c_byte * SOCK_NDATA), # raw data buffer 
                ("prjdata", PRJDATA),
                ("amem", AMEM),
                ("serdat", SERIO),
                ("vset", VSET),
# --- Skipped!
#   TRNOPT                trnopt;    ///< Sent in #UV_PRJ_GET_OPTITEM / #UV_PRJ_SET_OPTITEM
                ("sstr", SSTR),
# --- Skipped!                              
#   BKPARM                bkparm;    ///< Sent in #UV_DBG_CREATE_BP
#   BKCHG                  bkchg;    ///< Sent in #UV_DBG_CHANGE_BP
#   DBGTGTOPT          dbgtgtopt;    ///< Sent in #UV_PRJ_SET_DEBUG_TARGET
#   ADRMTFL              adrmtfl;    ///< Sent in #UV_DBG_ADR_TOFILELINE
#   iSHOWSYNC          ishowsync;    ///< Sent in #UV_DBG_ADR_SHOWCODE
#   iVTRENUM            ivtrenum;    ///< Sent in #UV_DBG_ENUM_VTR
                ("execcmd", EXECCMD),              
                ("iPathReq", iPATHREQ),
                ("powerScaleData", UVSC_PSTAMP),
                ("iStkEnum", iSTKENUM),
                ("pgress", PGRESS),
                ("enumtpm", ENUMTPM),
                ("iInterval", iINTERVAL),
                ("nVal", c_uint),
                ("nAddress", xU64),
                ("uvSockOpt", UVSOCK_OPTIONS),
                ("cmdRsp", UVSOCK_CMD_RESPONSE)]
               

# typedef struct _tag_UVSOCK_CMD  {
#   UINT             m_nTotalLen;    ///< Total message length (bytes)
#   UV_OPERATION          m_eCmd;    ///< Command code
#   UINT               m_nBufLen;    ///< Length of Data Section (bytes)
#   xU64                  cycles;    ///< Cycle value (Simulation mode only)
#   double                tStamp;    ///< time-stamp (Simulation mode only)
#   UINT                    m_Id;    ///< Reserved
#   UVSOCK_CMD_DATA         data;    ///< Data Section (Command code dependent data)
# } UVSOCK_CMD;
class UVSOCK_CMD (Structure):
    _fields_ = [("m_nTotalLen", c_uint),
                ("m_eCmd", c_int),  # enum UV_OPERATION
                ("m_nBufLen", c_uint),
                ("cycles", xU64),
                ("tStamp", c_double),
                ("m_Id", c_uint),
                ("data", UVSOCK_CMD_DATA)]

# typedef union _tag_UVSC_CB_DATA {
#   UVSOCK_CMD msg;                       ///< UVSOCK fromatted message (returned when UVSC_CB_TYPE is #UVSC_CB_ASYNC_MSG, #UVSC_CB_BUILD_OUTPUT_MSG, #UVSC_CB_CMD_OUTPUT_MSG or #UVSC_CB_PROGRESS_BAR_MSG)
#   UVSC_STATUS err;                      ///< Error notification (returned when UVSC_CB_TYPE is #UVSC_CB_ERROR)
#   int iConnHandle;                      ///< UVSC connection handle (returned when UVSC_CB_TYPE is #UVSC_CB_DISCONNECTED)
# } UVSC_CB_DATA;
class  UVSC_CB_DATA (Union):
    _fields_ = [("msg", UVSOCK_CMD),
                ("err", UVSC_STATUS),
                ("iConnHandle", c_int)]





# Callback function type
# typedef void (*uvsc_cb)(void* cb_custom, UVSC_CB_TYPE type, UVSC_CB_DATA *data);
uvsc_cb_t = CFUNCTYPE(None, c_void_p, UVSC_CB_TYPE, POINTER(UVSC_CB_DATA))
log_cb_t  = CFUNCTYPE(None, c_char_p, c_int);
