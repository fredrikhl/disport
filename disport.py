#!/usr/bin/env python
# encoding: utf-8
""" Import and disassemble stuff. """
from __future__ import unicode_literals, print_function, absolute_import

import argparse
import dis
import pkg_resources
import os


NAME = 'disport'


def get_distribution():
    try:
        return pkg_resources.get_distribution(NAME)
    except pkg_resources.DistributionNotFound:
        return pkg_resources.Distribution(
            project_name=NAME,
            version='0.0.0',
            location=os.path.dirname(__file__))


VERSION = get_distribution().version


def get_entry_point(name, entry_point):
    """ Create an EntryPoint object.

    :param str name: the entry point name
    :param str entry_point: an entry-point like import specification
    :return pkg_resources.EntryPoint:
    """
    return pkg_resources.EntryPoint.parse(
        '{name} = {entry_point}'.format(name=name, entry_point=entry_point))


def main(inargs=None):
    distribution = get_distribution()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-v', '--version',
        action='version',
        version="%s v%s" % (distribution.project_name, distribution.version))
    parser.add_argument(
        'entry_point',
        help="a module or entry point to disassemble")
    args = parser.parse_args(inargs)

    entry_point = get_entry_point('object', args.entry_point)
    dis.dis(entry_point.resolve())


if __name__ == '__main__':
    main()
