# Infineon UVSC Python/C++ Integration

This directory contains the Python wrapper used to control a Keil uVision debugger through the UVSC API.

## Runtime dependencies

`UvControlPy/uvctrl/libuvctrl.py` loads the UVSC shared library with `ctypes` when `LibUvCtrl` is created.

- Production use expects Keil's `UVSC.dll`. `test_uvctrl.py` first checks the `SysDevToolPath` environment variable and uses:
  `SysDevToolPath + SDK90\\UV4\\UVSC.dll`.
- For local development and tests without a Keil installation, the test falls back to `UvControlPy/uvctrl/keil_uvsc/UVSC64Mock.dll`.
- The Python declarations and wrapper code are in `UvControlPy/uvctrl/uvsc_defs.py` and `UvControlPy/uvctrl/libuvctrl.py`.
- A compatible DLL must export the UVSC functions used by the wrapper, including initialization, connection, debugger control, command, status, and close functions.

## Python usage

Run the example test from the `Infineon` directory or from the repository root:

```bash
python UvControlPy/test_uvctrl.py
python Infineon/UvControlPy/test_uvctrl.py
```

The test expects a reachable Keil uVision/UVSC service when using the real `UVSC.dll`. With the mock DLL, it exercises the wrapper API locally but does not provide a real uVision connection.

## C++ project

The mock DLL source, CMake project, CMake tasks, and C++ debugger configuration are kept in one target directory:

[Build and debug the keil_uvsc target](UvControlPy/uvctrl/keil_uvsc/README.md)
