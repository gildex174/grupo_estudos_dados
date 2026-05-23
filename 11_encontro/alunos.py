class Student:
    def __init__(self, name, course, favorite_flag):
        self.name = name 
        self.course = course
        self.favorite_flag = favorite_flag

        if self.name == "":
            raise ValueError("Faltou o nome!!")
        if self.course not in ["fisica", "fiscomp", "biomol", "lic"]:
            raise ValueError("Curso inválido!")
        
    def __str__(self):
        return f"{self.name} faz {self.course}"
    
    def print_favorite_flag(self):
        match self.favorite_flag:
            case "Brasil":
                print("🇧🇷")
            case "Coreia":
                print("🇰🇷")
            case "Eritreia":
                print("🇪🇷")
            case _:
                print("🏳️")

def get_student():

    name = input("Name: ")
    course = input("Course: ")
    favorite_flag = input("Flag: ")

    student = Student(name, course, favorite_flag)

    return student

def main():
    student = get_student()

    if student.name =="Artur":
        student.course =  "Fiscomp"

    print(student)

    student.print_favorite_flag()

if __name__ == "__main__":
    main()
