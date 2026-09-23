# TK Example Requirements
To run this python GUI apps you need to install package `tkinter` as follows:

## Python Linux
On Linux you usually run `pip` to install `tkinter`:
``` bash
pip install tkinter
``` 
Note: Modern Linux may rquires to install it via your packet-manager. 

## Install for Windows MSYS2
For MSYS2 you only can install `tkinter` for _MINGW64_ or _UCRT64_ based python versions, where the installation needs to be done via the `pacman` packetmanager. The _MSYS2_ python NOT supports it!

### Search for available python `tkinter` modules
``` bash
# List availables modules from repository and grep for 'tkinter'
pacman -Sl |grep -i tkinter
``` 
This may generates out put like:
```bash
clangarm64 _mingw-w64-clang-aarch64-python-customtkinter_ 6.0.0-1  
ucrt64 _mingw-w64-ucrt-x86_64-python-customtkinter_ 6.0.0-1  
clang64 _mingw-w64-clang-x86_64-python-customtkinter_ 6.0.0-1  
```

### Install python `tkinter` for _UCRT64_
``` bash
# Install with --needed to only install if not existing or update is required. 
pacman -S --needed mingw-w64-ucrt-x86_64-python-customtkinter
``` 


