import argparse
from gendiff.scripts.parse_data import parser_data

def generate_diff(path1, path2):

    file1, file2 = parser_data(path1, path2)
    if file1 and file2:
        pair_items = [x[0] for x in file1.items() if x in file2.items()]
        pair_keys = [x[0] for x in file1.items() if x[0] in file2.keys()]
        for _ in pair_items:
            pair_keys.remove(_)
        sorted_keys = sorted(set(file1).union(set(file2)))
        finished_list = []
        string_list = ["{"]
        for _2 in sorted_keys:
            if _2 in pair_items:
                finished_list.append((_2, file1.get(_2)))
            elif _2 in pair_keys:
                finished_list.append((_2, file1.get(_2), "-"))
                finished_list.append((_2, file2.get(_2), "+"))
            
            else:
                if file1.get(_2) != None:
                    finished_list.append((_2, file1.get(_2), "-"))
                elif file2.get(_2) != None:
                    finished_list.append((_2, file2.get(_2), "+"))

        for _3 in finished_list:
            if len(_3) == 3:
                concant_str = "{} {}: {}".format(_3[2], _3[0], _3[1])
            else:
                concant_str = "  {}: {}".format(_3[0], _3[1])
            string_list.append(concant_str)

        string_list.append("}")
        return ('\n'.join(string_list))
    else:
        return None
#generate_diff(first_file, second_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compares two configuration files ans shows a difference.')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help='set format of output')
    args = parser.parse_args()

    

    print(generate_diff(args.first_file, args.second_file))
    