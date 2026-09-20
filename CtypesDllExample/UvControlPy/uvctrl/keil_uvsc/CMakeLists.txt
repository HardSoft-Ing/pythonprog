cmake_minimum_required(VERSION 3.16)

project(UVSC64Mock LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(UVSC64Mock SHARED
    UVSC64Mock.cpp
)

target_include_directories(UVSC64Mock
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}
)

target_compile_definitions(UVSC64Mock
    PRIVATE
        WIN32
        _IN_DLL_
)

target_compile_options(UVSC64Mock
    PRIVATE
        -Wall
        -Wextra
)

set_target_properties(UVSC64Mock PROPERTIES
    OUTPUT_NAME "UVSC64Mock"
    PREFIX ""
)

# Optional: make the generated DLL easy to find next to the source tree
set_target_properties(UVSC64Mock PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)
