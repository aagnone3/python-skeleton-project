from os import path
from glob import glob
from setuptools import setup, find_packages
from configparser import ConfigParser


def get_package_info():
    cfg = ConfigParser()
    cfg.read("setup.cfg")
    return cfg["package_info"]


def get_requirements():
    requirements_fn = path.join(path.dirname(__file__), 'requirements.txt')
    with open(requirements_fn, 'r') as fh:
        requirements = [str(x).strip() for x in fh.readlines()]
    return requirements


def get_version(module_name):
    version_fn = path.join(module_name, "version.py")
    with open(version_fn) as fp:
        version = float(fp.readlines()[0].strip().split('=')[1].replace(' ', ''))
    return version


def get_data_files():
    data_files = ['README.rst']
    if path.isdir("conf"):
        data_files.append([
            path.join("conf", fn)
            for fn in glob(path.join("conf", "*"))
        ])
    return data_files


package_info = get_package_info()
module_name = package_info["module_name"]

setup(
    name=package_info["friendly_name"],
    version=get_version(package_info["module_name"]),
    description=package_info["description"],
    long_description=package_info.get("long_description", package_info["description"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering"
    ],
    url=package_info["url"],
    author=package_info["author"],
    author_email=package_info["author_email"],
    packages=find_packages(exclude=['*.test', 'test']),
    install_requires=get_requirements(),
    zip_safe=False,
    data_files=[('share/{}'.format(module_name), get_data_files())]
)
