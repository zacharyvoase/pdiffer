from distutils.core import setup

setup(name='pdiffer',
      version='0.0.3',
      description='A Python interface to the PerceptualDiff tool.',
      long_description=open('README.rst').read().decode('utf-8'),
      author='Zachary Voase',
      author_email='z@zacharyvoase.com',
      url='https://github.com/zacharyvoase/pdiffer',
      py_modules=['pdiffer'],
)
