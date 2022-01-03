from setuptools import setup, find_packages
import codecs
import os


def read(fname):
    """
    Utility function to read the README file.
    Used for the long_description. It's nice, because now (1) we have a top level
    README file and (2) it's easier to type in the README file than to put a raw
    string in below ...
    """
    return codecs.open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


setup(
    name='django-cities-legacy',
    version='0.6.2',
    description='Place models and worldwide place data for Django',
    author='Ben Dowling',
    author_email='ben.m.dowling@gmail.com',
    url='https://github.com/walksource/django-cities',
    packages=find_packages(exclude=['example']),
    install_requires=[
        'django-model-utils',
        'six',
        'swapper',
        'tqdm',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    tests_require=[
        'flake8',
        'psycopg2',
        'tox',
    ],
    license="MIT",
    keywords="django cities countries regions postal codes geonames",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
