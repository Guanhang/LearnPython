"""
if 要判断的条件:
    条件成立时，要做的事情
缩进为4个空格，缩进为4个空格，缩进为4个空格，缩进为4个空格，缩进为4个空格，缩进为4个空格，

== 检查两个操作数的值是否相等，如果是，则为True
!= 检查两个操作数的值是否不相等，如果是，则为True
>  检查左操作数的值是否大于右操作数，如果是，则为True
<  检查左操作数的值是否小于右操作数，如果是，则为True
>= 检查左操作数的值是否大于或等于右操作数，如果是，则为True
<= 检查左操作数的值是否小于或等于右操作数，如果是，则为True
"""

age = int(input(print("Your Age:")))

if age >= 18:
    print("Welcome to the disco")
else:
    print("Go home!!!")

print("Disco Guan")

# or 判断

height = int(input(print("Your height:")))

if age > 18 or height > 180:
    print("You can Enter")
else:
    print("Go Home")

# 布尔变量

print("are you employee? yes to conform, if you're not,than don't enter anything!")

employee = bool(input(print("?")))

if not employee:
    print("Go home")
else:
    print("Wellcome!")
