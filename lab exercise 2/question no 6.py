''''#weight convertor;
#input the weight of a person in either kg or lbs.
#if the person provides his/her weight in kg then convert it into lbs else convert it to kg.'''
weight=float(input("enter the weight in kg or lbs: "))
weight1=(input("Choose the weight in kg or lbs:"))lower.()
if weight1=="kg":
    weight2=weight*2.2
    print(weight2)
elif weight1 == "lbs":
    weight2=weight/2.2
    print(weight2)
else:
    print("imvalid format")