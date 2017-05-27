from setuptools import setup, find_packages

setup(
    name='sentimental',
    version='0.1.1',
    packages=find_packages(),
    package_data={
        'sentimental': ['word_list/*.csv'],
    },
    install_requires=[],
    author='Alexey Romanov',
    author_email='aromanov@cs.uml.edu',
    description='A simple dictionary-based sentiment analysis system with Russian language support',
    url='https://github.com/text-machine-lab/sentimental',
)
