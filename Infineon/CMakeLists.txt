cmake_minimum_required(VERSION 3.20)

set(CMAKE_CXX_COMPILER "g++" CACHE STRING "UCRT64 G++ compiler")

project(UVSC64Mock LANGUAGES CXX)

add_library(UVSC64Mock SHARED
    UvControlPy/uvctrl/keil_uvsc/UVSC64Mock.cpp
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
    # Note: UCTR64 generates Windows executables not relying on MSYS DLLs. Thus -static-libxxx
    # seems not to be necessary. But if this DLL should ever be run on Win-PCs without MSYS we shall
    # use the -static-libxxx link flags to link all required DLLs into this DLL.
    #target_link_options(UVSC64Mock PRIVATE -static-libgcc -static-libstdc++)
endif()
