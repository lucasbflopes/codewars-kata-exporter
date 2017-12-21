import json
import os
from helper.api import CodeWarsApi
from helper.kata import KataParser

with open('./setup.json') as fin:
    setup = json.load(fin)

with open('./source.html') as fin:
    file = fin.read()

base_dir = setup['download_folder']
extensions = setup['file_extensions']

parser = KataParser(file)
katas = parser.parse_katas()
api = CodeWarsApi(setup['codewars']['api_key'])

print('Exporting katas...')
for i, kata in enumerate(katas):
    print('\r{}/{} katas exported.'.format(i+1, len(katas)), end='')

    kata_description = api.get_kata_description(kata.kata_id)

    for language, source_code in zip(kata.languages, kata.source_codes):
        file_dir = os.path.join(base_dir, kata.difficulty, kata.title, language)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        filename = 'solution' + extensions.get(language, '')
        with open(os.path.join(file_dir, filename), 'w') as fout:
            fout.write(source_code)

        with open(os.path.join(file_dir, 'README.md'), 'w') as fout:
            fout.write(kata_description)