from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    packages=find_packages(),
    description='A sample test package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ziloughm',
    author_email=' ziloughm@42.fr',
    url=': https://github.com/ziloughm/ft_package',
    classifiers=[],
    license='MIT',
    python_requires='>=3.10',
)