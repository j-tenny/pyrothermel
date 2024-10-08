# Pyrothermel
Model fire rate of spread, fire intensity, tree mortality, and more for surface fires and crown fires using the extended 
Rothermel model. Pyrothermel provides a Python interface to the same C++ code that underlies [Behave](https://github.com/firelab/behave), Flammap, and other 
software tools maintained by the Missoula Fire Lab*.

Please submit bugs and feature requests as Github issues. Expect significant API changes in early versions of this package. 

*Pyrothermel and its authors are not associated with the Missoula Fire Lab or the US Government.

## Dependencies
- [CMake](https://cmake.org/download/)
- Python >= 3.8
- setuptools
- A C++ compiler
- [LLVM/Clang](https://clang.llvm.org/) (not sure if this is still required)

## Download
```bash
git clone https://github.com/j-tenny/pyrothermel.git
```

## Build
```bash
python setup.py bdist_wheel
```

## Install
Replace filename of wheel as needed

```bash
pip install dist/pyrothermel-0.0.1-cp38-cp38-win_amd64.whl --force-reinstall
```

## Test example
```bash
python example.py
```
