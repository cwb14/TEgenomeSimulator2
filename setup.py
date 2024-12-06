#! /usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='TEgenomeSimulator',
    version='0.1.0',
    description='A tool to simulate TE mutation and insertion into a random-synthesised or user-provided genome.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    author='Ting-Hsuan Chen', 
    author_email='Ting-Hsuan.Chen@plantandfood.co.nz',
    url='https://github.com/PlantandFoodResearch/TEgenomeSimulator',
    license='MIT',
    packages=find_packages(where='TEgenomeSimulator'),
    package_dir={'': 'TEgenomeSimulator'},  # Specify the location of the package
    install_requires=[
        'numpy',
        'pandas',
        'biopython',
        'pyyaml'
        ],
    entry_points={  # If you want to create command-line scripts
        'console_scripts': [
            'TEgenomeSimulator = TEgenomeSimulator.TEgenomeSimulator:main',  # The entry point to the main script
            ],
        },
    keywords=[
        'biology',
        'genomics',
        'bioinformatics',
        'transposon',
        'transposable element',
        'simulation'
        ],
    classifiers=[  # Optional: Help people find your project
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Operating System :: Unix'
        ],
    python_requires='>=3.9',
)