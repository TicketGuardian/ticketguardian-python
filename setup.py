from setuptools import setup, find_packages
from tg_sdk import __version__

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='tg_sdk',
    packages=find_packages(exclude=['test*']),
    version=__version__,
    description='A python SDK for interacting with the TicketGuardian API',
    author='TicketGuardian',
    author_email='developers@ticketguardian.com',
    url='https://github.com/TicketGuardian/ticketguardian-python',
    keywords=['sdk', 'TicketGuardian', 'python'],
    install_requires=requirements,
    classifiers=[],
)
