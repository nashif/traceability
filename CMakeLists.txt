cmake_minimum_required(VERSION 3.15)

project(traceme VERSION 0.1)

# Require dot, treat the other components as optional
find_package(Doxygen
             REQUIRED dot
             OPTIONAL_COMPONENTS mscgen dia)

add_subdirectory(src)
add_subdirectory (docs)