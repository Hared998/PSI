class FileManager:
    file_name =""
    def __init__(self,name):
        self.file_name=name
    def read_file(self):
        read= open(self.file_name,'r',encoding='utf-8')
        file= read.read()
        print(file)
        read.close()

    def update_file(self,data_text):
        update = open(self.file_name,'w', encoding='utf-8')
        update.write(data_text)
        update.close()

