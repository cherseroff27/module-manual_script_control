from setuptools import setup, find_packages

setup(
    name='manual_script_control',
    version='1.0',
    packages=find_packages(),
    install_requires=[
    ],
    description='Модуль, предоставляющий функционал, позволяющий останавливать выполнение скрипта'
                'до решения пользователя продолжить его или завершить вовсе.',
    author='cherseroff',
    author_email='proffitm1nd@gmail.com',
    url='https://github.com/cherseroff27/module-manual_script_control.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)