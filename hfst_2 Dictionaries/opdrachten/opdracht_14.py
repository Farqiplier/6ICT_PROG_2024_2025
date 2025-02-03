# Los de opdracht op met behulp van onderstaande dictionary van dictionaries.
laptop_config = {
    "name": "R90Y2ZH1",
    "asset_tag": "R90Y2ZH1",
    "serial": "R90Y2ZH1",
    "model": {"id": 8, "name": "L390 Touch"},
    "status_label": {
        "id": 8,
        "name": "KoopSignpost",
        "status_type": "deployable",
        "status_meta": "deployed"
    },
    "assigned_to": {
        "id": 1957,
        "username": "KOJA071105",
        "name": "Jan Korneel",
        "first_name": "Jan",
        "last_name": "Korneel",
        "employee_number": "KOJA071105",
        "type": "user",
        "created_at": {
            "date": "???",
            "time": "13:36:37"
        }
    },
    "category": {"id": 4, "status": "laptopMETtouch"},
    "manufacturer": {"id": 2, "name": "LENOVO"},
    "supplier": "???",
    "supplier_2": {"id": 1, "name": "SignPost"}
}


laptop_config["assigned_to"]["created_at"]["date"] = "2021-11-09"


laptop_config.pop("supplier_2")



# Er staan een hoop verschillende sleutels 'id' in de geneste dictionary.
# Doorloop de geneste dictionary en print alle waarden gekoppeld aan een sleutel 'ID'
# 	Merk op! Gebruik een for-loop. De code moet blijven werken, ook als de dictionary wijzigt.
# 		       Je mag er wel vanuit gaan dat sleutels 'id' zich ENKEL op het 2de niveau bevinden.

for key in laptop_config.items():
    for id in key:
        if id == "id":
            print(id)