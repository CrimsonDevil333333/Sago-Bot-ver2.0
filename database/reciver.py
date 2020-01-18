import smtplib

def reader():
    read_file = open("database\Data.txt", "r")
    data_read = read_file.read()
    read_file.close()
    return data_read

def Mail_Recever(m):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("username@gmail.com", "PASS")
        s.sendmail("username@gmail.com", "reviever@gmail.com", m) 
        s.quit()
    except:
        print("\nPlease check your net conectivity for better performance\n")

