from setuptools import setup, find_packages
import os

RAPHAEL_VERSION = '1.4.3'
version = '1.4.3.1'
# Name version after RAPHAEL_VERSION + .suffix


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '********\n')

setup(
    name='hurry.raphael',
    version=version,
    description="hurry.resource style resources for Raphael.",
    url = "http://github.com/jmichiel/hurry.raphael",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Jeroen Michiel',
    author_email='jmichiel@yahoo.com',
    packages=find_packages('src'),
    namespace_packages=['hurry'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'hurry.resource > 0.2',
        ],
    entry_points={
        'console_scripts': [
            'raphaelprepare = hurry.raphael.prepare:main',
            ],
        'zest.releaser.prereleaser.middle': [
            'prepare = hurry.raphael.prepare:entrypoint',
            ],
        # ALSO grab hurry.raphael in the separate tag checkout...
        'zest.releaser.releaser.middle': [
            'prepare = hurry.raphael.prepare:entrypoint',
            ],
        },
    extras_require={
        'zopesupport': ['hurry.zoperesource'],
        },
    )
