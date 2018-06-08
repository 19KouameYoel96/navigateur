from tkinter import *
from parser import *
from bs4 import BeautifulSoup
import urllib
import re

fenetre = Tk()

def main():
   LinksList = []
   var=entree.get()
   var=str(var)
   html_page = urllib.request.urlopen(var)
   soup = BeautifulSoup(html_page)
   for link in soup.findAll('a'):
      linkfound = link.get('href')
      LinksList.append(linkfound)
      print (linkfound)
      if LinksList :
         j=0
         yDefilB = Scrollbar(l, orient='vertical')
         yDefilB.grid(row=10, column=5, sticky='ns')
         liste = Listbox(l, height=20, width=60, yscrollcommand=yDefilB.set)
         liste.grid(row=0, column=0, sticky='ns')
         yDefilB['command'] = liste.yview
         for i in LinksList:
            liste.insert(j, i)
            j=j+1

def cherche():
   global LinksList
   j=0 
   strpage=StringVar()
   varb=entree1.get()
   while j<=4:
      name = "fichier"+str(j)
      if 'http' in LinksList[j]:
         html_page = urllib.request.urlopen(LinksList[j])
         soup = BeautifulSoup(html_page)
      #for txt in soup.findAll('p'):
      #strpage.replace(' ', '*')
         mon_fichier = open(name, "a")
         mon_fichier.write(soup.title.string)
      j=j+1
      #if varb in strpage:
      #   print(varb)
      #else:
      #  print(strpage)

#panneau d'affichage des liens
Frame1=Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=0, pady=0)

#fenetre de barre de recherche
Frame2 = Frame(fenetre, borderwidth=2, height=150, relief=GROOVE)
Frame2.pack(side=RIGHT, padx=0, pady=0)

#fenetre 3
Frame3 = Frame(Frame2, borderwidth=2, height=75, relief=GROOVE)
Frame3.pack(side=BOTTOM, padx=0, pady=0)

#fenetre 4
Frame4 = Frame(Frame2, borderwidth=2, height=75, relief=GROOVE)
Frame4.pack(side=BOTTOM, padx=0, pady=0)

#fenetre 5
Frame5 = Frame(fenetre, borderwidth=2, height=75, relief=GROOVE)
Frame5.pack(padx=0, pady=0)
#liste des liens
l=LabelFrame(Frame1, text="ARBORESCENCE", bg="white", height=400, width=350)
l.pack(fill="both", expand="yes")

#liste des mots cchercher
b=LabelFrame(Frame5, text="MOT RECHERCHER",  bg="white", height=400, width=350)
b.pack(fill="both", expand="yes")

#barre de recherche des liens 
titre = Label(Frame4, text="ESATIC SEARCH")
titre.pack()
#input
value = StringVar() 
value.set("entrez l'URL")
entree = Entry(Frame4, textvariable=value, width=70, bg='ivory')
entree.pack(padx=12, pady=10)
Button(Frame4, text ='recherche', bg='red', command=main).pack(side=TOP, padx=5, pady=5)


#barre de recherche d'un texte
titre2 = LabelFrame(Frame2, text="MOT A RECHERCHER")
titre2.pack()

#input de mot a rechercher
value1 = StringVar() 
value1.set("Entrez le mot à rechercher")
entree1 = Entry(Frame4, textvariable=value1, width=70, bg='ivory')
entree1.pack(padx=8, pady=6)
Button(Frame4, text ='recherche texte', bg='blue', command=cherche).pack(side=TOP, padx=5, pady=5)

fenetre.mainloop()


