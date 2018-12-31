# Cython_IPEM
## Auditory Model
Please visit [HERE](https://github.com/IPEM/IPEMToolbox) to get the latest IPEM Toolbox
## Build
Currently Only the following version has been built:
- Python2.7 64bit

If the version of python you are using is not listed above, please build your own extension by the following steps:
### Find proper compiler
https://github.com/cython/cython/wiki/CythonExtensionsOnWindows

### Compile to build
```
python setup.py build_ext --inplace --compiler=msvc
```
python2.7 can use msvc.

Read More:
https://docs.python.org/2/install/index.html#using-non-microsoft-compilers-on-windows

## Install
Install the built extension by the following command:

```
python setup.py install
```
Read More:
https://github.com/cython/cython/wiki/CythonExtensionsOnWindows