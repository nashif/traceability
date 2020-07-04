cmake_minimum_required(VERSION 3.15)

project(traceme VERSION 0.1)

set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})

#SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)


# We declare a variable to select what to build set
set(TARGET_GROUP production CACHE STRING "What Should I Build?")

add_subdirectory(module_a)

if(TARGET_GROUP STREQUAL production)
# If we had any files that ONLY were compiled into our release, for example startup code,
  # it's really handy to put it here.
    add_subdirectory(main)
    add_subdirectory(docs)
elseif(TARGET_GROUP STREQUAL test)
# Our tests need to let CTest know we're running tests
    include(CTest)

# It also needs to understand we have code in source and test directories
    add_subdirectory(external)
    add_subdirectory(test)
else()
    message(FATAL_ERROR "I don't know the TARGET_GROUP you gave me! (${TARGET_GROUP})")
endif()