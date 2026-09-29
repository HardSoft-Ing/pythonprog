import os
from pathlib import Path

import pytest

from uvctrl.libuvctrl import IFX_UVSCPORT, LibUvCtrl, UVSC_MAX_AUTO_PORT


MOCK_DLL_PATH = (
    Path(__file__).resolve().parents[1]
    / "uvctrl"
    / "keil_uvsc"
    / "UVSC64Mock.dll"
)


def _dll_path() -> Path:
    configured_path = os.environ.get("UVCTRL_TEST_DLL")
    if configured_path:
        return Path(configured_path)
    return MOCK_DLL_PATH


@pytest.fixture
def uvctrl():
    dll_path = _dll_path()
    if not dll_path.is_file():
        pytest.skip(f"UVSC test DLL was not found: {dll_path}")

    controller = LibUvCtrl(str(dll_path))
    yield controller

    if controller.cint_uvscHandle.value != -1:
        controller.uvsc_close_connection()


def test_debug_command_lifecycle(uvctrl):
    uvctrl.uvsc_init(IFX_UVSCPORT, UVSC_MAX_AUTO_PORT, True)
    assert uvctrl.cint_uvscHandle.value != -1

    uvctrl.uvsc_dbg_enter()
    assert uvctrl.uvsc_dbg_getstatus() == 0

    uvctrl.uvsc_dbg_start_execution()
    assert uvctrl.uvsc_dbg_getstatus() == 1

    uvctrl.uvsc_dbg_start_execution()
    assert uvctrl.uvsc_dbg_getstatus() == 1

    uvctrl.uvsc_dbg_stop_execution()
    assert uvctrl.uvsc_dbg_getstatus() == 0

    uvctrl.uvsc_dbg_stop_execution()
    uvctrl.uvsc_dbg_exec_cmd("log off; coverage asm", True)
    assert uvctrl.uvsc_get_cmd_output() == (
        "fake UVSC command: log off; coverage asm"
    )

    uvctrl.uvsc_dbg_exit()