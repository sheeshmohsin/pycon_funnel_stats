#!/usr/bin/env python

"""Pycon Funnel App"""

from setuptools import find_packages, setup

dependencies = ['setuptools', 'flask', 'subprocess', 'jinja2', 'urllib2', 'BeautifulSoup4',]

setup(name = 'Pycon_Funnel_App',
    version = '0.1',
    description = "An app to see Pycon India 2013 Statistics.",
    platforms = ["Linux"],
    author = "Shantanu Sarkar, Shalini Roy, Sheesh Mohsin",
    author_email = "shantanusarkar.me@gmail.com",
    url = "http://dgplug.org/summertraining/2013/",
    license = "MIT",
    install_requires=[
        "setuptools",
        "flask",
        "subprocess",
        "jinja2",
        "urllib2",
        "BeautifulSoup4",
        "pyparsing",
    ],
    include_package_data=True,
    scripts = ['project1'],
    dependency_links=[
        "https://pypi.python.org/packages/source/F/Flask-Admin/Flask-Admin-1.0.7.tar.gz",
        "https://pypi.python.org/packages/source/s/subprocess.run/subprocess.run-0.0.8.tar.gz",
        "https://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.7.1.tar.gz",
        "https://pypi.python.org/packages/source/h/httpsproxy_urllib2/httpsproxy_urllib2-1.0.tar.gz",
        "https://pypi.python.org/packages/source/b/beautifulsoup4/beautifulsoup4-4.3.2.tar.gz",
        "https://pypi.python.org/pypi/pyparsing/2.0.1#downloads",
    ],
    packages = find_packages()
    )
