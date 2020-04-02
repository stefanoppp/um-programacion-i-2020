class PizzaTime():
    def __init__(self):
        self.pizza_style = ''
        self.flavors = []

    def choice_style(self, p_style):
        if p_style == '0':
            self.pizza_style = 'Vegetariana'
            self.flavors = ['Pimiento', 'Toffu']
        elif p_style == '1':
            self.pizza_style = 'No Vegetariana'
            self.flavors = ['Pepperoni', 'Jamon', 'Salmon']
        else:
            print('fail_order')
            exit()

    def return_s_f(self, num):
        p = self.pizza_style
        s = self.flavors[num]
        return p, s

    def print_flavors(self):
        num = 0
        print('\n\tElige un sabor:\n')
        for flavor in self.flavors:
            print('\t{n}-{f}'.format(n=str(num), f=flavor))
            num += 1


def main():
    pizza = PizzaTime()
    print('''
    \t->PIZZA TIME<-
    Que tipo de pizza desea ordenar?\n
    0) Vegetariana
    1) No Vegetariana
    ''')
    # Ordenar una pizza
    select = input('>')
    pizza.choice_style(select)
    pizza.print_flavors()
    sel = input('>')
    ch = pizza.return_s_f(int(sel))
    # Pizza ordenada
    print('''\n
    Usted eligio una pizza:{style}.
    Los ingredientes de esta son:
    -Muzzarela
    -Tomate
    -{flavor}
    '''.format(style=ch[0], flavor=ch[1]))


if __name__ == '__main__':
    main()
