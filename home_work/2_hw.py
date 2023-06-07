def task_1(a:str= 'hi', b:int= 14, c:list= [1,2,3], d:bool= True, f:float= 1.2):
    return type(a), type(b), type(c),type(d), type(f)
print(task_1())
def task_2(a:list = [1, 2, 3, 5, 8, 13, 21]):
    return a[:3]
print(task_2())
# последовательность Фибоначи

def task_3(a:int)->int:
    return a**2
print(task_3(5))


