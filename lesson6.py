

def func_2():
    def func_3():
        print('in func_3 x =', x)
    x = 28
    print('in func_2 x =', x)
    func_3()


x = 42
func_2()
print('x =', x)

# Область видимости функции задается в момент её определения, не в момент вызова!
for _ in range(4):
    print(_)