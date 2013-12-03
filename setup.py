try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="chrono",
    version="1.0.2",
    description="A (BSD licensed) context manager for timing execution.",
    author='Daniel Lindsley',
    author_email='daniel@toastdriven.com',
    url='https://github.com/toastdriven/chrono',
    license='BSD',
    long_description=open('README.rst', 'r').read(),
    py_modules=[
        'chrono'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
