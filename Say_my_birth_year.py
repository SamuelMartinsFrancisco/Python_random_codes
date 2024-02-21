import datetime, math;

print('\n*** This is a program that uses print, input, and eval functions. ***\n\n');


current_year = datetime.date.today().year;
name = input('Please, what is your name?\n ');
age = input('And, what is your age?\n ');
age = eval(age);
birth_year = current_year - age;

print(name + ',i think you were born in', birth_year, end='.');
is_correct = input('Is my answer right? \nif it isn\'t, please type "n"; if it is, type "y":\n  ');

months = ['', 'january', 'february', 'march',
          'april', 'june', 'july', 'august',
          'september', 'november', 'december'];

birth_month = '';
if is_correct == 'n':
        birth_month = input('\n\nSo, please, let me try one more time. \nWhat is your birth month?\n  ');
        if birth_month in months:
            birth_month = months.index(birth_month);
        age = str(age) + '.' + str(birth_month);
        age = eval(age);
        birth_year = math.floor(current_year - age);
        print('\n' + name + ',i discovered!\nyou were born in', birth_year, end='!');
elif is_correct == 'y':
        print('\n:) :D');
