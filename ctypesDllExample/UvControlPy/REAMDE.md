# UvControlPy `ctypes` DLL-wrapper example
This project contains a `ctypes` DLL accessing project which originally was developed for to control the Keil uVision IDE.  

Open the project in _VS Code_ from the root DIR (contains `.vscode`):
```shell
cd ./UvControlPy && code .
```

The project contains: 
---
- The _uvctrl_ lib.
- The native DLL project *uvctrl/keil_uvsc*  
  A **mocked** *keil_uvsc* DLL with own _VS Code_ [C++ debug build](uvctrl/keil_uvsc/README)
- The _test-framework_
  A `pytest` based test-framework for executing the `ctypes` lib. Do testing as follows:
  - Install first [pytests](#install-pytest) 
  - Execute tests from [command line](#run-pytest) or in the [debugger](#debug-pytest).
   

## Install `pytest`
The `pytest` package (if not installed) is recommend to be installed via `.venv` under the current DIR as follows:

```shell
python -m venv ctypesDllExample/UvControlPy/.venv
# Note: '.venv/bin/activate' is valid for Windows 'MSYS2' but may differ for others e.g. Linux.
source ctypesDllExample/UvControlPy/.venv/bin/activate
# On Windows PowerShell or cmd.exe you also can run: 
# ctypesDllExample/UvControlPy/.venv/bin/Activate.ps1 or activate.bat

# Install `pytest` into the activated virtual environment:
python -m pip install pytest
```

## Run `pytest`
Run the tests from the repository root:

```shell
python -m pytest ctypesDllExample/UvControlPy/testing -q
```

## Debug `pytest`
The project `launch.json` has already configured pytest debug-launcher `Pytest: Debug Current Module` which must be selected for the _Run And Debug_ module via its _drop-box_ as the current debug-config.  

**Note** the following:  
- Adapt python-path `"python": "${workspaceFolder}/.venv/bin/python.exe"` of `launch.json` to match your venv-bin-path!
- The _Debug Test_ option of the _Testing_ module **is not supported** (TODO: check why?). Use the proposed `Pytest: Debug Current Module` launch-config.


