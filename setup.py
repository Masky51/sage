from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sage/__init__.py
from sage import __version__ as version

setup(
	name="sage",
	version=version,
	description="Sage operation",
	author="mohammed shariq",
	author_email="mohammed.shariq@metadottech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
