from setuptools import setup, find_packages

__version__ = '1.2.0

import os

setup(
    name='ticketguardian-python',
    packages=find_packages(exclude=['test*']),
    version=__version__,
    description='A python SDK for interacting with the TicketGuardian API',
    author='TicketGuardian',
    author_email='developers@protecht.io',
    url='https://github.com/TicketGuardian/ticketguardian-python',
    keywords=['sdk', 'TicketGuardian', 'python'],
    install_requires=['PyJWT==1.5.3', 'simplejson==3.16.0', 'requests[security]'],
    classifiers=[],
)
