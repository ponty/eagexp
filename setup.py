import os.path

from setuptools import setup


NAME = "eagexp"
URL = "https://github.com/ponty/eagexp"
DESCRIPTION = "export eagle schematic or board to image or partlist"
PACKAGES = [
    NAME,
    NAME + ".examples",
]

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__

# extra = {}
# if sys.version_info >= (3,):
#     extra["use_2to3"] = True

classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

install_requires = open("requirements.txt").read().split("\n")

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.rst", "r").read(),
    classifiers=classifiers,
    keywords="eagle",
    author="ponty",
    # author_email='',
    url=URL,
    license="BSD",
    packages=PACKAGES,
    include_package_data=True,
    #     test_suite='nose.collector',
    zip_safe=False,
    install_requires=install_requires,
    # **extra
)
