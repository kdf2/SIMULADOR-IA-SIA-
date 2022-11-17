from html.entities import codepoint2name
from lib2to3.pytree import LeafPattern
import re
from turtle import pos



alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
asciikdff=['m','l','k','j','i','h','t','f','e','d','c','b','a','z','y','x','w','v','u','g','s','r','q','p','o','n','_']
traducido=[]
traducido2=[]
def kdff_es(frase):
    lista=list(frase)
    for i in range(len(lista)):
        for j in range(len(alfabeto)):
            if(lista[i]==asciikdff[j]):
                traducido.append(alfabeto[j])
    palabra="".join(traducido)
    return palabra

def es_kdff(frase):
    lista=list(frase)
    for i in range(len(lista)):
        for j in range(len(alfabeto)):
            if(lista[i]==alfabeto[j]):
                traducido2.append(asciikdff[j]) 
    palabra2="".join(traducido2)
    return palabra2
convertir=input("ingrese palabra o frase: ")
print(kdff_es(convertir))
convertir2=input("ingrese palabra o frase: ")
print(es_kdff(convertir2))


