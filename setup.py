from setuptools import setup
from setuptools.extension import Extension
import os


def list_all_src_files(foldername):
    """
    find all source files(.c) in 'foldername'
    and list their directories
    """
    sourcefiles = ["mycodecpy.pyx"]
    for r, d, f in os.walk(foldername):
        for file in f:
            if ".c" in file and ".cpp" not in file:
                sourcefiles.append(os.path.join(r, file))
    return sourcefiles


def list_all_header_folders(folder):
    """
    find all folders containing header files(.h)
    and list their directories
    """
    dirs = []
    for r, d, f in os.walk(folder):
        for file in f:
            if ".h" in file:
                if not os.path.join(r) in dirs:
                    dirs.append(os.path.join(r))
    return dirs


# path of Auditory Model Folder
AuditoryModel = 'AuditoryModel'

setup(
    name="mycodecpy",
    version="1.0.1",
    description="mycodecpy",
    url='https://github.com/IPEM/IPEMToolbox/tree/master/AuditoryModel/src',
    setup_requires=[
        'setuptools >= 18.0',
        'Cython',
    ],
    ext_modules=[
     Extension("mycodecpy",
               sources=list_all_src_files(AuditoryModel),
               include_dirs=list_all_header_folders(AuditoryModel),
               )
    ],
    # required to run IPEM.py
    install_requires=[
        'brian',
        'scipy',
        'numpy',
        'sympy',
    ]
)
# https://stackoverflow.com/questions/43163315/how-to-include-header-file-in-cython-correctly-setup-py