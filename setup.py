import os
from setuptools import setup

with open('VERSION', 'r') as f:
    VERSION = f.readline().strip()

# Utility function to read the README file.  Used for the long_description.
# It's nice, because now 1) we have a top level README file and 2) it's easier
# to type in the README file than to put a raw string in below.
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name="ceilometer.publisher.vaultaire",
    version=VERSION,
    description="A publisher plugin for Ceilometer that outputs to Vaultaire",
    author="Barney Desmond",
    author_email="engineering@anchor.net.au",
    url="https://github.com/anchor/FIXME",
    zip_safe=False,
    packages=[
        "ceilometer", # Does anyone know what this means?
    ],
    long_description=read("README"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
    entry_points = {
        "ceilometer.publisher": [
            "vaultaire = ceilometer.publisher.vaultaire:VaultairePublisher",
        ],
    },
)