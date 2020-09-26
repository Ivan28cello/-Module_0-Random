def game_core_random(number):  # создаём функцию

    count = 0  # создаём счётчик попыток
    predict = np.random.randint(1,101)  # загадываем число от 1 до 100
    low = 1  # создаём нижнюю переменную границы рандомного числа
    high = 100  # создаём высшую переменную границы рандомного числа
    
    	# создаём цикл
	while predict != number:
		#  уменьшаем в процессе цикла числовой диапазон для идентификации числа
		#  увеличиваем счётчик попыток на +1
        count += 1
        predict = (low+high)//2  
	if number > predict: 
            low = predict + 1
        elif number < predict: 
            high = predict
            
	return(count) # выходим из цикла, если угадали число
