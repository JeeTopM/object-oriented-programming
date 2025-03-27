names = ['pikachu', 'scyther', 'gyarados', 'gengar']
fname = ['lapras', 'pikachu', 'alakazam']
class Pokemon:
    pass
pokemons = Pokemon()
for i in range(4):
    setattr(pokemons, names[i], "")
for name in fname:
    print(hasattr(pokemons, name))