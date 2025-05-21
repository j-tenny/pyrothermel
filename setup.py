from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
import glob

class get_pybind_include(object):
    """Helper class to determine the pybind11 include path"""
    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11
        return pybind11.get_include(self.user)

# Include all .cpp files in src/behave
behave_sources = glob.glob('src/behave/*.cpp')

ext_modules = [
    Extension(
        'pyrothermel_bindings',  # Ensure this matches your package structure
        sources=['pyrothermel/pyrothermel_bindings.cpp'] + behave_sources,
        include_dirs=[
            get_pybind_include(),
            get_pybind_include(user=True),
            'pybind11/include',
            'src/behave',
        ],
        language='c++',
    ),
]




# Setup
setup(
    name='pyrothermel',
    version='0.0.5',
    author='Johnathan Tenny',
    author_email='jt893@nau.edu',
    description='Python bindings and API for Behave extended Rothermel fire models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/j-tenny/pyrothermel',
    license='MIT',
    packages=find_packages(),
    ext_modules=ext_modules,
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C++',
        'Operating System :: OS Independent',
    ],
    cmdclass={'build_ext': build_ext},
    zip_safe=False,
)