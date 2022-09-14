def count_word(chaine):
    print(len(chaine.split(" ")))  # Cette ligne va permettre au code de conter 1 mot chaque fois qu'ìl y a une espace vide dans la phrase


phrase = input("Ecrit une phrase")  # Lorsque le code va etre executer, la console va nous demander d'ecrire une phrase grace au input
count_word(phrase)  # Cette ligne va permetre au console de conter le nombre de mot dans la phrase ecrite
