from gendiff.cli import parse_args
from gendiff.tree import generate_diff


def main():
    args = parse_args()
    formater = args.format
    generate_diff(args.first_file, args.second_file, formater=formater)


if __name__ == "__main__":
    main()
