import os.path

from setuptools import setup

NAME = "eagexp"

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__

URL = "https://github.com/ponty/eagexp"
DESCRIPTION = "export eagle schematic or board to image or partlist"
LONG_DESCRIPTION = """export eagle schematic or board to image or partlist

Documentation: https://github.com/ponty/eagexp/tree/"""
LONG_DESCRIPTION += VERSION

PACKAGES = [
    NAME,
    NAME + ".examples",
]


classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

install_requires = [
    "pillow",
    "PyUserInput",
    "PyScreenshot",
    "easyprocess",
    "pyvirtualdisplay",
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    classifiers=classifiers,
    keywords="eagle",
    author="ponty",
    # author_email='',
    url=URL,
    license="BSD",
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    # package_data={
    #     NAME: ["py.typed"],
    # },
)
