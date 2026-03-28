import sqlite3

con = sqlite3.connect('brain.db')
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS BRAINDATA (inkey TEXT PRIMARY KEY, outvalue TEXT)")

name = input("what is your name: ")

if name != "Abhi":
    print("sorry wrong name")
    con.close()
    exit()

print("hey abhi! start talking, type bye to quit\n")

while True:
    ipt = input("").strip()

    if ipt.lower() == "bye":
        print("good bye, talk to you later!")
        break

    cursor.execute("SELECT outvalue FROM BRAINDATA WHERE inkey = ?", (ipt,))
    result = cursor.fetchone()

    if result:
        print(result[0])
    else:
        print("sorry i didn't understand that")
        teach = input("teach me the reply (or type skip): ").strip()

        if teach == "skip" or teach == "":
            print("ok moving on\n")
        else:
            cursor.execute("INSERT OR REPLACE INTO BRAINDATA VALUES (?, ?)", (ipt, teach))
            con.commit()
            print("got it! thanks for teaching me\n")

con.close()