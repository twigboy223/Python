print("this is my translator")
print("es mi traductor")
print("you can only do single words")
print("this is a product of julian.v")
translations = {
    'hello': 'hola',
    'hi': 'hola',
    'goodbye': 'adios',
    'please': 'por favor',
    'thank you': 'gracias',
    'bye': 'adios',
    'yes': 'si',
    'no': 'no',
    'morning': 'mañana',
    'night': 'noche',
    'food': 'comida',
    'water': 'agua',
    'friend': 'amigo',
    'family': 'familia',
    'love': 'amor',
    'happy': 'feliz',
    'sad': 'triste',
    'angry': 'enojado',
    'house': 'casa',
    'car': 'coche',
    'school': 'escuela',
    'book': 'libro',
    'computer': 'computadora',
    'phone': 'teléfono',
    'cat': 'gato',
    'dog': 'perro',
    'music': 'música',
    'beach': 'playa',
    'mountain': 'montaña',
    'city': 'ciudad',
}

resp = input("Do you want to do English → Spanish? (yes/no): ").strip().lower()
if resp != 'yes':
    print('OK, exiting.')
else:
    word = input("Enter the English word to translate (single word): ").strip().lower()
    if not word:
        print('No word entered. Exiting.')
    else:
        # try direct lookup
        translation = translations.get(word)
        if translation:
            print('The answer is:', translation)
        else:
            print("Sorry, I don't know that word.")
        