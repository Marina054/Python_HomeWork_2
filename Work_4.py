#3. Реализуйте случайное перемешивание списка.




import random
list = ['я', 'помню', 'чудное', 'мгновенье', ' :', 'передо', 'мной', 'явилась', 'ты']
random.shuffle(list, random.random)
print(list)