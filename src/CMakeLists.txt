
add_library(traceability STATIC mylib.c)

add_executable(traceme main.c)

target_link_libraries(traceme traceability)

