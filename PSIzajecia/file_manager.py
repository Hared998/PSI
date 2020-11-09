class FileManager:
    file_name = ""

    def __init__(self,fname):
        self.file_name = fname

    def update_file(self, data_text):
        file_object = open(self.file_name, 'a')
        file_object.write(data_text)
        file_object.close()
    def read_file(self):
        file_object = open(self.file_name, 'r')
        return file_object.readlines()