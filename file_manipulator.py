import sys


def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print_usage()

    mode = args[0]
    input_path = args[1]

    if mode == "reverse":
        if len(args) != 3:
            print_usage()
            return 1
        output_path = args[2]
        return mode_reverse(input_path, output_path)

    elif mode == "copy":
        if len(args) != 3:
            print_usage()
            return 1
        output_path = args[2]
        return mode_copy(input_path, output_path)

    elif mode == "duplicate-contents":
        if len(args) != 3:
            print_usage()
            return 1
        n = args[2]
        if not n.isdigit():
            print_usage()
            return 1
        return mode_duplicate(input_path, int(n))

    elif mode == "replace-string":
        if len(args) != 4:
            print_usage()
            return 1
        needle = args[2]
        new_string = args[3]
        return mode_replace(input_path, needle, new_string)

    else:
        print_usage()
        return 1


def print_usage():
    print("Usage: python3 file_manipulataor.py reverse <input_path> <output_path>")
    print("       python3 file_manipulataor.py copy <input_path> <output_path>")
    print("       python3 file_manipulataor.py duplicate-contents <input_path> <n>")
    print(
        "       python3 file_manipulataor.py replace-string <input_path> <needle> <new_string>"
    )


def mode_reverse(input_path, output_path):
    with open(input_path) as f:
        # read file and remove automatic newline at end of the file
        contents = f.read().rstrip()
        reversed_content = contents[::-1]
    with open(output_path, "w") as f:
        f.write(reversed_content)
    return 0


def mode_copy(input_path, output_path):
    with open(input_path) as f:
        contents = f.read().rstrip()
    with open(output_path, "w") as f:
        f.write(contents)
    return 0


def mode_duplicate(input_path, n):
    with open(input_path, "r+") as f:
        contents = f.read()
        f.write(contents * n)
    return 0


def mode_replace(input_path, needle, new_string):
    with open(input_path, "r") as f:
        contents = f.read()
        replace_contents = contents.replace(needle, new_string)
    with open(input_path, "w") as f:
        f.write(replace_contents)
    return 0


if __name__ == "__main__":
    main()
