#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test
    
setup(
    name='paypal_date',
    version='0.1',
    author='Chris Kelly',
    author_email='chris@ckely.net',
    description='calculate next paypal date for monthly recurring',
    url='https://github.com/ckelly/paypal-date',
    zip_safe=False,
    install_requires=[
        'python-dateutil',
    ],
    packages=find_packages(),
    test_suite = 'test.test_paypal_date',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)