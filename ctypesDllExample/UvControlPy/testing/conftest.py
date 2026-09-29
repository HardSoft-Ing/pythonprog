# The 'conftest.py' is loaded by 'pytest' for test-preparation. 
# Each DIR containing test_xxx.py modules may provide a 'conftest.py'.

import sys
from pathlib import Path


# --- Since the test-module(s) are somewhere below 'UvControlPy' we need to add root 'UvControlPy'
#     to the python sys-lib-path to access lib DIR 'UvControlPy/uvctrl'. 

THIS_FILE_ABSPATH = Path(__file__).resolve()
# Point to 2'nd parent DIR which is 'UvControlPy'.
UVCONTROL_ROOT = THIS_FILE_ABSPATH.parents[1]

# TODO: Check if this is really needed. 
if str(UVCONTROL_ROOT) not in sys.path:
    sys.path.insert(0, str(UVCONTROL_ROOT))