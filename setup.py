from setuptools import setup
from setuptools.extension import Extension


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
     Extension("mycodecpy", ["mycodecpy.pyx", "cpu.c", "cpupitch.c",
                          "decimation.c", "ecebank.c", "filterbank.c",
                          "Hcmbank.c", "command.c", "filenames.c",
                          "pario.c", "sigio.c", "IPEMAuditoryModel.c", "Audimod.c", "AudiProg.c"])
    ],
)
# brian, scipy, numpy