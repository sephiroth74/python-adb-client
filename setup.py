"""
rm -fr out build dist src/pythonadb.egg-info
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
"""

import sys
import re
from setuptools import find_namespace_packages, setup

assert sys.version_info >= (3, 8, 0), "STB Utilities requires Python 3.8+"

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSIONFILE = "src/pythonadb/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name="pythonadb",
    version=verstr,
    author="Alessandro Crugnola",
    author_email="alessandro.crugnola@gmail.com",
    description="pure python adb client for mac/win/linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sephiroth74/python-adb-client",
    license="MIT",
    py_modules=[],
    package_dir={"": "src"},
    python_requires=">=3.8",
    packages=find_namespace_packages(where="src", exclude=("tests", "htmlconv")),
    test_suite="nose.collector",
    install_requires=[
        "verboselogs>=1.7",
        "zope.event>=4.5.0",
        "coloredlogs>=15.0",
        "optional.py>=1.1.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
