import datetime

def initializing_database():
    name=input("Please enter your name - ")
    now = datetime.datetime.now()
    real_time = now.strftime("%Y-%m-%d %H:%M")
    file = open("database\Data.txt","a")
    file.write(real_time + "  "+"'"+name+"'" +"\n")
    file.close()
    print("Ask questions here - \n")
    
def database_input(A):
    file = open("database\Data.txt", "a")
    file.write("\t\t---" + A + "---\n")
    file.close()

def wikipedia_search(N):
    file = open("database\Data.txt", "a")
    file.write("\t\t\t" + N + "....\n")
    file.close()

def unknown_input(N):
    file = open ("database\Data.txt","a")
    file.write("--------------Error here\n")
    file.close()
