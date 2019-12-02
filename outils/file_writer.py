class FileWriter:

    def write_to_file(self, string: str, filename: str):
        f = open(filename, "w+")
        f.write(string)
        f.close()
