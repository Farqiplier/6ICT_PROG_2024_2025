landen_feiten = {
    'Frankrijk': {
        'hoofdstad': 'Parijs',
        'bevolking': 67348000,
        'taal': 'Frans',
    },
    'België': {
        'hoofdstad': 'Brussel',
        'bevolking': 11563000,
        'taal': ['Nederlands', 'Frans', 'Duits'],
    },
    'Duitsland': {
        'bevolking': 83190556,
        'taal': 'Duits',
    }
}

print("Overzicht van grootste steden in Europese landen...")
for land, feiten in landen_feiten.items():
    for feit, waarde in feiten.items():
        if feit == 'hoofdstad':
            print(f"{land}: {waarde}")
