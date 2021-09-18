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
