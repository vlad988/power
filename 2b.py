import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
a = float(input('Введіть магнітуду: '))
if a < 2:
    print('Мікро')
    print('Мікроземлетруси, не відчуваються.')
elif 3 >= a >= 2:
    print('Дуже слабкі')
    print('Як правило не відчуваються, але реєструються.')
elif 4 >= a >= 3:
    print('Слабкі')
    print('Часто відчуваються, дуже рідко завдають шкоди.')
elif 5 >= a >= 4:
    print('Легкі')
    print('Відчутне тремтіння речей всередині будинків, значна шкода малоймовірна.')
elif 6 >= a >= 5:
    print('Помірні')
    print('Може завдати значної шкоди старим та погано сконструйованим будівлям на незначній території./n Щонайбільше, незначні пошкодження добре спроектованим будівлям.')
elif 7 >= a >= 6:
    print('Сильні')
    print('Може спричинити руйнацію на території до 150 км довжиною/шириною в населених регіонах.')
elif 8 >= a >= 7:
    print('Дуже сильні')
    print('Значна руйнація на значній території.')
elif 10 >= a >= 8:
    print('Великі')
    print('Серйозна руйнація на територіях довжиною/шириною в сотні кілометрів.')
elif a >= a:
    print('Рідкісно великі')
    print('')
printTimeStamp('Nehodenko and Neskoromny Yaroslav')
