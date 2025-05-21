from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import glob
import pybind11

class get_pybind_include:
    def __str__(self):
        return pybind11.get_include()

sources = ['pyrothermel/pyrothermel_bindings.cpp'] + glob.glob('src/behave/*.cpp')

ext_modules = [
    Extension(
        "pyrothermel_bindings",
        sources=sources,
        include_dirs=[
            get_pybind_include(),
            'src/behave',
        ],
        language="c++",
    ),
]

setup(ext_modules=ext_modules, cmdclass={"build_ext": build_ext})
