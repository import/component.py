try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='component',
    version='0.0.1',
    license='MIT',
    author='Daniel Chatfield',
    author_email='databrimo758@gmail.com',
    url='http://github.com/import/component',
    py_modules=['component'],
    description='A python library that makes is easy to consume bower '
                'components with python.',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
