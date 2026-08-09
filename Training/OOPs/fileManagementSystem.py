import os
class FileManagementSystem:
  
  def create_file(self):
    file_name=input("Enter the new file name ")
    if os.path.exists(file_name):
      print("already exist ")
    else:
      open(file_name,"w").close()
      print("File created ")

  def update_file(self):
    update_file=input("enter the file name you want to update: -")
    if os.path.exists(update_file):
      content=input("enter the content :- ")
      with open (update_file,"a") as f:
        f.write("\n"+content)
        print("file updates sucessfully")
    else:
      print("file doesnt exist")

  def showFile(self):
    list1=os.listdir()
    for i in list1:
      print(i)

  def deletFile(self):
    file=input("Enter the file name you want to delete :- ")
    if os.path.exists(file):  
        os.remove(file)
        print("file removed sucessfully")
    else:
      print("file doesn't exist's")



file_manager=FileManagementSystem()
while True:
    print("""
1. Create File
2. Update File
3. Show Files
4. Delete File
5. Exit
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        file_manager.create_file()
    elif choice == 2:
        file_manager.update_file()
    elif choice == 3:
        file_manager.showFile()
    elif choice == 4:
        file_manager.deletFile()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice")