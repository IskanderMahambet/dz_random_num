import random
i1=0
rand=0
numbers_tryed=[]
print('У вас есть 5 попыток, вы должны отгадать рандомное число от 1 до 10')
rand=random.randint(0,10)
for i in range(0,5):
    print(rand)
    num = int(input('Введите число: '))
    numbers_tryed.append(num)
    if num > rand:        
        print('Ваше число больше рандомного')
        continue
    elif num == rand:
        print('Поздравляю вы победили!')
        print('Вам понадобилось',i,'попыток')
        print('Это все вами введённые числа   ',numbers_tryed)
        break
    elif num < rand:
        print('Ваше число меньше рандомного')
        continue




    
    


