import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="SuperResolution",
    py_modules=["SuperResolution"],
    version="1.0",
    description="",
    author="Devanshu",
    url='https://github.com/7iFinalBoSS/SuperResolutionFast',
    packages=find_packages(include=['SuperResolution']),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
)