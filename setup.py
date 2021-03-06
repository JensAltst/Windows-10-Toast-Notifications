
"""The setup script."""

from os import path

from setuptools import find_packages, setup

import versioneer

BASE_DIR = path.abspath(path.dirname(__file__))


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]

with open(path.join(BASE_DIR, "README.md")) as readme_file:
    readme = readme_file.read()

req_files = {
    "requirements": "requirements.txt",
}

requirements = {}
for req, req_file in req_files.items():
    requirements[req] = parse_requirements(req_file)

setup(
    name="win10toast",
    version="0.9.1",
    install_requires=requirements["requirements"],
    packages=["win10toast"],
    license="BSD",
    url="https://github.com/JensAltst/Windows-10-Toast-Notifications",
    download_url = 'https://github.com/JensAltst/Windows-10-Toast-Notifications',
    description=(
        "An easy-to-use Python library for displaying "
        "Windows 10 Toast Notifications"
    ),
    include_package_data=True,
    package_data={
        '': ['*.txt'],
        'win10toast': ['data/*.ico'],
    },
    long_description=readme,
    author="Jithu R Jacob",
    author_email="jithurjacob@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Environment :: Win32 (MS Windows)',
        "License :: OSI Approved :: MIT License",
    ],
)
