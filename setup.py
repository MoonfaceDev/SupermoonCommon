from setuptools import setup, find_packages

setup(
    name='supermoon_common',
    version='0.1.0',
    author='Elai Corem',
    description='Shared utilities used across Supermoon services',
    url='https://github.com/MoonfaceDev',
    python_requires='>=3.10, <4',
    packages=find_packages(include=['supermoon_common', 'supermoon_common.*']),
    install_requires=[
        'pydantic~=1.10.2'
    ],
)
