a: int = 5
b: str = 'строка'
c: list = [1,2]

def indent(s: str, widh: int) ->str:
    return " "*(max(0, widh - len(s)))+s
print(indent('123', 123))

def l(s:str=''):
    return len(s)
print(l())

def w(a:list, b:list)->int:
    return max(len(a), len(b))

print(w([1, 2, 3], [0,3,5,7,9]))



