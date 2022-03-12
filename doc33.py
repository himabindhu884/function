# Q33. Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi > 30 return "Obese"
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"


def fun():
    a=int(input('num'))
    if a>30:
        print('obese')
    elif a<=18.5:
        print('underweight')
    elif a>=18.5 and a<=25.0:
        print('normal')
    elif a>=25.0 and a<=30:
        print('overweight')
    else:
        print('nothing')
fun()