
def get_txt(filename):
    content = ''
    with open(filename, 'r') as file:
        content = file.read()
    return content


def split(str):
    return str.split


class txt_file:
    def __init__(self, filename):
        try:
            with open(filename, 'r') as file:
            self.content = file.read()
        except FileNotFoundError:
            print("Невозможно открыть файл")
    def get_content(self):
        return self.content
   
