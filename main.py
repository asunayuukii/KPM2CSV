import csv
from pathlib import Path

class txt2csv:
    def __init__(self, txt, lines, path,name):
        self.path = path
        self.txt = txt
        self.lines = ''
        self.name = name

    def read(self):
        with open(self.txt) as f:
            self.lines = f.read().splitlines()

    def addcsv(self):
        header = ['name', 'url', 'username', 'password', 'note', 'cardholdername', 'cardnumber', 'cvc', 'expirydate', 'zipcode', 'folder', 'full_name', 'phone_number', 'email', 'adress1', 'adress2', 'city', 'country', 'state']

        with open(self.path + "\\" + self.name, 'w', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            csvline = []

            for x in self.lines:
                if 'Password: ' in x:
                    csvline.append(x.removeprefix('Password: '))
                    writer.writerow(csvline)
                    csvline.clear()
                    csvline.remove

                if 'Website name: ' or 'Website URL: ' or 'Login: ' in x:
                    if 'Website name: ' in x:
                        csvline.append(x.removeprefix('Website name: '))
                    if 'Website URL: ' in x:
                        csvline.append(x.removeprefix('Website URL: '))
                    if 'Login: ' in x:
                        csvline.append(x.removeprefix('Login: '))
    
def validate_txtfile(txt):
    path = Path(txt)

    if path.is_file and txt[-4:] in '.txt': return True
    else: return False

if __name__ == "__main__":
    print('Kaspersky Password Manager Export 2 CSV\n\n')

    txt = input('Please enter Path to TXT File: ')
    txt = txt.replace('"','')

    while(validate_txtfile(txt) == False):
        if txt.lower() == 'exit':
            exit()

        txt = input('Cant find .txt File. Please try again or enter exit to stop: ')
        txt = txt.replace('"','')

    folder = input('Please enter where the .csv should be created [Folder Path]: ')

    while(Path(folder).is_dir == False):
        if folder.lower() == 'exit':
            exit()

        folder = input('Folder not found. Please try again or enter exit to stop: ')

    folder = folder.rstrip('\\')

    name = input('Please enter the Filename [without .csv]: ')

    name = name + '.csv'


    file2csv = txt2csv(txt, '', folder, name)
    file2csv.read()
    file2csv.addcsv()


    print('\n\nfin')
    input()
