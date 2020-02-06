groupmates =  [
{
    "name": "Иван",
    "surname": "Асначев",
    "exams": ["Информатика","ЭЭиСЭ","Web"],
    "marks": [4,3,5]
    },
{
    "name": "Роман",
    "surname": "Горелов",
    "exams": ["Информатика","ВМ","Физика"],
    "marks": [5,4,4]
    },
{
    "name": "Евгений",
    "surname": "Каринов",
    "exams": ["КТП","АиГ","Физика"],
    "marks": [5,5,3]
    
    },
{
    "name": "Арсен",
    "surname": "Вартанян",
    "exams": ["Философия","СиАОД","Физика"],
    "marks": [5,5,5]   
    },
    {
    "name": "Валерий",
    "surname": "Сычев",
    "exams": ["ВМ","ТЯП","МЛиТА"],
    "marks": [5,4,5]   
    },
]
def print_students(students):
    print(u"Имя".ljust(15),u"Фамилия".ljust(10),u"Экзамены".ljust(30),
          u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),student["surname"].ljust(10),
              str(student["exams"]).ljust(35),str(student["marks"]).ljust(20))
print_students(groupmates)
average = input()
average_mark = 0
filtered_students = []
def filter_average(students):
    
    for student in students:
        average_mark = 0
        for mark in student["marks"]:
            average_mark = average_mark + mark
        average_mark = average_mark/len(student["marks"])
        if float(average) < average_mark:
            filtered_students.append(student)
            print(student["name"].ljust(15),student["surname"].ljust(10),
            str(student["exams"]).ljust(35),str(student["marks"]).ljust(20))
filter_average(groupmates)
