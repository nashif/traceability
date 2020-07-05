
find_package(Doxygen REQUIRED)
find_package(Sphinx REQUIRED)

# Find all the public headers
get_target_property(MODULE_A_PUBLIC_HEADER_DIR module_a INTERFACE_INCLUDE_DIRECTORIES)
file(GLOB_RECURSE MODULE_A_PUBLIC_HEADERS ${MODULE_A_PUBLIC_HEADER_DIR}/*.h)

#This will be the main output of our command
set(DOXYGEN_INDEX_FILE ${CMAKE_CURRENT_SOURCE_DIR}/html/index.html)

target_include_directories(module_a PUBLIC .)

set(DOXYGEN_INPUT_DIR "${PROJECT_SOURCE_DIR}/module_a ${PROJECT_SOURCE_DIR}/test")
set(DOXYGEN_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/doxygen)
set(DOXYGEN_INDEX_FILE ${DOXYGEN_OUTPUT_DIR}/html/index.html)
set(DOXYFILE_IN ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in)
set(DOXYFILE_OUT ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile)
set(DOXYFILE_REQUIREMENT_TAG "TRCSRS")

configure_file(${DOXYFILE_IN} ${DOXYFILE_OUT} @ONLY)
file(MAKE_DIRECTORY ${DOXYGEN_OUTPUT_DIR}) #Doxygen won't create this for us

add_custom_command(OUTPUT ${DOXYGEN_INDEX_FILE}
                   DEPENDS ${MODULE_A_PUBLIC_HEADERS} ${PROJECT_SOURCE_DIR}/test/suite_1/*.c
                   COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYFILE_OUT}
                   MAIN_DEPENDENCY ${DOXYFILE_OUT} ${DOXYFILE_IN}
                   COMMENT "Generating docs"
                   VERBATIM)

add_custom_target(Doxygen ALL DEPENDS ${DOXYGEN_INDEX_FILE})

set(SPHINX_SOURCE ${CMAKE_CURRENT_SOURCE_DIR})
set(SPHINX_BUILD ${CMAKE_CURRENT_BINARY_DIR}/sphinx)
set(SPHINX_INDEX_FILE ${SPHINX_BUILD}/index.html)
set(RST_OUT ${SPHINX_BUILD}/rst)


set(EXTRACT_CONTENT_COMMAND
  ${CMAKE_COMMAND} -E env
  ${PYTHON_EXECUTABLE} scripts/extract_content.py
  # Ignore any files in the output directory.
  --ignore ${CMAKE_CURRENT_BINARY_DIR}
  --project-root ${PROJECT_SOURCE_DIR}
  # Copy all files in doc to the rst folder.
  "*:docs:${RST_OUT}"
  # We want to copy the .rst files in samples/ and boards/ to the rst
  # folder, and also the doc folder inside rst.
  #
  # Some files refer to items in samples/ and boards/ relative to
  # their actual position in the Zephyr tree. For example, in
  # subsystems/sensor.rst:
  #
  # .. literalinclude:: ../../samples/sensor/mcp9808/src/main.c
  #
  VERBATIM # optional
)


set(EXTRACT_CONTENT_COMMAND1
  ${CMAKE_COMMAND} -E make_directory ${RST_OUT}

  VERBATIM # optional
)

add_custom_target(
  content
  COMMAND ${CMAKE_COMMAND} -E make_directory ${RST_OUT}
  # Copy all files in doc/ to the rst folder
  COMMAND ${EXTRACT_CONTENT_COMMAND}
  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
  COMMENT "Copying files to ${RST_OUT}"

)

# Only regenerate Sphinx when:
# - Doxygen has rerun
# - Our doc files have been updated
# - The Sphinx config has been updated

add_custom_command(OUTPUT ${SPHINX_INDEX_FILE}
                   COMMAND
                   ${SPHINX_EXECUTABLE} -E  -b html
                   # Tell Breathe where to find the Doxygen output
                   -Dbreathe_projects.traceability=${DOXYGEN_OUTPUT_DIR}/xml
                   ${RST_OUT} ${SPHINX_BUILD}
                   WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
                   DEPENDS
                   # Other docs files you want to track should go here (or in some variable)
                   ${RST_OUT}/docs/index.rst
                   ${RST_OUT}/docs/SRS.rst
                   ${RST_OUT}/docs/tests.rst

                   ${DOXYGEN_INDEX_FILE}
                   MAIN_DEPENDENCY ${SPHINX_SOURCE}/conf.py
                   COMMENT "Generating documentation with Sphinx")

# Nice named target so we can run the job easily
add_custom_target(Sphinx ALL DEPENDS ${SPHINX_INDEX_FILE})


add_dependencies(Sphinx content)