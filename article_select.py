#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:17:20 2022

@author: edu
"""

import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

sheet_url = "https://docs.google.com/spreadsheets/d/1of86-Ptb-dbE0TanivUn2eYDbTfrwMws__w9yrSUDVU/edit#gid=1926997835"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
data = pd.read_csv(url_1)
remove_words=["mato grosso do sul",'primate','aves','nematode','membracidae','mosquitoes'
              ,'arbuscular mycorrhizal','isoptera','myxomycetes','lizards','rhizosphere','holoparasitic'
              ,'castor bean','floral visitors','insect galls','plant-ant',"extrafloral nectaries",
              'molecular','agroforestry','sunflower crop','crop',"pollen traits",'insect','farming'
              ,'macroarthropods',"populational and spatial structure",'cyrtopodium holstii'
              ,'hábitos alimentares','dasypodidae','macrolichens','planobídeos','pleistocênicos'
              ,'distribuição geográfica','hidrometria','fenológicos','pantanal','triatoma sordida','briófitas',
              "zoogeográfico",'doença de chagas','checklist','proteins','anurans','ovinos','bovinos',
              'apis mellifera','cabras','silvopastoral','tegumento','hymenoptera','caprinos','biologia floral',
              'sementes','semente', "cabra",'perdas de solo','sobrevivência','composição nutricional'
              ,'reprodução','ocorrência','brazilian cerrado','cerrado','distribuição geográfica','eussociais',
              'visitantes florais','basidiomycota','produção','production','irrigated','agrária','check-list',
              'tradicional','o gênero','micorrízicos','esquistossomose','ndvi','apidae','diptera','recursos florais',
              'biology','cerrado','nidificação','dispersão','silage',"espaço-temporal",'faun','plantas jovens','amazônia',
              'elementos','aves','pteridófitas','lizards','bee','mammals','use of plant resources','foraging'
              ,'perda de solo','biologia','reprodu','trypanosoma cruzi','cordeiros','anatomia','hospedeiro','taninos'
              ,'equations','bovista','trap-nesting','chromosomal','taxonomia','anfíbios','solo','tannin','beija-flores'
              ,"mineração",'melão','novilhos','fungos','invasão biológica','biológica','legumes','new specie'
              ,'nova espécie','infectividade','fruit','frutíferas','bacteria','phyllanthaceae','agroflorestais'
              ,'novas espécies','descrição','crescimento','isoptera','o gênero','índices','frutos','perennial','vespas'
              ,'bioquímica','microbiana','infection','a família','ensino','lizards','checklist','doença','cultura', 'agrícola'
              ,'pasture',"pasto",'predação','ovino','palinologia','ovino','floral','a new specie','in vitro',"canavial"
              ,"ração",'componente herbáceo','biologia reprodutiva','polínica','corredor','hospedeiros','beija-flore','fenologia'
              'de crescimento','vegetação herbácea','pimenta','aceae','percep','medicinal','squamata','proteína'
              ,"flavonóide",'modelling','model','síndromes','historical relationships','distribution','insect'
              ,'geographic distribution','food','nutrition','uma nova espécie','indigenous','medicin','comportamento','notas'
              ,"germina",'serapilheira','pré-tratamento','aquatic','macrophytes','aqu','dormência','arachnida','ruminant'
              ,'forage',"cabr",'históricas','rain forest','vegetação herbácea','herbaceous','spider',"wasp", 'biolog'
              ,'estimada','conhecimento botânico local','degradação da caatinga','ant','n-15','refugia','microorgan'
              ,'arthropoda','coppicing','predator','revegetation','dregaded','recovery','mutualistic','herb','root'
              ,'seedlings', 'mapping' ,'ants','new record','agro-ecosystem','herbáceas','fisiol','fruto', 'helmint','fenologia'
              ,'helmintos','reptiles','amphibians','agroecológico','nectários','educação','farm','modis','bird','detoxification'
              ,"dióxido de carbono",'termites','bioindicator','goat','physiological',"biogeochemical",'agroeconômico','genitais'
              ,'serpentes','mucorales','siluriformes','adaptações','conhecimento','scorpion','crustacea','morphometric'
              ,'lizard','sediment','snake','lizard','catfish','anura','erosion','erosion','físico-química','sensoriamento remoto'
              ,"algae",'morcegos','landsat','soil','carbon sequestration','remote sensing','phytoplankton','rodoent','honeys'
              ,'oxygen-18','amazonian','invasive','fish','paulo','maize','parana','wetland','oil','chemical composition'
              ,'pollen','career','porto alegre','peat bog','flooded','damselfly','bromeliad','botanical knowledge','particles'
              ,"fertiliser",'succulent','amazonian','aluminum',"canga",'european','mining','urban','physico-chemical'
              ,'inundation','mid-holocene','late holocene','planescope','brazilian savanna','seed','mangrove','heath'
              ,"neotropical savanna",'systematic conservation planning','urban','radiation','remote sensing','lakes','araucaria'
              ,'isotope','water quality','rodent', 'bentic','palms','palynology','ethnobotanical','frugivory','wind','marine'
              ,"amazon",'chemical','rio grande do sul','eucalyptus','endozoochory','eucalyptus','a new','odonate','pleistocene'
              ,'chemical','amazon','reservoir', 'andean','bat','predictions','carbon', 'cacti','occurrence','swamp','satellite','alien','notes'
              ,'planetscope','c-14','fabrication','classification','image','murundus','palynological','bryophyte','dam','imaging','chlorophyll'
              ,"orchid",'bryophyte','flooding','freshwater','vegetation indice','greenhouse', "rio de janeiro",'fungi','myrmecochory','metaanalysis'
              ,'freshwater','multispectral','rio de janeiro','sugarcane','late-holocene','the genus','bryophytes', 'asia','flow','genetic diversity'
              ,'mato grosso','bryophyt','cerrad','cultiva','wet','lichen','bryophyte','quaternary','cultivation','flooding','agriculture'
              ,'nectary','soybean','yield','sunflowers','liana','course','offshore','nurse','vehicles','uav-multispectral','simulation'
              ,'agriculture','soybean','simula','anatomy', 'trait','epiphyte', 'restoration','population','leguminosae','record','regenaration'
              ,'potential','development','regeneration','juss','diatom','sustainability']


for i in  np.unique(remove_words):
    data['select']=data['title'].str.contains(r'{0}'.format(i))
    print(data.shape[0])
    d1=data
    data=data[data.select != True]
    print(data.shape[0])

text = " ".join(cat.split()[1] for cat in data.title)
text=text.replace(' e ','')
text=text.replace(' da ','')
text=text.replace(' de ','')
# Creating word_cloud with text as argument in .generate() method
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
# Display the generated Word Cloud
plt.figure(figsize=(12,10))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('/home/edu/wc.png')
data.to_csv('/home/edu/artigos_pre_processados.csv')
