from datetime import date
today = date.today()

day = int(input('tugilgan kuningizni kiriting: '))
month = int(input('tugilgan oyingizni kiriting: '))
year = int(input('tugilgan yilingizni kiriting: '))

age = today.year - year - ((today.month, today.day) < (month, day))

print(f'Sizni yoshingiz: {age}')

