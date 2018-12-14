#!/usr/bin/python
# -*- coding: utf-8 -*
import os
import re
import sys
import xml.etree.ElementTree as ET
from lxml import etree


def createXmlFile(text):
	


				
		filename = text+".xml"
		print (filename)
		root = ET.Element("article")
		userelement = ET.SubElement(root,"preamble")
		userelement1 = ET.SubElement(root,"titre")
		userelement2 = ET.SubElement(root,"auteur")
		userelement3 = ET.SubElement(root,"abstract")
		userelement3 = ET.SubElement(root,"biblio")
  
		tree= ET.ElementTree(root)
		tree.write(filename)

def createFichierTxt() :
	
			listFichierPdf = os.listdir('.') 

			dir_path = os.path.dirname(os.path.abspath(__file__))

			for i in listFichierPdf :
				  if i.endswith(".pdf"):
					  s = os.path.splitext(os.path.basename(i))[0]
					  b= i.replace(' ', '_')
					  os.rename (i , b)
					  cmd=  'pdftotext ' + b  + ' ' + s +'.txt'
					  os.system( cmd )
					  
				
				  if i.endswith(".txt"):
					  os.remove(os.path.join(dir_path, i))
					

				
				  
					
def createFichierXml() :	
	listFichierPdf = os.listdir('.') 

	dir_path = os.path.dirname(os.path.abspath(__file__))

	for i in listFichierPdf :
		if i.endswith(".pdf"):
					  s = os.path.splitext(os.path.basename(i))[0]
					  b= i.replace(' ', '_')
					  os.rename (i , b)
					  cmd=  'pdftotext ' + b  + ' ' + s +'.txt'
					  os.system( cmd )
					  createXmlFile(s)
								
					
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
				f1 = open (os.path.splitext(os.path.basename(i))[0]+'modif', "w")
				f1.write ("title : " +os.path.splitext(os.path.basename(i))[0] +"\n")
				for x , line in enumerate(f):
					if x == 3 :
						f1.write("auteur  : " + line)
						f.close
						f1.close
		

def parsingTxt():
	
	listFichierPdf = os.listdir('.') 
	dir_path = os.path.dirname(os.path.abspath(__file__))
		
	for i in listFichierPdf :
			if i.endswith(".txt"):
		
						f= open (i ,"r")
						fichier = open (os.path.splitext(os.path.basename(i))[0]+'modif.txt' , "a")
						for x , line in enumerate(f):
							if x == 3 :
								fichier.write("auteur  : " + line)
								f.close
								fichier.close
													
								
						with open(i, "r") as f:
					
								textfile_temp = f.read()
								titre = os.path.splitext(os.path.basename(i))[0]
								fichier.write("title : " +titre +"\n")
								fichier.write( 'abstract : '+ textfile_temp.split("abstract")[1].split("introduction")[0]+ "\n")
								titre=titre.replace("_"," ")
								fichier.write("preamble: " +titre+ "\n")
								
								fichier.write("biblio : " + textfile_temp.split("references")[1].split("\n\n")[0]+"\n")
								fichier.close
								f.close
									
							
						
							
			
def parsingXml():
	listFichierPdf = os.listdir('.') 
	dir_path = os.path.dirname(os.path.abspath(__file__))
		
	for i in listFichierPdf :
			if i.endswith(".txt"):
		
						
	
						tree = ET.parse(os.path.splitext(os.path.basename(i))[0]+'.xml',parser=ET.XMLParser(encoding='utf8'))  
						root = tree.getroot()
						titre = os.path.splitext(os.path.basename(i))[0]
						with open(i, "r") as f:
							for x , line in enumerate(f):
								if x == 3 :
									for elem in root.iter('auteur'):  
										special = u"\u2022"
										elem.text =  line.replace(special,'X')
										tree.write(os.path.splitext(os.path.basename(i))[0]+'.xml',encoding="utf-8")
						with open(i, "r") as f:	
							textfile_temp = f.read()
							for elem in root.iter('titre'):
								
										titre=titre.replace("_"," ") 
										elem.text = titre
							for elem in root.iter('abstract'):  
										elem.text = textfile_temp.split("abstract")[1].split("introduction")[0]
										tree.write(os.path.splitext(os.path.basename(i))[0]+'.xml',encoding="utf-8") 
							for elem in root.iter('biblio'):  
										elem.text = textfile_temp.split("references")[1].split("\n\n")[0]
										tree.write(os.path.splitext(os.path.basename(i))[0]+'.xml',encoding="utf-8") 
									
							for elem in root.iter('preamble'):  
										elem.text = os.path.splitext(os.path.basename(i))[0] +"\n"
										tree.write(os.path.splitext(os.path.basename(i))[0]+'.xml',encoding="utf-8") 
							
					
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



def movetxt():
	
		listFichierPdf = os.listdir('.')
		dir_path = os.path.dirname(os.path.abspath(__file__))

		for i in listFichierPdf :
				if i.endswith(".txt"):
					try:
						cmd = 'mv '+ os.path.splitext(os.path.basename(i))[0]+'modif.txt' + ' ' + os.path.splitext(os.path.basename(i))[0]
					
						os.system(cmd)
					except OSError as err:
						print("OS error: {0}".format(err))		
		


def movexml():
	
		listFichierPdf = os.listdir('.')
		dir_path = os.path.dirname(os.path.abspath(__file__))

		for i in listFichierPdf :
				if i.endswith(".txt"):
					try:
						cmd = 'mv '+ os.path.splitext(os.path.basename(i))[0]+'.xml' + ' ' + os.path.splitext(os.path.basename(i))[0]
					
						os.system(cmd)
					except OSError as err:
						print("OS error: {0}".format(err))		
					



def main (argv):
	for arg in sys.argv[1:]:
		if arg == '-t':
			createFolder()
			createFichierTxt() 
			lower()	
			parsingTxt()
			movetxt()
			os.system('rm *.txt')
		if arg == '-x':
			createFolder()
			createFichierXml() 
			lower()	
			parsingXml()
			movexml()
			os.system('rm *.txt')

		
	
	
	
if __name__ == '__main__':
	
	main(sys.argv[1:])

	
	
