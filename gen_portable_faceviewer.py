import argparse

def insert_binary_file_here(current_line, out, filename):
    with open(filename, "rb") as toinsert:
        left = current_line.split("/*")[0]
        right = current_line.split("*/")[1]

        first_byte = hex(toinsert.read(1)[0])
        out.write(left + f"{first_byte}")
        while (current_byte := toinsert.read(1)):
            as_string = hex(current_byte[0])
            out.write(f", {as_string}")
        out.write(right)
    toinsert.close()

    return

def insert_plaintext_file_here(current_line, out, filename):
    with open(filename) as toinsert:
        left = current_line.split("/*")[0]
        right = '`' + current_line.split("*/")[1]

        # beginning of previous string
        out.write(left + '`')
        for towrite in toinsert:
            out.write(towrite)
        # end of previous string
        out.write(right)
    return

def main():
    parser = argparse.ArgumentParser(prog='gen_portable_faceviewer', description='generate a website which has all the relevant data included to display a face scan')
    parser.add_argument('-t')
    parser.add_argument('-o')
    parser.add_argument('filenames', nargs='*')

    args = parser.parse_args()
    print(args.filenames, args.t)

    out = open(args.o, "wt")

    with open(args.t) as template:
        for line in template:
            was_replaced = False
            for filename in args.filenames:
                string_to_replace = '/* ' + filename + ' here */'
                if string_to_replace in line:
                    was_replaced = True
                    # if current line contains a file to be replaced
                    if '.jpg' in filename \
                        or '.jpeg' in filename \
                        or '.png' in filename:
                        print(f"Replacing : {string_to_replace}, with contents of file : {filename} (binary)")
                        insert_binary_file_here(line, out, filename)
                    else:
                        print(f"Replacing : {string_to_replace}, with contents of file : {filename} (plain text)")
                        insert_plaintext_file_here(line, out, filename)
            if not was_replaced:
                out.write(line)
    
    out.close()


if __name__ == "__main__":
    main()
