from datetime import date
from babel.dates import format_date
from babel.numbers import format_decimal

if __name__ == '__main__':
    today = date.today()
    print(today)

    formatted_date = format_date(today, locale='en')
    print(formatted_date)

    number = 240000000000.32212
    print(number)

    formatted_number = format_decimal(number, locale='en')
    print(formatted_number)

    name = input('Input your name: ')
    print('Hello {}'.format(name))