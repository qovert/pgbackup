from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to S3.',
    long_description=readme,
    author='Brian Harkreader',
    author_email='git@qov.io',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'':'src'}
)
