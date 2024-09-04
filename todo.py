import os   #facility to establish the interaction between the user and the operating system

#login functionnality
def read_logins():
    with open("login.txt", "r") as file:
        credentials = file.readlines() #readlines multiple reading of lines from text file
        #print(credentials)

        #we get indivisual username,password as the credentials like this - 
        #[['hello', ' 12345hello'], ['admin', ' admin@123'], ['macos', ' macos#789']]  
        new_credentials = []
        for i in credentials:
            field = i.split(',')
            field[1] = field[1].rstrip()  #rstrip is used to remove \n when we are prinitng the cred.
            new_credentials.append(field) 

        return new_credentials
    
logins = read_logins()

def login():
    ask_username = str(input('Enter your Username: '))
    ask_password = str(input('Enter your Password: '))

    loggedIn = False

    #[['hello', ' 12345hello'], ['admin', ' admin@123'], ['macos', ' macos#789']]
    #    i[0]       i[i]           i[0]        i[1]     ...
    for i in logins:  
        if i[0] == ask_username and loggedIn == False:
            if i[1] == ask_password:
                loggedIn = True 

    if loggedIn == True:
        print(f"Logged in Suceessfully into {ask_username} account !!")
    else:
        print("Username/ Password incorrect")
        login()


#load the tasks from the file
def load_task_file(file_path):
    taskList = [] #create empty list
    if os.path.exists(file_path):
        with open(file_path, "r") as file:    #read mode from the file
            taskList = file.read().splitlines()
    return taskList    


#save the tasks from the file
def save_task_file(file_path, tasks):
    with open(file_path, "w") as file:   #write mode from the file
        for task in tasks:
            #file.write(task)     
            file.write(f"{task}\n") #- f stands for formatted string literal


#show/read task function
def show_tasks(tasks):
    if not tasks:
        print("No Task found!")
    else:
        for ind, task in enumerate(tasks, 1):
            print(f"{ind}. {task}")    


#add/create tasks function    
def add_task(tasks, new_tasks):
    tasks.append(new_tasks)
    print("Task Added Successfully!!")


#update the existing task
def update_task(tasks, index, updated_task):
    if 1 <= index <= len(tasks):
        tasks[index-1] = updated_task
        print("Task Updated Successfully!!")
    else:
        print("Invalid task index")


#delete the task
def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index-1)
        print(f" Task '{deleted_task}' Deleted Successfully!!")
    else:
        print("Invalid task index")    



# Defining main function
def main():

    #to store data(i.e. task) into file
    file_path = "todo_list.txt"

    #to load the tasks from the file
    tasks = load_task_file(file_path)

    while True:
        print("\n=== TODO LIST ===")
        print("1. LOGIN USER ACCOUNT")
        print("2. SHOW/READ TASK")
        print("3. CREATE/ADD TASK")
        print("4. UPDATE TASK")
        print("5. DELETE TASK")
        print("6. SAVE TASK")

        
        choice = input("Enter your choice from (1-6): ")
        if choice == "1":
            login()
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            create_task = input("Enter the new task: ")
            add_task(tasks, create_task)
        elif choice == "4":
            index = int(input("Enter the index to be updated: "))
            updated_task = input("Enter the Update task:")
            update_task(tasks, index, updated_task)
        elif choice == "5":
            index = int(input("Enter the index to be deleted: "))
            delete_task(tasks, index)
        elif choice == "6":
            save_task_file(file_path, tasks)
            print("Task Saved Successfully!!")  
            break
        else:
            print("Invalid choice") 

            
if __name__ == "__main__":
    main()