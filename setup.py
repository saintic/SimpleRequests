#!/usr/bin/env python

from SimpleRequests import __version__, __doc__

try:
    from setuptools import setup
except ImportError:
    print "Install it using your package manager (usually python-setuptools) or via pip (pip install setuptools)."
    exit(127)

setup(
    name = 'SimpleRequests',
    version = __version__,
    description = __doc__,
    author = 'Mr.tao',
    author_email = 'staugur@saintic.com',
    keywords = "requests, url, RESTful API",
    url = 'https://github.com/saintic/SimpleRequests',
    download_url = 'https://github.com/saintic/SimpleRequests/releases/tag/v%s' %__version__,
    license = "MIT",
    py_modules = [ 'SimpleRequests',],
    classifiers = [
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
