from main.models import Features

def load_all_symptoms():
    f = open('list_symptoms.txt', 'r')
    symps = f.read()
    symps = symps.replace("prognosis", '')
    symps = symps.replace("'", '')
    symps = symps.replace('"', '')
    symps = symps.replace("[", '')
    symps = symps.replace("]", '')
    symps = symps.replace(" ", '')
    symps = symps.capitalize()
    symps = symps.replace(",,", '')
    symps = symps.replace("_", ' ')
    symps = symps.title()
    symps = symps.split(',')

    for symp in symps:
        print(f'<Features: {symp}>')
        Features.objects.create(txt = symp)
