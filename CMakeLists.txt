cmake_minimum_required(VERSION 3.15)
project(pyrothermel LANGUAGES CXX)

# Use C++14 or upgrade to C++17 if needed
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Behave source files
file(GLOB_RECURSE BEHAVE_SOURCES CONFIGURE_DEPENDS "src/behave/*.cpp")
file(GLOB_RECURSE BEHAVE_HEADERS CONFIGURE_DEPENDS "src/behave/*.h")

# Add pybind11 subdirectory if bundled (optional, prefer find_package otherwise)
add_subdirectory(pybind11)

# Add the bindings
pybind11_add_module(pyrothermel_bindings
    pyrothermel/pyrothermel_bindings.cpp
    ${BEHAVE_SOURCES}
    ${BEHAVE_HEADERS}  # Not required, but useful for IDEs
)

target_include_directories(pyrothermel_bindings PRIVATE
    src/behave
)