def greet(language):
    # your code here

    db = [
        ['english', 'Welcome'],
        ['czech', 'Vitejte'],
        ['danish', 'Velkomst'],
        ['dutch', 'Welkom'],
        ['estonian', 'Tere tulemast'],
        ['finnish', 'Tervetuloa'],
        ['flemish', 'Welgekomen'],
        ['french', 'Bienvenue'],
        ['german', 'Willkommen'],
        ['irish', 'Failte'],
        ['italian', 'Benvenuto'],
        ['latvian', 'Gaidits'],
        ['lithuanian', 'Laukiamas'],
        ['polish', 'Witamy'],
        ['spanish', 'Bienvenido'],
        ['swedish', 'Valkommen'],
        ['welsh', 'Croeso']
    ]

    for pair in db:
        if (pair[0]) == language:
            return pair[1];
    return db [0][1];


print(greet('polish1'));
