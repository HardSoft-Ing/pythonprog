from pathlib import Path

# Added file-wrapper for debugging: 
# It codes the special functions called by the `with` statement so we can trace it!
class FileWrapper:
    """Small file wrapper with explicit, safely managed operations."""

    def __init__(self, path, mode="r", encoding="utf-8"):
        self.path = Path(path)
        self.mode = mode
        self.encoding = encoding
        self._handle = None

    def open(self):
        self._handle = self.path.open(self.mode, encoding=self.encoding)
        return self

    def read(self, size=-1):
        if self._handle is None:
            raise ValueError("File is not open")
        return self._handle.read(size)

    def write(self, data):
        if self._handle is None:
            raise ValueError("File is not open")
        return self._handle.write(data)

    def close(self):
        if self._handle is not None:
            self._handle.close()
            self._handle = None

    # Called automatically when execution enters a `with` block.
    # It must return the object that will be assigned to the `as` target.
    def __enter__(self):
        return self.open()

    # Called automatically when execution leaves a `with` block.
    # The exception details are passed in if the block exits with an error;
    # returning False lets Python propagate the exception normally.
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"#Dbg __exit__(): exc_type={exc_type}, exc_value={exc_value}")
        self.close()
        return False


TST_FILE = "with_example.txt"
NON_FILE = "None.txt"
BIN_FILE = "output.bin"


with FileWrapper(TST_FILE, "w") as file:
    file.write("Hello, Python with statement!")

with FileWrapper(TST_FILE) as file:
    print(f"File-Data: {file.read()}")

try:
    with FileWrapper(NON_FILE) as file:
        print(f"File-Data: {file.read()}")
except FileNotFoundError:
    print(f"File not found: {NON_FILE}")

with open(BIN_FILE, "wb") as f:
    # Write binary bytes and text-literal
    #f.write(bytes([0x01, 0xaa, 0xbb, 0xcc]) + b": Hello Binary") 
    f.write(bytes([1, 170, 187, 204]) + b": Hello Binary") 

# Binary files shall be opened for reading via "rb"  
with open(BIN_FILE, "rb") as f:
    data = f.read()          # Using a bytes literal
    print("Bin-Text:", data)

try:
# Now we provoke an error for `with`:
# Reading the binary-file raises and exception but `with` takes care to close the file 
# it did open (see `FileWrapper` log-traces)!
    with FileWrapper(BIN_FILE) as file:
        print(f"File-Data: {file.read()}")
except Exception as exec:
    # Note: We can lazily print as 'reason' {exec}' since it converts to {exec.__str__()}.
    # And `exec` has as base `Exception` but its behavior is defined by the latest derived class.
    print(f"Got read-error type: {type(exec)}, reason: {exec}")

