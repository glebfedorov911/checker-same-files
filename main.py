from difflib import SequenceMatcher

def Plagerisn_cheker(f1, f2):
    with open(f1, errors='ignore') as file1, open(f2, errors='ignore') as file2:
        f1_data = file1.read()
        f2_data = file2.read()
        checker = SequenceMatcher(None, f1_data, f2_data).ratio()
    print(f'Сходство на {checker*100}%')

file1 = input('Путь к первому файлу: ')
file2 = input('Путь ко второму файлу: ')

try:
    Plagerisn_cheker(file1, file2)
except:
    print('Ошибка')

z = input()