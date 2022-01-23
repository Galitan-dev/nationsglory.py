from setuptools import find_packages, setup

setup(
    name='nations-glory',
    packages=find_packages(include=['nations_glory']),
    version='0.1.0',
    description='A nationsglory.fr Web Scrapper',
    author='galitan-dev',
    license='MIT',
    install_requires=['requests==2.22.0', 'html-to-json'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)