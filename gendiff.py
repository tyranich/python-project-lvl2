import argparse
parser = argparse.ArgumentParser(description='Compares two configuration files ans shows a difference.')
parser.add_argument("first_file")
parser.add_argument("second_file")
args = parser.parse_args()
#parser.add_argument(firs_file)