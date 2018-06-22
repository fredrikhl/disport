#!/usr/bin/env python
# coding: utf-8
import io
import setuptools

modules = ['disport']


def get_requirements(filename):
    """ Read requirements from file. """
    with io.open(filename, mode='rt', encoding='utf-8') as f:
        for line in f:
            requirement = line.partition('#')[0].strip()
            if not requirement:
                continue
            yield requirement


def get_textfile(filename):
    """ Get contents from a text file. """
    with io.open(filename, mode='rt', encoding='utf-8') as f:
        return f.read().lstrip()


def run_setup():
    setup_requirements = ['setuptools_scm']
    install_requirements = list(get_requirements('requirements.txt'))

    setuptools.setup(
        name='disport',
        description='Import and disassemble code',
        long_description=get_textfile('README.md'),
        license='MIT',
        author='fredrikhl',
        # author_email='todo@example.org',
        # TODO: url='https://github.com/fredrikhl/disport',
        use_scm_version=False,
        py_modules=modules,
        setup_requires=setup_requirements,
        install_requires=install_requirements,
        entry_points={
            'console_scripts': [
                'disport = disport:main',
            ],
        }
    )


if __name__ == '__main__':
    run_setup()
