import json
import hashlib


class CountryIterate:
    # при создании экз.класса открывается json, записывается в атрибут и создается счетчик индексов
    def __init__(self, data=None, count=-1):
        with open('countries.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.count = count

    def __iter__(self):
        return self

    # на каждой итерации открывается файл и в него дописывается строка с названием и ссылкой на вики
    def __next__(self):
        self.count += 1
        if self.count == len(self.data) - 1:
            raise StopIteration
        link_name = f"{self.data[self.count]['name']['common']}".replace(' ', '_')
        line = f"{self.data[self.count]['name']['common']}, https://en.wikipedia.org/wiki/{link_name}\n"
        print(line.strip('\n'))
        with open('wiki.txt', 'a', encoding='utf-8')as file:
            file.write(line)


# возвращает хэш очередной строки из файла
def generator_hash(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line_hash = hashlib.md5(line.encode())
            yield line_hash.hexdigest()


if __name__ == '__main__':
    iter = CountryIterate()
    iter.__next__()
    iter.__next__()
    iter.__next__()
    iter.__next__()

    for line_hash in generator_hash('wiki.txt'):
        print(line_hash)

#Альтернативное решение

# class CountryLinks:
#
# 	WIKI_URL = 'https://en.wikipedia.org/wiki/'
#
# 	def __init__(self, countrys_file_path: str):
# 		with open(countrys_file_path) as file:
# 			countries_data = json.load(file)
# 			country_names = (country['name']['common'] for country in countries_data)  # генератор возвращающий
# 			                                                                           # имена стран
# 			self.country_names_iter = iter(country_names)  # итератор по именам стран
#
# 	def __iter__(self):
# 		return self
#
# 	def make_link(self, country_name: str):
# 		"""Метод возвращает ссылку на страну"""
#
# 		country_name = country_name.replace(' ', '_')
# 		return f'{self.WIKI_URL}{country_name}'
#
# 	def __next__(self):
# 		country_name = next(self.country_names_iter)  # получаем имя страны.
# 		                                              # Если имена закончатся выбросится StopIteration
# 		return f'{country_name} - {self.make_link(country_name)}'
#
#
# def get_hash(path: str):
# 	with open(path, 'rb') as file:
# 		for line in file:
# 			yield hashlib.md5(line).hexdigest()
#
#
# if __name__ == '__main__':
# 	with open('country_names.txt', 'w') as country_names_file:
# 		for country_link in CountryLinks('countries.json'):  # итерируемя по ссылкам
# 			country_names_file.write(f'{country_link}\n')  # и пишем их в файл
#
# 	for hash_string in get_hash('country_names.txt'):
# 		print(hash_string)