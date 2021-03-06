from django.contrib.auth.models import User
from main.models import Student, Group, PointList, Subject, AdditionalEduResource, ResourceToStudent, Lesson
import random

surnames = ["Архипов", "Гилязов", "Григорьев", "Джунушалиев", "Ефимова", "Закиров", "Индиенкова", "Квасников", "Малышкин", "Минахметова", "Мукиев", "Мустафина", "Орлов", "Палутин", "Подлевских", "Рахимов", "Салахов", "Саттаров", "Соловьев", "Федорова", "Хамидуллина", "Чегодаев", "Чемкин", "Шапиро", "Шарафеев", "Шамарданов", "Аверьянова", "Аскарова", "Бады", "Бекмуратов", "Будников", "Габдрахманов", "Габдрахманов", "Габдуллина", "Галимова", "Гончаренко", "Дмитриев", "Загидуллин ", "Зиятдинов", "Кадыров", "Казаков", "Калашкин", "Мирошихина", "Мухамедьянов", "Мухутдинова", "Пашин", "Петров", "Плотников", "Примаченко ", "Сагдеев", "Сиразетдинов", "Султанов", "Хайбуллин", "Хамидуллин", "Шакирова", "Шамсутдинов", "Широков", "Абдрашитова", "Арифуллин", "Гильмуллина", "Гусинников", "Еланская", "Западнов", "Илалов", "Килин", "Леонтьев", "Мазитов", "Мирзаянова", "Низамов", "Озбаян", "Халиуллин", "Абдуллин", "Апсадиков", "Ахметов", "Блинов", "Богачева", "Богомолов", "Бузанов", "Валинурова", "Вдовинов", "Гариева", "Гатин", "Гатин", "Гимазов", "Гордеев", "Гришин", "Егорова", "Елин", "Зайнуллин", "Закиров", "Исаичкин", "Каримова", "Каримуллин", "Коньков", "Корченов", "Манахов", "Маннапов", "Михеев", "Мокшин", "Мурзина", "Мусин", "Мухаметов", "Пономарев", "Потапов", "Прокопьев", "Рахимов", "Рябов", "Сайдашев", "Сакаев", "Салимов", "Сафин", "Солдатов", "Сюняков", "Фасхутдинов", "Хайруллина", "Хисамов", "Шайдуллин", "Шакуров", "Шигабутдинов", "Шигапов", "Якубенко", "Яманаев", "Азин", "Аликиличова", "Валитов", "Грошев", "Еникеева", "Ермаков", "Ибрагимова", "Калинина", "Мельникова", "Минюков", "Насыбуллин", "Нафиков", "Хакимов", "Хасанов", "Чербаева", "Берендакова", "Бикмуллин", "Железнова", "Загидуллин", "Малов", "Самигуллин", "Хасанов", "Дингизбаев", "Аглеев", "Акрамова", "Ахматянов", "Ахмедов", "Аюбов", "Аюпов", "Барышан", "Гареев ", "Генч", "Валиуллин", "Габдулхаков", "Ганеев", "Давлетьяров", "Дуак", "Едкова", "Казанцев", "Максимов", "Мигранов", "Мустаев", "Мухаметханов", "Мухтаров", "Назипова", "Назиров", "Наумов", "Правдивцев", "Сафиуллин", "Смышляева", "Соцкова", "Сухова", "Сюй", "Санлыер ", "Тимергалиева", "Тресков", "Усмонов", "Ушаков ", "Хабибрахманов", "Хадиев", "Хазиев", "Хайбуллин", "Хамдамов", "Харисов", "Хищенко", "Чеканин  ", "Черемисин", "Шарафутдинов ", "Шумилов", "Халилов ", "Иванов", "Кононов", "Мирончук", "Мырзин", "Хамматова", "Чернигов", "Алиев", "Арсембекова", "Артемьев", "Асанов", "Ахметов", "Беляков", "Билалов", "Валиев", "Гатауллин", "Гильмутдинов", "Грибанова", "Губайдуллин", "Гурьянов", "Давлетгареева", "Данилов", "Замалдинов", "Зиангирова", "Мухитов", "Нуриева", "Рыжаков", "Саетова", "Сайфутдинов", "Семакин", "Сенюкова", "Султанов", "Уезбаев", "Федотова", "Хисматова", "Шагалиев", "Шакирова", "Шафеева", "Эрдоган", "Афанасьев", "Буланова", "Вагманов", "Габдрашитов", "Гиниятуллина", "Губаева", "Королев", "Кубышкин", "Кузьмин", "Лужбин", "Малышев", "Марданов", "Мубараков", "Мялицин", "Сошников", "Строев", "Шабельник", "Шамсиев", "Шуркин", "Гатауллин", "Гиззатуллин", "Гимадиев", "Лаврентьев", "Мамедов", "Михайлова", "Сурков", "Хаялеева", "Шайдуллина", "Шангареев", "Амирханова", "Букарев", "Гатин", "Гильфанов", "Горская", "Константинов", "Кочедыков", "Левченко", "Мусин", "Садыков", "Самигулов ", "Стрелов", "Счастливцев", "Финеев", "Шарифуллин", "Шаронова"]
names = ["Никита", "Тагмир", "Яков", "Александр", "Алина", "Дамир", "Анастасия", "Игорь", "Егор", "Альбина", "Мухаммад", "Анжела", "Дмитрий", "Филипп", "Дмитрий", "Самат", "Даниял", "Артур", "Артем", "Анна", "Нурия", "Дмитрий", "Дмитрий", "Давид", "Равиль", "Фарит", "Александра", "Булат", "Алтея", "Алмаз", "Максим", "Айдар", "Кадыр", "Динара", "Аида", "Богдан", "Михаил ", "Булат", "Ремир", "Самат", "Александр", "Никита", "Екатерина", "Райнур", "Алия", "Руслан", "Максим", "Илья", "Артем", "Радель ", "Динар", "Айнур", "Аскар", "Тимур", "Гульназ ", "Адель", "Роман", "Альсина", "Арслан", "Диана", "Дамир", "Ангелина", "Алексей", "Максим", "Михаил", "Дмитрий", "Камиль", "Регина", "Салават", "Урал", "Булат", "Марат", "Данил", "Марсель", "Ренат", "Виктория", "Даниил", "Владислав", "Алина", "Даниил", "Аделя", "Айнур", "Айрат", "Булат", "Сергей", "Александр", "Анастасия", "Артём", "Руслан", "Ринат", "Данила", "Эвелина", "Амир", "Семён", "Руслан", "Альберт", "Нияз", "Сергей", "Дмитрий", "Алена", "Алмаз", "Аяз", "Степан", "Руслан", "Павел", "Джалил", "Дмитрий", "Булат", "Эльдар", "Наиль", "Марк", "Роман", "Роман", "Азат", "Камилла", "Артур", "Айдар", "Динар", "Марат", "Ринат", "Тимур", "Азат", "Илья ", "Сабина", "Константин", "Виталий", "Сюмбель", "Александр", "Алина", "Александра", "Александра", "Рамиль", "Равиль", "Дамир", "Артем", "Райнур", "Дарья", "Татьяна", "Тимур", "Екатерина", "Линар", "Илья", "Илья", "Расим", "Загир", "Тимур", "Регина", "Алексей", "Джейхун", "Санджар", "Вадим", "Ибрахим", "Эрнест", "Мухсин", "Азат", "Дамир", "Нияз", "Ильдар", "Ала-Еддин", "Ксения", "Матвей", "Аретм", "Эрнест", "Ильяс", "Ильсур", "Ибрагим", "Аделия", "Руслан", "Андрей", "Илья", "Альфред", "Анастасия", "Вероника", "Алина", "Хаосюань", "Дженгизхан Эмиль", "Эльза", "Никита", "Рустамджон", "Кирилл", "Рустем", "Адель", "Булат", "Булат", "Отабек", "Эмиль", "Анна", "Даниил", "Павел", "Карим", "Максим", "Магамед", "Артём", "Кирилл", "Тимофей", "Валерий", "Камила", "Никита", "Эмин", "Талия", "Артем", "Аркадий", "Аскар", "Дмитрий", "Булат", "Азат", "Эдгар", "Ильназ", "Анастасия", "Рамис", "Вадим", "Алсу", "Дмитрий", "Эмиль", "Алия", "Нияз", "Римма", "Сергей", "Алина", "Алмас", "Артем", "Полина", "Азат", "Исабек", "Диана", "Азалия", "Руслан", "Регина", "Дина", "Селим", "Никита", "Камилла", "Альберт", "Динис", "Алсу", "Алсу", "Кирилл", "Родион", "Евгений", "Никита", "Данил", "Амир", "Эмиль", "Максим", "Богдан", "Егор", "Сергей", "Роберт", "Роман", "Ильшат", "Амирхан", "Марсель", "Станислав", "Радимир", "Юлия", "Никита", "Изида", "Эльвина", "Алмаз", "Гульназ", "Богдан", "Камиль", "Данис", "Виктория", "Владислав", "Александр", "Никита", "Искандер", "Данияр", "Айнур", "Алексей", "Михаил", "Егор", "Ильназ", "Алина"]
groups = ["11-801", "11-802", "11-803", "11-804", "11-805", "11-806", "11-807", "11-808", "11-809", "11-810", "11-811"]
subjects = ["Алгебра", "Матанализ", "Дискретная математика", "Информатика", "Алгоритмы и структуры данных", "Введение в проектную деятельность", "Русский язык и культура речи"]
st_groups = ["11-808", "11-809", "11-809", "11-808", "11-811", "11-809", "11-809", "11-810", "11-809", "11-808", "11-808", "11-808", "11-808", "11-809", "11-808", "11-808", "11-808", "11-809", "11-808", "11-809", "11-809", "11-808", "11-810", "11-810", "11-808", "11-808", "11-801", "11-807", "11-810", "11-811", "11-804", "11-809", "11-806", "11-809", "11-808", "11-809", "11-805", "11-811", "11-804", "11-805", "11-809", "11-810", "11-810", "11-810", "11-805", "11-801", "11-811", "11-808", "11-808", "11-808", "11-811", "11-810", "11-810", "11-808", "11-806", "11-810", "11-810", "11-807", "11-804", "11-807", "11-810", "11-801", "11-806", "11-806", "11-801", "11-801", "11-804", "11-807", "11-805", "11-809", "11-808", "11-803", "11-806", "11-803", "11-805", "11-802", "11-802", "11-803", "11-801", "11-802", "11-802", "11-806", "11-802", "11-805", "11-805", "11-802", "11-805", "11-804", "11-807", "11-803", "11-802", "11-802", "11-807", "11-801", "11-805", "11-806", "11-801", "11-803", "11-803", "11-806", "11-802", "11-804", "11-803", "11-807", "11-807", "11-806", "11-802", "11-803", "11-802", "11-802", "11-802", "11-803", "11-807", "11-806", "11-802", "11-802", "11-802", "11-803", "11-805", "11-803", "11-803", "11-802", "11-802", "11-803", "11-810", "11-804", "11-801", "11-804", "11-803", "11-801", "11-806", "11-804", "11-809", "11-802", "11-805", "11-809", "11-805", "11-804", "11-801", "11-808", "11-804", "11-810", "11-805", "11-804", "11-804", "11-808", "11-803", "11-809", "11-811", "11-811", "11-806", "11-811", "11-810", "11-811", "11-806", "11-803", "11-807", "11-808", "11-811", "11-801", "11-811", "11-811", "11-810", "11-809", "11-809", "11-811", "11-806", "11-804", "11-803", "11-806", "11-810", "11-803", "11-802", "11-810", "11-811", "11-811", "11-806", "11-809", "11-811", "11-801", "11-811", "11-806", "11-806", "11-808", "11-811", "11-805", "11-810", "11-811", "11-809", "11-804", "11-801", "11-811", "11-805", "11-809", "11-803", "11-810", "11-810", "11-806", "11-805", "11-804", "11-803", "11-806", "11-808", "11-807", "11-807", "11-807", "11-805", "11-805", "11-803", "11-805", "11-804", "11-801", "11-802", "11-803", "11-802", "11-806", "11-802", "11-801", "11-801", "11-807", "11-811", "11-804", "11-807", "11-811", "11-801", "11-811", "11-806", "11-802", "11-803", "11-811 ", "11-805", "11-805", "11-809", "11-808", "11-807", "11-810", "11-807", "11-801", "11-803", "11-811", "11-811", "11-806", "11-804", "11-805", "11-804", "11-807", "11-811", "11-809", "11-801", "11-807", "11-809", "11-810", "11-807", "11-805", "11-806", "11-806", "11-804", "11-804", "11-802", "11-807", "11-801", "11-805", "11-807", "11-801", "11-810", "11-801", "11-803", "11-804", "11-804", "11-807", "11-807", "11-804", "11-801", "11-801", "11-803"]
ress = ["не использую", "stepik", "youtube", "матпрофи", "гуглю", "javarush", "acmp"]
maxSem = 6

print("started generating groups (группы)")
for gr in groups:
    g = Group(name=gr)
    g.save()
print("groups generated")
print("started generating subjects")
for sb in subjects:
    s = Subject(name=sb)
    s.save()
print("subjects generated")
print("started generating res")
for re in ress:
    r = AdditionalEduResource(name=re, url="somesite.com")
    r.save()
i = 0
print("res generated")
print("started generating users")
while i < len(surnames):
    user = User.objects.create_user(username=surnames[i]+str(i), password=surnames[i]+surnames[i])
    user.save()
    i+=1
print("users generated")
print("started generating students")
i = 0
while i < len(names):
    grs = Group.objects.filter(name=st_groups[i])
    if(len(grs)==0):
        gr = Group.objects.all()[0]
    else:
        gr =Group.objects.get(name=st_groups[i])
    stud = Student(name=names[i], surname=surnames[i], group=gr,
                   user=User.objects.all()[i])
    stud.save()
    i+=1
print("students generated")
print("started generating resToStud")
i = 0
while i < len(names):
    rts = ResourceToStudent(student=Student.objects.all()[i],
                            resource=AdditionalEduResource.objects.all()[i%len(ress)])
    rts.save()
    i+=1
print("resToStudGenerated")
print("started generating PointLists")
i = 0
while i < maxSem:
    for stud in Student.objects.all():
        for sub in Subject.objects.all():
            pl = PointList(student=stud, subject=sub, semester=i, point=50+random.random()*50)
            pl.save()
    i+=1
print("PointLists generated")
print("started generating lessons")
for gr in Group.objects.all():
    for sb in Subject.objects.all():
        tot = random.randint(20, 50)
        ls = Lesson(group=gr, subject=sb, total=tot,
                    passed=random.randint(0, tot))
        ls.save()
print("lessons generated")