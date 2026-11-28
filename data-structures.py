
classmates=["Minahil","Amna","Iqra","Sadia","Hajra"]
print("Class:",classmates)
print("Total:", len(classmates))
print("First:", classmates[0], "Last:", classmates[-1])
print("First Three:", classmates[0:3])
classmates[2]= "Laiba"
print("Updated:", classmates)

def remove_student(names,name):
    if name in names:
        names.remove(name)
        return True
    return False

classmates.append("Fiza")
std_left=input("WHo has left the class?")
print("Removed:", remove_student(classmates, std_left))

classmates.sort()
print("sorted:", classmates)

teacher={"name": "Mr.Smith", "subject": "Python", "experience":5}
print("Teacher:", teacher["name"])
print("Subject:", teacher["subject"])
print("Email:", teacher.get("email","Not found"))

teacher["experience"]=6
teacher["room"]= "room no.9"
print("Updated:", teacher)

roll_numbers=[1,2,3,4,5]
directory = dict(zip(roll_numbers,classmates))
print("\nDirectory:", directory)

def find_by_roll(book,roll):
    return book.get(roll, "No student found")
roll=int(input("enter roll no:"))
print("student:", find_by_roll(directory,roll))
print("Roll 2:", find_by_roll(directory, 2))

empty_class = []
print("Empty class:", len(empty_class), empty_class[:3])
print("Remove Amna:", remove_student(empty_class, "Amna"))
