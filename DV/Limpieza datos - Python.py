# -*- coding: utf-8 -*-

import pandas as pd


#EDICIÓN DATOS:

# Carga de las 2 fuentes de datos:
salaries = pd.read_csv('Datos/net_salary_per_town_categories.csv')
geog = pd.read_csv('Datos/name_geographic_information.csv')

# Limpieza geog:
geog = geog.rename(columns={"code_région":"REG", "nom_région":"nom_REG", "numéro_département":"DEP",  
                            "nom_département":"nom_DEP", "nom_commune":"town", "code_insee":"CODGEO"})
geog = geog.drop(['EU_circo', 'chef.lieu_région', 'chef.lieu_région', 'préfecture', 'numéro_circonscription', 
                  'codes_postaux', 'éloignement'], axis = 1)
geog = geog.drop_duplicates()

# Limpieza salaries:
salaries = salaries.rename(columns={'LIBGEO': "town", 'SNHM14':"MS", 'SNHMF14':"MSF", 'SNHMH14':"MSM", 'SNHM1814':"MS1825", 
        'SNHM2614':"MS2650", 'SNHM5014':"MS51", 'SNHMF1814':"MSF1825", 'SNHMF2614':"MSF2650", 'SNHMF5014':"MSF51",
        'SNHMH1814':"MSM1825", 'SNHMH2614':"MSM2650", 'SNHMH5014':"MSM51", 'SNHMC14':"MSexecutive", 'SNHMP14':"MSmanager", 
        'SNHME14':"MSemployee",'SNHMO14':"MSworker",'SNHMFC14':"MSFexecutive", 'SNHMFP14':"MSFmanager", 
        'SNHMFE14':"MSFemployee", 'SNHMFO14':"MSFworker", 'SNHMHC14':"MSMexecutive", 'SNHMHP14':"MSMmanager", 
        'SNHMHE14':"MSMemployee", 'SNHMHO14':"MSMworker"})
salaries["gender_diff"] = salaries["MSM"] - salaries["MSF"]
salaries["Executive_diff"] = salaries["MSMexecutive"] - salaries["MSFexecutive"]
salaries["Manager_diff"] = salaries["MSMmanager"] - salaries["MSFmanager"]
salaries["Employee_diff"] = salaries["MSMemployee"] - salaries["MSFemployee"]
salaries["Worker_diff"] = salaries["MSMworker"] - salaries["MSFworker"]


# Unificar fuentes de datos:
salaries.CODGEO = pd.to_numeric(salaries.CODGEO, errors="coerce")
df = pd.merge(geog, salaries, on = "CODGEO")
df["nom_REG"] = df["nom_REG"].astype('category')



########

# Datos Salarios por género y puesto:

salaries = salaries[["MSF", "MSM", "MSFexecutive", "MSMexecutive", 
                      "MSFmanager", "MSMmanager", "MSFemployee", "MSMemployee",
                      "MSFworker", "MSMworker"]].mean().to_csv('datos.csv')



#########
# Datos Brecha salarial por regiones:

compSalario = df[["nom_REG", "gender_diff"]].groupby("nom_REG").mean()
compSalario = compSalario.sort_values(["gender_diff"], ascending=False).to_csv('datos2.csv', header=False)


"""
# Cargar los datos para generar los gráficos: 

lista  =[]
with open('datos.csv', 'r') as archivo_lectura:
    for linea in archivo_lectura:
        a = {}
        a['label'] = linea.split(',')[0]
        a['value'] = linea.split(',')[1].strip()
        lista.append(a)


lista2  =[]
with open('datos2.csv', 'r') as archivo_lectura:
    for linea in archivo_lectura:
        b = {}
        b['label'] = linea.split(',')[0]
        b['value'] = linea.split(',')[1].strip()
        lista.append(a)
"""    