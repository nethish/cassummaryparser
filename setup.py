from setuptools import find_packages, setup

setup(
    name='cassummaryparser',
    packages=find_packages(include=['cassummaryparser']),
    version='0.1.0',
    description='Cas summary parser',
    author='Nethish Rajendran',
    author_email='nethish259@gmail.com',
    install_requires=['tabula-py==2.9.0', 'jpype1==1.5.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==8.0.2'],
    test_suite='tests',
)
