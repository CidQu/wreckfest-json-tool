import json
import os 
import csv

print('Enter File Name, ex: txt.json')

jsonname = input()

f = open(jsonname)

data = json.load(f)

directory = os.getcwd()
txtdosyasi = directory + '\\1.txt'
txtyol = os.path.join(txtdosyasi)

for i in data['segments']:
    def yazilari_al(i):
        if 3 < uzunluk < 5:
            bir = i["texts"][0]["value"] + ' |cidqu| '
            iki = i["texts"][1]["value"] + ' |cidqu| '
            üç = i["texts"][2]["value"] + ' |cidqu| '
            dört = i["texts"][3]["value"]
            yazilar = bir + iki + üç + dört
            return yazilar
        elif 2 < uzunluk < 3:
            bir = i["texts"][0]["value"] + ' |cidqu| '
            iki = i["texts"][1]["value"] + ' |cidqu| '
            üç = i["texts"][2]["value"]
            yazilar = bir + iki + üç
            return yazilar
        elif 1 < uzunluk < 2:
            bir = i["texts"][0]["value"] + ' |cidqu| '
            iki = i["texts"][1]["value"]
            yazilar = bir + iki
            return yazilar
        else:
            yazilar = i["texts"][0]["value"]
            return yazilar
    
    kod = i["id"]
    uzunluk = len(i["texts"])
    yazilar = yazilari_al(i)
    with open('csv.csv', 'a', newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([kod, yazilar])
    
f.close()