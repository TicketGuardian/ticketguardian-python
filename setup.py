from setuptools import setup, find_packages
from tg_sdk import __version__

setup(
    name='tg_sdk',
    packages=find_packages(exclude=['test*']),
    version=__version__,
    description='A python SDK for interacting with the TicketGuardian API',
    author='TicketGuardian',
    author_email='austin@ticketguardian.net',
    url='https://github.com/TicketGuardian/ticketguardian-sdk',
    keywords=['sdk', 'TicketGuardian'],
    classifiers=[],
)
