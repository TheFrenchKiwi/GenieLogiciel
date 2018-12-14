#!/usr/bin/python
# -*- coding: utf-8 -*
import os
import re
import sys
import xml.etree.ElementTree as ET
from lxml import etree


def createXmlFile(text):
	
# create the file structure

# create a new XML file with the results
				
		filename = text+".xml"
		print (filename)
		root = ET.Element("article")
		userelement = ET.SubElement(root,"preamble")
		userelement1 = ET.SubElement(root,"titre")
		userelement2 = ET.SubElement(root,"auteur")
		userelement3 = ET.SubElement(root,"abstract")
		userelement3 = ET.SubElement(root,"biblio")
		root.append(userelement)
		#myfile = open(text+".xml", "w")  
		#myfile.write(text+".xml")  
		tree= ET.ElementTree(root)
		tree.write(filename)

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
		
def return_utf(s):
    if isinstance(s, str):
        return s.encode('utf-8')
    if isinstance(s, (int, float, complex)):
        return str(s).encode('utf-8')
    try:
        return s.encode('utf-8')
    except TypeError:
        try:
            return str(s).encode('utf-8')
        except AttributeError:
            return s
    except AttributeError:
        return s
    return s # assume it was already utf-8

def parsing2():
	
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
													
											tree = ET.parse(os.path.splitext(os.path.basename(i))[0]+'.xml',parser=ET.XMLParser(encoding='utf8'))  
											root = tree.getroot()
											for elem in root.iter('auteur'):  
												parser = ET.XMLParser(encoding="utf-8")
												tree = ET.fromstring(line, parser=parser)
												elem.text =  return_utf(line)
											tree.write(os.path.splitext(os.path.basename(i))[0]+'.xml',encoding="utf-8")
							
								
							
							
								

						
						with open(i, "r") as f:
				
							textfile_temp = f.read()
							fichier.write("title : " +os.path.splitext(os.path.basename(i))[0] +"\n")
							fichier.write( 'abstract : '+ textfile_temp.split("abstract")[1].split("introduction")[0])
							fichier.close
							f.close
							
							
							tree = ET.parse(os.path.splitext(os.path.basename(i))[0]+'.xml')  
							root = tree.getroot()
							for elem in root.iter('titre'):  
								elem.text = os.path.splitext(os.path.basename(i))[0] +"\n"
							for elem in root.iter('abstract'):  
								elem.text = textfile_temp.split("abstract")[1].split("introduction")[0]
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



def move():
	
		listFichierPdf = os.listdir('.')
		dir_path = os.path.dirname(os.path.abspath(__file__))

		for i in listFichierPdf :
				if i.endswith(".txt"):
					try:
						cmd = 'mv '+ os.path.splitext(os.path.basename(i))[0]+'modif.txt' + ' ' + os.path.splitext(os.path.basename(i))[0]
					
						os.system(cmd)
					except OSError as err:
						print("OS error: {0}".format(err))			
					

if __name__ == '__main__':
	
	createFolder()
	createFichier() 
	lower()	
	#createXmlFile();
	parsing2()
	move()
	os.system('rm *.txt')

	
	
