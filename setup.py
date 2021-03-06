import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'circuits',
    ]

setup(name='TODO Circuits',
      version='0.0',
      description='TODO Backend with Circuits frameworks',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Victor Shyba',
      author_email='victor.shyba@gmail.com',
      url='https://github.com/shyba/todo-circuits',
      keywords='todo backend circuits example',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="tests",
      entry_points="""\
      [paste.app_factory]
      main = todo:main
      """,
      )
