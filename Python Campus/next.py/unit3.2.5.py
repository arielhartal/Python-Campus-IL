def read_file(file_name):
    try:
        file = open(file_name, "r")
        print("__CONTENT_START__" + "\n" + file.read() + "\n" + "__CONTENT_END__")
        return ""
    except FileNotFoundError:
        print("__CONTENT_START__" + "\n" + "__NO_SUCH_FILE__" + "\n" + "__CONTENT_END__")
        return ""



print(read_file("c:\\files\\names.txt"))