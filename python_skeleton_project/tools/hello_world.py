import sys
from argparse import ArgumentParser

from python_skeleton_project import greet_world


def get_clargs():
    parser = ArgumentParser()
    parser.add_argument("-d", "--descriptor", help="Descriptor of world to greet.")
    return parser.parse_args()


def main():
    args = get_clargs()
    sys.exit(greet_world(args.descriptor))
