"""
    Zinc Search engine API

    Zinc Search engine API documents https://docs.zincsearch.com  # noqa: E501

    The version of the OpenAPI document: 0.3.3
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

NAME = "zincsearch-sdk"
VERSION = "0.3.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Zinc Search engine API",
    author="Zinc Search",
    author_email="team@openapitools.org",
    url="https://github.com/zinclabs/sdk-python-zincsearch",
    keywords=["OpenAPI", "OpenAPI-Generator", "Zinc Search engine API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["zinc", "zincsearch"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description=long_description +
    """\
    Zinc Search engine API documents https://docs.zincsearch.com  # noqa: E501
    """
)
