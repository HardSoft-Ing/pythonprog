cmake_minimum_required(VERSION 3.20)

set(CMAKE_C_COMPILER "gcc" CACHE STRING "UCRT64 GCC compiler")
#set(CMAKE_C_COMPILER "/c/Tools/msys64/ucrt64/bin/gcc.exe" CACHE FILEPATH "UCRT64 GCC compiler")

project(UVSC64Mock LANGUAGES C)

add_library(UVSC64Mock SHARED
    UvControlPy/uvctrl/keil_uvsc/UVSC64Mock.c
)

target_include_directories(UVSC64Mock PRIVATE
    UvControlPy/uvctrl/keil_uvsc
)

target_compile_definitions(UVSC64Mock PRIVATE WIN32)

set_target_properties(UVSC64Mock PROPERTIES
    OUTPUT_NAME "UVSC64Mock"
    PREFIX ""
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/UvControlPy/uvctrl/keil_uvsc"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/UvControlPy/uvctrl/keil_uvsc"
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
)

if(MSVC)
    target_compile_options(UVSC64Mock PRIVATE /W4)
else()
    target_compile_options(UVSC64Mock PRIVATE -Wall -Wextra)
    target_link_options(UVSC64Mock PRIVATE -static-libgcc)
endif()
