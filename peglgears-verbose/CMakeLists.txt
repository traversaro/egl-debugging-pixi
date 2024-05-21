cmake_minimum_required(VERSION 3.16)

project(peglgears-verbose)

find_package(OpenGL REQUIRED COMPONENTS EGL)

add_executable(peglgears-verbose peglgears-verbose.c)

target_link_libraries(peglgears-verbose PRIVATE OpenGL::EGL)

find_library(MATH_LIBRARY m)
if(MATH_LIBRARY)
    target_link_libraries(peglgears-verbose PRIVATE ${MATH_LIBRARY})
endif()
