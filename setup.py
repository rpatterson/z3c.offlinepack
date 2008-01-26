from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='z3c.offlinepack',
      version=version,
      description="Pack ZODB databases without running Zope or ZEO",
      long_description=open(os.path.join(os.path.dirname(__file__),
                                         'README.txt')).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Ross Patterson',
      author_email='me@rpatterson.net',
      url='http://pypi.python.org/pypi/z3c.offlinepack',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['z3c'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'ZODB3', 'zope.dottedname'
      ],
      extras_require=dict(test=['zc.buildout', 'zc.recipe.egg']),
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      offlinepack = z3c.offlinepack:main
      """,
      )
