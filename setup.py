import setuptools
from numpy.distutils.core import setup, Extension
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Fortran module
ccflibfort = Extension(name='raccoon.ccflibfort', sources=['raccoon/ccflibfort.f'])

setup(
    name='raccoon',
    version="0.0.1",
    description='Radial velocities and Activity indicators from Cross-COrrelatiON with masks',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/mlafarga/raccoon',
    author="Marina Lafarga Magro",
    author_email="marina.lafarga@gmail.com",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='CCF spectroscopy RV activity',
    # package_dir={'': 'raccoon'},
    # packages=['raccoon'],
    packages=setuptools.find_packages(),
    # python_requires='>=3.6',
    setup_requires=['numpy', 'scipy'],  # need for fortran
    install_requires=['numpy', 'scipy', 'astropy', 'pandas', 'lmfit', 'progress', 'matplotlib'],

    package_data={
        "raccoon": ["data/tellurics/*.dat", "data/mask/*.mas", "data/mask/*.pkl", "data/mask/*.dat", "data/phoenix/*.fits", ],
    },

    # scripts=['scripts/ccf_compute.py', 'scripts/mask_compute.py'],
    entry_points={
        'console_scripts': [
            'raccoonccf=raccoon.scripts.ccfcompute:main',
            'raccoonmask=raccoon.scripts.maskcompute:main',
        ],
    },

    ext_modules=[ccflibfort],
    )