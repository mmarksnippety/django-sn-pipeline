from setuptools import setup

setup(
    name='sn-django-pipeline',
    version='0.1',
    description='Django Pipeline Sassc compiler',
    # url='http://github.com/storborg/funniest',
    author='Marcin Markiewicz',
    author_email='marcin@snippety.pl',
    license='MIT',
    packages=['sn-django-pipeline'],
    install_requires=open('requirements.txt').read(),
    zip_safe=False
)
