from file_manager import FileManager

plik = FileManager('plik.txt')
plik.update_file("Hello there!")
print(plik.read_file())
