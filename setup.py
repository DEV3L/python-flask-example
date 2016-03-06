import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


setup(name='DEV3L-Flask',
      version='1.0',
      description='DEV3L Python Flask OpenShift App',
      author='Justin Beall',
      author_email='jus.beall@gmail.com',
      url='https://softwaredev3loper.wordpress.com/',
      install_requires=[
          'Flask==0.10.1',
          'MarkupSafe==0.23',
          'pytest==2.9.0'],
      )


class PyTest(TestCommand):
    # http://pytest.org/latest/goodpractises.html?highlight=setuptools#integration-with-setuptools-test-commands
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)
