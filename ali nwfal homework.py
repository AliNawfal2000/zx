data = {"Name": "ali ahmed", "Age": 25, "Email": "Aliahmed@gmail.com"}

username = "aliahmed"
password = "12345678"
attempts = 0

while attempts < 3:
    user = input("Enter username: ")
    pw = input("Enter password: ")
    if user == username and pw == password:
        print(data)
        break
    else:
        attempts += 1
        print("Incorrect username or password.")
else:
    data.clear()
    print("Too many failed attempts. Data deleted.")