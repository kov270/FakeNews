from histogram import Dictogram

#глубина по кол-ву символов
'''def make_higher_order_markov_model(order, data):
    markov_model = dict()

    for i in range(0, len(data)-1):
        # Создаем окно
        window = tuple(data[i: i])
        # Добавляем в словарь
        if window in markov_model:
            # Присоединяем к уже существующему распределению
            markov_model[window].update([data[i]])
        else:
            markov_model[window] = Dictogram([data[i]])
    f = open('markov_status', 'w', encoding='utf8')
    f.write(str(markov_model))
    return markov_model'''

#глубина для словосочетаний (в кол-ве двух штук), осторожно он костыльный
def make_higher_order_markov_model(order, data):
    data = data.split(' ')
    markov_model = dict()
    k = 1
    for i in range(0, len(data)//2 -1):
        data[i] = data[k] + ' ' + data[k+1]
        k += 2

    for i in range(0, len(data)-1):
        print(data[i])
        if data[i] in markov_model:
            # Просто присоединяем к уже существующему распределению
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = Dictogram([data[i+1]])

    f = open('markov_status', 'w', encoding='utf8')
    f.write(str(markov_model))
    return markov_model