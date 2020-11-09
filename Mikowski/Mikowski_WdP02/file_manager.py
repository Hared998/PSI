class FileManager(file_name):
    def read_file(self):
        read= open('file_name.txt','r',encoding='utf-8')
        file= read.read()
        print(file)
        read.close()

    def update_file(self,text_data):
        update = open('self.txt','w', encoding='utf-8')
        update.write(text_data)
        update.close()

