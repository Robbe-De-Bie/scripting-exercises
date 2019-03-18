# Write your code here
def slug(name):
    stukken = name.split(' ')
    voornaam = stukken[0]
    naam = stukken[1:]

    return '-'.join(s.lower() for s in naam + [voornaam])