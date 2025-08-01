import os
import os.path
from setuptools import setup
from glob import glob

here = os.path.abspath(os.path.dirname(__file__))
packages = []
for d, _, _ in os.walk(os.path.join(here, 'ImageMetaTag')):
    if os.path.exists(os.path.join(d, '__init__.py')):
        packages.append(d[len(here)+1:].replace(os.path.sep, '.'))

setup_args = dict(
    name = 'ImageMetaTag',
    # see release_process for details on incrementing the version
    version = '0.8.2',
    description = 'Image metadata tagging, database and presentation',
    license = 'BSD3',
    author = 'Melissa Brooks',
    url = 'https://github.com/MetOffice/image-meta-tag',
    packages = packages,
    test_suite = 'python test.py',
    classifiers = ['Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10',
                  ],
    package_data = {'ImageMetaTag': ['javascript/*']},
    scripts = ['bin/rm_imt_images'],
)

if __name__ == '__main__':
    setup(**setup_args)
