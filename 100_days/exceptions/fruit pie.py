

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + 'pie')


fruits = eval(input("enter list of fruits"))


make_pie(4)


