from setuptools import setup

setup(
    name='serp',
    version="1.0.1",
    url='https://github.com/shifter-io/python-serp-sdk',
    description='Shifter’s SERP Python SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Shifter',
    author_email='office@shifter.io',
    maintainer='shifter',
    maintainer_email='office@shifter.io',
    license='MIT',
    packages=['serp'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
)