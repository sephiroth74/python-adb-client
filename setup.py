import sys
from setuptools import find_namespace_packages, setup

assert sys.version_info >= (3, 8, 0), "STB Utilities requires Python 3.8+"

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("src/__version__.py") as fh:
    version = fh.read()

setup(
    name="adb-client",
    version=version,
    scripts=["src/adb"],
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
    packages=find_namespace_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
