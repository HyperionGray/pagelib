import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name='pagelib',
    version='0.0.1',
    author='Luke Maxwell',
    author_email='support@hyperiongray.com',
    description='Object-oriented html pages',
    long_description=long_description,
    classifiers=[
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: 3.9',
                'Programming Language :: Python :: 3.10',
                'Programming Language :: Python :: 3.11',
                'Programming Language :: Python :: 3.12',
                'Topic :: Software Development :: Libraries',
                ],
    install_requires=[
        'morfessor',
        'numpy',
        'parsel',
        'polyglot',
        'pycld2',
        'pyicu',
        'selectolax',
        'six',
    ],
    packages=setuptools.find_packages(),
)
