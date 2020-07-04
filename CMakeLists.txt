cmake_minimum_required(VERSION 3.15)

project(traceme VERSION 0.1)

set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})

# Require dot, treat the other components as optional
find_package(Doxygen
             REQUIRED dot
             OPTIONAL_COMPONENTS mscgen dia)

add_subdirectory(src)
add_subdirectory (docs)