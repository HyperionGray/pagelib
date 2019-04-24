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
                'Development Status :: 0.0.1 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.2',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'Topic :: Software Development :: Libraries',
                ],
    install_requires=[
        'gensim',
        'morfessor',
        'numpy',
        'paramiko',
        'parsel',
        'polyglot',
        'pycld2',
        'pyicu',
        'selectolax',
        'six',
    ],
    packages=setuptools.find_packages(),
)
