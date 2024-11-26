# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.



# Задача "Найдёт везде":

# Напишите класс WordsFinder, объекты которого создаются следующим образом:

# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).

class WordsFinder:
    def __init__(self,*file_names):
        self.file_names=file_names 

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i,'r',encoding='utf-8') as f:
                line = f.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(j,'' )
                words = line.split()
                all_words[i] = words
        return all_words
    
    def find(self, word):
        resalt = {}
        for name, words in self.get_all_words().items():
            if  word.lower() in words:
                resalt[name] = words.index(word.lower()) + 1
        return resalt
   
    def count(self, word):
        resalt= {}
        for name, words in self.get_all_words().items():
            if  word.lower() in words:
                resalt[name] = words.count(word.lower())
        return resalt        




# Пример результата выполнения программы:

# Представим, что файл 'test_file.txt' содержит следующий текст:

# It's a text for task Найти везде,

# Используйте его для самопроверки.

# Успехов в решении задачи!

# text text text



# Пример выполнения программы:

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего



# Вывод на консоль:

# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}

# {'test_file.txt': 3}

# {'test_file.txt': 4}



# Запустите этот код с другими примерами предложенными здесь.

# Если решение верное, то результаты должны совпадать с предложенными.



# Примечания:

# Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
# Решайте задачу последовательно - написав один метод, проверьте результаты его работы.


