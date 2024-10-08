# Pyrothermel
Model fire rate of spread, fire intensity, tree mortality, and more for surface fires and crown fires using the extended 
Rothermel model. Pyrothermel provides a Python interface to the same C++ code that underlies Behave, Flammap, and other 
software tools maintained by the Missoula Fire Lab. 

## Dependencies
- [CMake](https://cmake.org/download/)
- setuptools
- A C++ compiler
- [LLVM/Clang](https://clang.llvm.org/)?


## Build
```bash
python setup.py bdist_wheel
```

## Install
Replace filename of wheel as needed

```bash
pip install dist/pyrothermel-0.0.1-cp311-cp311-win_amd64.whl --force-reinstall
```

## Test example
```bash
python example.py
```
