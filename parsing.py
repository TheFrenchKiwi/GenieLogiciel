#!/usr/bin/python
# -*- coding: utf-8 -*
import os
import re



def createFichier() :
	
			listFichierPdf = os.listdir('.') 

			dir_path = os.path.dirname(os.path.abspath(__file__))

			for i in listFichierPdf :
				
				  if i.endswith(".txt"):
					  os.remove(os.path.join(dir_path, i))
					

				
				  
				  if i.endswith(".pdf"):
					  s = os.path.splitext(os.path.basename(i))[0]
					  b= i.replace(' ', '_')
					  os.rename (i , b)
					  cmd=  'pdftotext ' + b  + ' ' + s +'.txt'
					  os.system( cmd )
					
					
					
def createFolder():


		listFichierPdf = os.listdir('.')
		dir_path = os.path.dirname(os.path.abspath(__file__))
		
		for i in listFichierPdf :
					os.mkdir(dir_path+"/" + os.path.splitext(os.path.basename(i))[0])


def parsing():
	
		listFichierPdf = os.listdir('.') 
		dir_path = os.path.dirname(os.path.abspath(__file__))
		
		for i in listFichierPdf :
		
			if i.endswith(".txt"):
				f= open (i ,"r")
				f1 = open (os.path.splitext(os.path.basename(i))[0]+'modif' , "w")
				f1.write ("title : " +os.path.splitext(os.path.basename(i))[0] +"\n")
				for x , line in enumerate(f):
					if x == 3 :
						f1.write("auteur  : " + line)
						f.close
						f1.close
		


def parsing2():
	
	listFichierPdf = os.listdir('.') 
	dir_path = os.path.dirname(os.path.abspath(__file__))
		
	for i in listFichierPdf :
			if i.endswith(".txt"):
				
				fichier = open (os.path.splitext(os.path.basename(i))[0]+'modif' , "a")
				with open(i, "rb") as f:
					print i
					textfile_temp = f.read()
					
					fichier.write( 'abstract : '+ textfile_temp.split("abstract")[1].split("introduction")[0])
					fichier.close
					f.close
					
					
					
					
def lower():
	listFichierPdf = os.listdir('.') 
	dir_path = os.path.dirname(os.path.abspath(__file__))
		
	for i in listFichierPdf :
		if i.endswith(".txt"):
			   
			f = open(i, "r")
			text = f.read()
        
			lines = [text.lower() for line in i]
			with open(i, "w") as out:
					out.writelines(lines)


		
if __name__ == '__main__':
	
	#createFolder()
	#createFichier() 	
	parsing()
	parsing2()
	

	

	
	
