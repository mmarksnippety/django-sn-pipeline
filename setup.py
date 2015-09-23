from setuptools import setup, find_packages

setup(
    name='django-sn-pipeline',
    version='0.1',
    description='Django Pipeline Sassc compiler',
    # url='http://github.com/storborg/funniest',
    author='Marcin Markiewicz',
    author_email='marcin@snippety.pl',
    license='MIT',
    packages=find_packages(include=('django-sn-pipeline*', )),
    install_requires=open('requirements.txt').read(),
    zip_safe=False
)
