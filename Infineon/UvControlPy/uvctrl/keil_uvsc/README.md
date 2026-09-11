# UVSC64Mock C++ Target

This directory contains the local C++ mock implementation of the Keil UVSC DLL used by the Python wrapper tests.

## Files

- `UVSC64Mock.cpp`: mock UVSC implementation.
- `UVSC_C.h` and `UVSOCK.h`: UVSC API declarations used by the implementation.
- `CMakeLists.txt`: CMake project for building `UVSC64Mock.dll`.
- `.vscode/tasks.json`: configure, build, and clean tasks for this target.
- `.vscode/launch.json`: C++ GDB attach configuration.

## Build

Open this directory as the VS Code workspace folder, then run:

```text
CMake: Debug Build UVSC64Mock.dll
```

The build task first configures with Ninja and places the build files in `build/uvsc64`. The resulting DLL is written beside the source files:

```text
UVSC64Mock.dll
```

Equivalent MSYS2/UCRT64 commands from this directory are:

```bash
cmake -S . -B build/uvsc64 -G Ninja -DCMAKE_BUILD_TYPE=Debug -DCMAKE_CXX_COMPILER=g++
cmake --build build/uvsc64 --config Debug --parallel
```

The UCRT64 tools are expected under `C:/Tools/msys64/ucrt64/bin`.

## C++ debugging alongside Python

1. Start the Python debugger for `UvControlPy/test_uvctrl.py` and stop at a breakpoint after the mock DLL has been loaded.
2. Open the C++ Run and Debug view for this target and select `(gdb) Attach`.
3. In the process picker, select the Python process that has `UVSC64Mock.dll` loaded. If several Python processes exist, identify it with:

   ```bash
   tasklist.exe /m UVSC64Mock.dll
   ```

4. Continue or set C++ breakpoints in `UVSC64Mock.cpp`.

The DLL must already be loaded by the Python process. If `tasklist.exe /m UVSC64Mock.dll` returns no process, attach after Python has constructed `LibUvCtrl`.

## Clean build

Run the VS Code task:

```text
CMake: Clean UVSC64Mock Build
```

Or run:

```bash
cmake --build build/uvsc64 --target clean
```
