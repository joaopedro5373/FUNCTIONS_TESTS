def read_file_content(path:str)->str:
    with open(path, "r") as f:
        return f.read()