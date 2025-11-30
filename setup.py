# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='lesson_package',
    version='1.0.0',
    # packages=[
    #     'lesson_package',
    #     'lesson_package.talk',
    #     'lesson_package.tools',
    #           ],
    packages=find_packages(),
    url='https://github.com/chie-works/python_study/',
    # license='Free',
    license='MIT',
    author='chie',
    author_email='',
    description='sample package'
)