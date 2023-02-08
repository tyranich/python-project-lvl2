import argparse


def parse_args():

    description = 'Compares two configuration files ans shows a difference.'
    parser = argparse.ArgumentParser(description)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", type=str,
                        default="stylish", choices=["stylish", "plain", "json"],
                        help='set format of output')
    args = parser.parse_args()
    return args
