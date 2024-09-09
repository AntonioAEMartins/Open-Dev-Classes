from setuptools import setup, find_packages

setup(
    name='dev_aberto_antonioaem',
    version='0.1',
    packages=find_packages(),
    scripts=['scripts/hello.py'],
    author='Antonio E. M. A.',
    author_email='antonioaem@icloud.com',
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    requires=['requests']
)
