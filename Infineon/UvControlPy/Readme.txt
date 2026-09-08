Python wrapper-application for Keil UVSC API, which is needed to control the Keil UV-IDE.

Note:
Actually only the file ".\uvctrl\keil_uvsc\UVSC.dll"  is required by uvctrl.libuvctrl.py 
which is dynamically loaded as ctypes dll. The USCV h-files of ".\uvctrl\keil_uvsc"  are 
just for documentation purpose. 
