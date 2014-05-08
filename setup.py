"""
PyPages
-------

Do pagination in python like a charm.

Links
`````

* `documentation <https://github.com/fengsp/pypages>`_
* `development version
  <http://github.com/fengsp/pypages/zipball/master#egg=pypages-dev>`_

"""
from setuptools import setup


setup(
    name='PyPages',
    version='0.1',
    url='https://github.com/fengsp/pypages',
    license='BSD',
    author='Shipeng Feng',
    author_email='fsp261@gmail.com',
    description='Python Pagination for Humans',
    long_description=__doc__,
    py_modules=['pypages'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
