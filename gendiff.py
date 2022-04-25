import argparse
from email import parser
parser = argparse.ArgumentParser(prog='Compares two configuration files ans shows a difference.')
parser.add_argument("first_file", type=str, help="first file")
parser.add_argument("second_file", type=str, help="second file")
#parser.add_argument(firs_file)