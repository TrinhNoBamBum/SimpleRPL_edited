from distutils.core import setup, Extension
from Cython.Build import cythonize
ext_modules = [
    Extension(
        "RplIcmp",
        sources=["RplIcmp.pyx", "caplib.c", "icmplib.c"],  
        libraries=["cap"], 
        include_dirs=['.'],  
    )
]


setup(
    name="RplIcmp",
    ext_modules=cythonize(ext_modules),
)