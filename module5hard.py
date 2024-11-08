# Дополнительное практическое задание по модулю: "Классы и объекты."

# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.

# Задание "Свой YouTube":

# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.
# Общее ТЗ:

# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

# Подробное ТЗ:

# Каждый объект класса User должен обладать следующими атрибутами и методами:

# Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:

# Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:


from time import sleep

# Всего будет 3 класса: UrTube, Video, User.
class User:
    def __init__(self, nickname:str, password:int,age:int):
        self.nickname=nickname
        self.password=password
        self.age=age
    def __str__(self):
        return self.nickname 
    
class Video:
    def __init__(self, title:str, duration:int,time_now:int=0,adult_mode:bool=False):
        self.title=title
        self.duration=duration
        self.time_now=time_now
        self.adult_mode=adult_mode


class UrTube:

    def __init__(self,users=[], videos=[], current_user: User=None):
        self.users=users
        self.videos=videos
        self.current_user=current_user

    def log_in(self, nickname:str, password:str ):
        user=self.get_user(nickname)
        if user:
            if hash(password)==user.password:
               self.current_user=user
    def register(self,nickname:str, password:str, age:int):
        if not self.get_user(nickname):
            self.users.append(User(nickname, hash(password),age))
            self.log_in( nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")   
    def log_out(self):
        self .current_user=None
    def add(self,*videos:Video):
        for video in videos:
            if not self.get_video(video.title):
                self.videos.append(video)
    def get_videos (self, search: str):
        found = []
        search=search.lower()
        for title in map(getattr,self.videos,['title']*len(self.videos)):
            if search in title.lower():
                found.append(title)
        return  found       
    def watch_video(self,title:str):
        video=self.get_video(title)
        if video:
            if self.current_user:
                if video.adult_mode and self.current_user.age<18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    while video.time_now<video.duration:
                        sleep(1)
                        video.time_now+=1
                        print(video.time_now,end=' ',flush=True)
                    video.time_now=0
                    print("Конец видео")
            else:
                print("Войдите в аккаунт, чтобы смотреть видео")

    def get_video(self,title:str):
        for video in self.videos:
            if title==video.title:
                return video
            
    def get_user(self,nickname:str):
        for user in self.users:
            if nickname==user.nickname:
                return user
        return None

#  Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)


# Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
# Метод log_out для сброса текущего пользователя на None.
# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:

# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"

# 
# Код для проверки:

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')



# Вывод в консоль:

# ['Лучший язык программирования 2024 года']

# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Войдите в аккаунт, чтобы смотреть видео

# Вам нет 18 лет, пожалуйста покиньте страницу

# 1 2 3 4 5 6 7 8 9 10 Конец видео

# Пользователь vasya_pupkin уже существует

# urban_pythonist





