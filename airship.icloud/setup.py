from setuptools import setup

setup(
    name='airship-icloud',
    version='1.2.2',

    description='iCloud plugin for Airship',

    url='https://github.com/constancebello/airship',

    author='Constance Bello',
    author_email='me@constancebello.dev',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'Topic :: Internet',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='cloud games',

    packages=['airship'],

    install_requires=['airship']
)
