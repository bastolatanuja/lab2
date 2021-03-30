# if the temperature is greature than 30, its a hot day otherwise if its less than 10:
#its less than 10:its a cold day otherwise its neither hot not cold.
temperature=float(input("enter the temperature: "))
if temperature>30:
    print("its a hot day")
elif temperature<10:
    print("its a cold day")
else:
    print("its neither hot nor cold")