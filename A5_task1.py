marks={'Alice': 35 , 'Chloe': 54 , 'Jack': 87, 'Lily': 99, 'Oliver': 65}
name = input("Enter the students's name :")

try:
    print(name,"'s marks :",marks[name])
except KeyError as e :
    print('Student not found')