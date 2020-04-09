class PizzaTime():              # Mejoras de OOP 2/4/20
    def __init__(self):
        self.pizza_style = ''
        self.pizza_flavor = ''
        self.flavors = []

    def select_style(self, p_style):
        if p_style == '0':
            self.pizza_style = 'Vegetariana'
            self.flavors = ['Pimiento', 'Toffu']
            return 'correct'
        elif p_style == '1':
            self.pizza_style = 'No Vegetariana'
            self.flavors = ['Pepperoni', 'Jamon', 'Salmon']
            return 'correct'
        else:
            return 'fail_order'

    def select_flavor(self, sel):
        sel = int(sel)
        list_len = len(self.flavors)
        if (0 >= sel <= list_len):
            self.pizza_flavor = self.flavors[sel]
            return 'correct'
        else:
            return 'fail_order'

    def check_order(self, check):
        if check == 'fail_order':
            print(check)
            exit()

    @property
    def print_inicio(self):
        print('''
        \t->PIZZA TIME<-
        Que tipo de pizza desea ordenar?\n
        0) Vegetariana
        1) No Vegetariana
        ''')

    @property
    def print_flavors(self):
        num = 0
        print('\n\tElige un sabor:\n')
        for flavor in self.flavors:
            print('\t{n}-{f}'.format(n=str(num), f=flavor))
            num += 1

    @property
    def print_pizza_orden(self):
        print('''\n
        Usted eligio una pizza:{style}.
        Los ingredientes de esta son:
        -Muzzarela
        -Tomate
        -{flavor}
        '''.format(style=self.pizza_style, flavor=self.pizza_flavor))


def main():
    pizza = PizzaTime()
    pizza.print_inicio
    style = input('>')
    ch = pizza.select_style(style)
    pizza.check_order(ch)
    pizza.print_flavors
    sel = input('>')
    ch = pizza.select_flavor(sel)
    pizza.check_order(ch)
    pizza.print_pizza_orden


if __name__ == '__main__':
    main()
