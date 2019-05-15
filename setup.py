# -*- coding: utf-8 -*-
#
from setuptools import setup, find_packages
import os
import codecs

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "vandermonde", "__about__.py"), "rb") as f:
    exec(f.read(), about)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding="utf-8").read()


setup(
    name="vandermonde",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=find_packages(),
    description=(u"Vandermonde matrix tools"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/nschloe/vandermonde",
    license=about["__license__"],
    platforms="any",
    install_requires=["numpy"],
    classifiers=[
        about["__status__"],
        about["__license__"],
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    scripts=[],
)
