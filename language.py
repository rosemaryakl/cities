import json
from os import name

COUNTRIES_JSON = '/Users/rosy/Documents/GitHub/cities/node_modules/countries-list/dist/countries.json'
LNG_JSON = '/Users/rosy/Documents/GitHub/cities/node_modules/countries-list/dist/languages.min.json'

def generate_language_name_to_code(json_filepath):
    with open(json_filepath) as json_file:
        languages_dict = json.load(json_file)

        output = {}

    for language_code in languages_dict:
        language_obj = languages_dict[language_code] # all values in languages.json
        language_name = language_obj['name'] #name of language in languages.json
        output[language_name] = language_code 

    return output #''Xhosa': 'xh', 'Chinese': 'zh' 

def generate_language_code_to_countries(json_filepath):
    with open(json_filepath) as json_file:
        countries_arr = json.load(json_file)

        output = {}

    for countries_obj in countries_arr:
        language_obj = countries_arr[countries_obj] # all values in countries.json
        language_code = language_obj['languages'] # language codes in countries.json
        country_name = language_obj['name'] #name of countries in countries.json
        if language_code in output:
            country_languages = output[language_code]
            country_languages.append(country_name)
        else:
            output[language_code] = [country_name]
        
    return output # the output dict will have a dict of key country code and value name of cities 'ZW': ['Zvishavane', 'Victoria Falls', 'Shurugwi', 'Shangani', 'Shamva', 'Rusape', 'Redcliff', 'Raffingora', 'Plumtree', 'Penhalonga', 'Odzi', 'Nyazura', 'Nyanga', 'Norton', 'Mvurwi', 'Mvuma', 'Mutoko', 'Mutare', 'Murehwa', 'Mount Darwin', 'Mhangura', 'Mazowe', 'Masvingo', 'Mashava', 'Marondera', 'Macheke', 'Lupane', 'Lalapanzi', 'Kwekwe', 'Karoi', 'Kariba', 'Kamativi Mine', 'Kadoma', 'Inyati', 'Insiza', 'Hwange', 'Headlands', 'Harare', 'Gweru', 'Gwanda', 'Gokwe', 'Glendale', 'Filabusi', 'Esigodini', 'Dorowa Mining Lease', 'Dete', 'Concession', 'Chivhu', 'Chirundu', 'Chiredzi', 'Chipinge', 'Chinhoyi', 'Chimanimani', 'Chegutu', 'Chakari', 'Centenary', 'Bulawayo', 'Binga', 'Bindura', 'Beitbridge', 'Beatrice', 'Banket', 'Epworth', 'Chitungwiza']

language_code_to_cities_dict = generate_language_code_to_countries(LNG_JSON) # ex {'AD': ['Sant Julià de Lòria']} 
language_name_to_code_dict = generate_language_name_to_code(COUNTRIES_JSON) # entire dict of name / code ex : 'South Africa': 'ZA', 'Zambia': 'ZM', 'Zimbabwe': 'ZW' }

language_name_or_code = input('Enter a Language Name / Code: ')

#success = True
if language_name_or_code in language_code_to_cities_dict: # enter name or code both work to get output which is a list of cities
    language_code = language_name_or_code
    success = True
elif language_name_or_code in language_name_to_code_dict:
    language_code = language_name_to_code_dict[language_name_or_code]
    success = True
else:
    print("Language name / code does not exist.")
    success = False

if success:
    language_countries = language_code_to_cities_dict[language_code]
    print (language_countries)

