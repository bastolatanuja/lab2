#if name is less than 3 characters long-name must be at least 3 characters otherwise if its more
#than 50 character-name must be maximum of 50 characters otherwise -name looks good.
name=(input("enter the name: "))
length=len(name)
if length<3:
    print("name muast be atleast 3 character")
elif length>50:
    print("name must be of 50 character")
else:
    print("name looks good")