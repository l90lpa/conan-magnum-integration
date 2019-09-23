cmake_minimum_required(VERSION 2.8.12)
project(test_package)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test-package test_package.cpp)
target_link_libraries(test-package ${CONAN_LIBS})
set_target_properties(test-package 
    PROPERTIES 
    	CXX_STANDARD 17
    	CXX_STANDARD_REQUIRED ON
    	CXX_EXTENSIONS OFF
)

add_executable(test-eigen EXCLUDE_FROM_ALL test_eigen.cpp)
target_link_libraries(test-eigen ${CONAN_LIBS})
set_target_properties(test-eigen
      PROPERTIES 
    	CXX_STANDARD 17
    	CXX_STANDARD_REQUIRED ON
    	CXX_EXTENSIONS OFF)
