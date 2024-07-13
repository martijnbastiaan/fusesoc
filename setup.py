# Copyright FuseSoC contributors
# Licensed under the 2-Clause BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-2-Clause

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

import time

now = int(time.time())

setup(
    name="fusesoc",
    packages=find_packages(where="."),
    package_dir={"": "."},
    version=f"2.3dev{now}",
    author="Olof Kindgren",
    author_email="olof.kindgren@gmail.com",
    description=(
        "FuseSoC is a package manager and a set of build tools for HDL "
        "(Hardware Description Language) code."
    ),
    license="BSD-2-Clause",
    url="https://github.com/olofk/fusesoc",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["fusesoc = fusesoc.main:main"]},

    # Supported Python versions: 3.6+
    python_requires=">=3.6",
)
