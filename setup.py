import setuptools

setuptools.setup(
    name='atypon.consulate',
    version='2.0.0',
    description='A Client library and command line application for the Consul',
    maintainer='Alaa Humaidat',
    maintainer_email='ahumaidat@atypon.com',
    url='https://consulate.readthedocs.org',
    install_requires=['requests>=2.0.0,<3.0.0'],
    extras_require={'unixsocket': ['requests-unixsocket>=0.1.4,<=1.0.0']},
    license='BSD',
    package_data={'': ['LICENSE', 'README.rst']},
    packages=['consulate', 'consulate.api', 'consulate.models'],
    entry_points=dict(console_scripts=['consulate=consulate.cli:main']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Clustering',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True)
