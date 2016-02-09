from setuptools import setup
from setuptools import find_packages

setup(
    name='FakeDataCRUDService',
    version='0.1.0',
    author='Guido Barbaglia',
    author_email='guido.barbaglia@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    description='Simple CRUD service for fake data.',
    install_requires=[
        'watchdog', 'flask', 'gunicorn', 'pymongo'
    ],
    url='http://pypi.python.org/pypi/FakeDataCRUDService/'
)