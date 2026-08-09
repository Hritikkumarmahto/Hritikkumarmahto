class Student:
    def __init__(self, roll_no: str, name: str, branch: str, city: str):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch
        self.city = city


class SMS:
    def __init__(self):
        self.students = {}

    def add_student(self, roll_no: str, name: str, branch: str, city: str):
        self.students[roll_no] = Student(roll_no, name, branch, city)

    def remove_student(self, roll_no: str):
        self.students.pop(roll_no, None)

    def display_all(self):
        for s in self.students.values():
            print(f"Roll No: {s.roll_no} | Name: {s.name} | Branch: {s.branch} | City: {s.city}")


def main():
    sms = SMS()
    while True:
        print("\n1. Add Student\n2. Remove Student\n3. List All\n4. Exit")
        choice = input("Choice: ")
        
        if choice == "1":
            sms.add_student(input("Roll No: "), input("Name: "), input("Branch: "), input("City: "))
        elif choice == "2":
            sms.remove_student(input("Roll No to remove: "))
        elif choice == "3":
            sms.display_all()
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
