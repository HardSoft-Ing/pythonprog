/**
 * AI generated DLL to mock the uVision-API DLL to avoid installing uVision.
 * Note: This DLL is just created for to playing with python ctypes.
 */

#include <stdio.h>
#include <string.h>

#ifndef WIN32
#define WIN32
#endif
#define _IN_DLL_
#include "UVSC_C.h"

#define UVSC_HANDLE 1
#define UVSC_COMMAND_MAX sizeof(((EXECCMD *)0)->sCmd.szStr)

static int g_initialized = 0;
static int g_connected = 0;
static int g_debugging = 0;
static int g_executing = 0;
static int g_last_port = UVSC_PORT_AUTO;
static char g_command_output[UVSC_COMMAND_MAX];

static int valid_handle(int handle) {
    return g_initialized && g_connected && handle == UVSC_HANDLE;
}

static int valid_port_range(int min_port, int max_port) {
    return min_port >= UVSC_MIN_AUTO_PORT &&
           max_port <= UVSC_MAX_AUTO_PORT &&
           min_port <= max_port;
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    switch (ul_reason_for_call) {
        case DLL_PROCESS_ATTACH:
        case DLL_THREAD_ATTACH:
        case DLL_THREAD_DETACH:
        case DLL_PROCESS_DETACH:
            break;
    }
    return TRUE;
}

UVSC_STATUS UVSC_Init(int uvMinPort, int uvMaxPort) {
    if (!valid_port_range(uvMinPort, uvMaxPort)) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    g_initialized = 1;
    g_connected = 0;
    g_debugging = 0;
    g_executing = 0;
    g_last_port = UVSC_PORT_AUTO;
    g_command_output[0] = '\0';
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_UnInit(void) {
    if (!g_initialized) {
        return UVSC_STATUS_NOT_INIT;
    }

    g_initialized = 0;
    g_connected = 0;
    g_debugging = 0;
    g_executing = 0;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_OpenConnection(
    char *name,
    int *connection_handle,
    int *port,
    char *uv_command,
    UVSC_RUNMODE run_mode,
    uvsc_cb callback,
    void *callback_custom,
    char *log_file_name,
    xBOOL log_file_append,
    log_cb log_callback) {
    (void)name;
    (void)uv_command;
    (void)callback;
    (void)callback_custom;
    (void)log_file_name;
    (void)log_file_append;
    (void)log_callback;

    if (!g_initialized) {
        return UVSC_STATUS_NOT_INIT;
    }
    if (connection_handle == NULL || port == NULL ||
        (run_mode != UVSC_RUNMODE_NORMAL && run_mode != UVSC_RUNMODE_LABVIEW)) {
        return UVSC_STATUS_INVALID_PARAM;
    }
    if (g_connected) {
        return UVSC_STATUS_INVALID_PARAM;
    }
    if (*port != UVSC_PORT_AUTO &&
        (*port < UVSC_MIN_AUTO_PORT || *port > UVSC_MAX_AUTO_PORT)) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    g_connected = 1;
    g_last_port = *port == UVSC_PORT_AUTO ? UVSC_MIN_AUTO_PORT : *port;
    *connection_handle = UVSC_HANDLE;
    *port = g_last_port;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_CloseConnection(int connection_handle, xBOOL terminate) {
    (void)terminate;

    if (!valid_handle(connection_handle)) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    g_connected = 0;
    g_debugging = 0;
    g_executing = 0;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_DBG_ENTER(int connection_handle) {
    if (!valid_handle(connection_handle)) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    g_debugging = 1;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_DBG_EXIT(int connection_handle) {
    if (!valid_handle(connection_handle)) {
        return UVSC_STATUS_INVALID_PARAM;
    }
    if (g_executing) {
        return UVSC_STATUS_COMMAND_ERROR;
    }

    g_debugging = 0;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_DBG_START_EXECUTION(int connection_handle) {
    if (!valid_handle(connection_handle) || !g_debugging) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    g_executing = 1;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_DBG_STOP_EXECUTION(int connection_handle) {
    if (!valid_handle(connection_handle) || !g_debugging) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    g_executing = 0;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_DBG_STATUS(int connection_handle, int *status) {
    if (!valid_handle(connection_handle) || status == NULL || !g_debugging) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    *status = g_executing;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_DBG_RESET(int connection_handle) {
    if (!valid_handle(connection_handle) || !g_debugging) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    g_executing = 0;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_DBG_EXEC_CMD(
    int connection_handle,
    EXECCMD *command,
    int command_length) {
    size_t command_size;

    if (!valid_handle(connection_handle) || !g_debugging ||
        command == NULL || command_length < (int)sizeof(EXECCMD)) {
        return UVSC_STATUS_INVALID_PARAM;
    }
    if (command->sCmd.nLen <= 0 ||
        command->sCmd.nLen != command_length) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    command_size = strnlen(command->sCmd.szStr, sizeof(command->sCmd.szStr));
    if (command_size == 0 || command_size >= sizeof(g_command_output)) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    snprintf(g_command_output, sizeof(g_command_output),
             "fake UVSC command: %.235s", command->sCmd.szStr);
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_GetCmdOutputSize(
    int connection_handle,
    int *command_output_size) {
    if (!valid_handle(connection_handle) || command_output_size == NULL) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    *command_output_size = (int)strlen(g_command_output) + 1;
    return UVSC_STATUS_SUCCESS;
}

UVSC_STATUS UVSC_GetCmdOutput(
    int connection_handle,
    char *command_output,
    int command_output_length) {
    size_t output_size;

    if (!valid_handle(connection_handle) || command_output == NULL ||
        command_output_length <= 0) {
        return UVSC_STATUS_INVALID_PARAM;
    }

    output_size = strlen(g_command_output) + 1;
    if ((size_t)command_output_length < output_size) {
        return UVSC_STATUS_BUFFER_TOO_SMALL;
    }

    memcpy(command_output, g_command_output, output_size);
    return UVSC_STATUS_SUCCESS;
}
