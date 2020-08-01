from src import help
from src import add
from src import rm



version = '0.9.0'
print(f'Todo app for cli ver {version}  type "help"!! ')
while True:
    order = input("> ")

    if order.startswith('help'):
        help.help()

    elif order.startswith('q'):
        print('Bye! See you later!')
        break
    elif order.startswith('add'):
        add.add(order)
    else:
        print(f'There is not command "{order}"')