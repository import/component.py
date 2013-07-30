try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='component',
    author='Daniel Chatfield',
    author_email='chatfielddaniel@gmail.com',
    version='0.0.1',
    url='http://github.com/import/component',
    py_modules=['component'],
    description='A python library that makes component(1) play nicely with python.',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)