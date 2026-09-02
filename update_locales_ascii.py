# -*- coding: utf-8 -*-
import json

def update_locale(file_path, translations):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    data['contact'].update(translations)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

fr_trans = {
    "phone": "Telephone",
    "phone_ph": "+33 6 00 00 00 00",
    "budget": "Budget (Optionnel)",
    "budget_small": "Moins de 1000",
    "budget_med": "1000 - 5000",
    "budget_large": "Plus de 5000"
}

en_trans = {
    "phone": "Phone",
    "phone_ph": "+1 234 567 8900",
    "budget": "Budget (Optional)",
    "budget_small": "Under 1000",
    "budget_med": "1000 - 5000",
    "budget_large": "Over 5000"
}

update_locale('src/locales/fr.json', fr_trans)
update_locale('src/locales/en.json', en_trans)
