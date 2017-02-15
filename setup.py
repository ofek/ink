from setuptools import find_packages, setup

setup(
    name='ink',
    version='0.0.1',
    description='Digital signatures made easy.',
    long_description=open('README.rst', 'r').read(),
    author='Ofek Lev',
    author_email='ofekmeister@gmail.com',
    url='https://github.com/ofek/privy',
    license='MIT',

    keywords=(
        'digital signatures',
        'signing',
        'ed25519',
        'key storage',
    ),

    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),

    install_requires=['click', 'cryptography', 'pynacl'],
    tests_require=['pytest'],

    packages=find_packages(),
)
