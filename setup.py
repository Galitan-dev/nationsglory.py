from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='nations-glory',
    packages=find_packages(include=['nations_glory']),
    version='1.0.0',
    description='A python library that collects information from nationsglory.fr, just for you.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='galitan-dev',
    license='MIT',
    install_requires=['requests==2.22.0', 'html-to-json'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)