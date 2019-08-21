from setuptools import setup, find_packages
from configparser import ConfigParser


conf = ConfigParser()
conf.read(['setup.cfg'])
metadata = dict(conf.items('metadata'))


PACKAGENAME = metadata.get('name', 'packagename')

version = "0.1.dev"

setup(use_scm_version=True)
