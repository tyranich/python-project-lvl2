from gendiff.cli import parser_args
from gendiff.tree import generate_diff


def main():
    args = parser_args()
    formater = args.format

    if formater:
        print(generate_diff(args.first_file, args.second_file, formater))
    else:
        print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
