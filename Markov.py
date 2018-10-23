from histogram import Dictogram


def make_markov_model(data):
    markov_model = Dictogram()
    data = data.split(' ')
    for i in range(0, len(data)-1):
        if data[i] in markov_model:
            # Просто присоединяем к уже существующему распределению
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = Dictogram([data[i+1]])
    f = open('markov_status', 'w', encoding='utf8')
    f.write(str(markov_model))
    return markov_model
