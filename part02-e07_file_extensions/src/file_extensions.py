#!/usr/bin/env python3


def file_extensions(filename):
    no_ext_list = []
    ext_dict = {}
    with open(filename, "r") as fp:
        for x in fp:
            if "." in x:
                # Split the file by extension
                split_file = x.split(".")

                # Get the file extension and strip newlines
                dict_key = split_file[-1].strip()
                
                # Get the value and strip newlines
                dict_value = x.strip()
                if dict_key not in ext_dict:
                    ext_dict[dict_key] = [dict_value]
                else:
                    ext_dict[dict_key].append(dict_value)
            else:
                no_ext_list.append(x.strip())

    return (no_ext_list, ext_dict)


def main():
    # l, d = file_extensions(["file1.txt","mydocument.pdf","file2.txt","archive.tar.gz","test"])
    l, d = file_extensions("src/filenames.txt")
    print(f"{len(l)} files with no extension")
    for i in sorted(d.keys()):
        print(f"{i} {len(d[i])}")


if __name__ == "__main__":
    main()