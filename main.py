def count_word(chaine):
    # Cette ligne va permettre au code de conter 1 mot chaque fois qu'ìl y a une espace vide dans la phrase
    return len(chaine.split(' '))

# Lorsque le code va etre executer, la console va nous demander d'ecrire une phrase grace au input
phrase = input("Ecrit une phrase")
# Cette ligne va permetre au console de conter le nombre de mot dans la phrase ecrite
print(count_word(phrase))
