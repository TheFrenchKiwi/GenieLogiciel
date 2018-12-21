#!/usr/bin/python3
# -*- coding: utf-8 -*
import os
import re
import sys
import argparse
import xml.etree.ElementTree as ET
from lxml import etree
import time
def createXmlFile(text):
				
		filename = text+".xml"
		
		root = ET.Element("article")
		userelement = ET.SubElement(root,"preamble")
		userelement1 = ET.SubElement(root,"titre")
		userelement2 = ET.SubElement(root,"auteur")
		userelement3 = ET.SubElement(root,"abstract")
		userelement4 = ET.SubElement(root,"corps")
		userelement5 = ET.SubElement(root,"conclusions")
		userelement6 = ET.SubElement(root,"biblio")
		
		tree= ET.ElementTree(root)
		tree.write(filename)
		
def createFolder():

			listFichierPdf = os.listdir('.')
			dir_path = os.path.dirname(os.path.abspath(__file__))
			
			for i in listFichierPdf :
						os.mkdir(dir_path+"/" + os.path.splitext(os.path.basename(i))[0])


def createFichierTxt() :
	
			listFichierPdf = os.listdir('.') 

			dir_path = os.path.dirname(os.path.abspath(__file__))

			for i in listFichierPdf :
				  if i.endswith(".pdf"):
					  s = os.path.splitext(os.path.basename(i))[0]
					  b= i.replace(' ', '_')
					  os.rename (i , b)
					  cmd=  'pdftotext -nopgbrk ' + b  + ' ' + s +'.txt'
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
					  cmd=  'pdftotext -nopgbrk ' + b  + ' ' + s +'.txt'
					  os.system( cmd )
					  createXmlFile(s)
	
	

	
								
								
def createFolderByFile(file):
	
			listFichierPdf = os.listdir('.')
			dir_path = os.path.dirname(os.path.abspath(__file__))
			os.mkdir(dir_path+"/" +os.path.splitext(file)[0])
		
			
		




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
								fichier.write("corps : " +textfile_temp.split("references")[1].split("\n\n")[0]+"\n")
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
							for elem in root.iter('conclusions'):
							
										elem.text =  textfile_temp.split("references")[1].split("conclusions")[0] #### a modifier
										
										tree.write(os.path.splitext(os.path.basename(i))[0]+'.xml') 			
										
							for elem in root.iter('corps'):
										
										special = u"\u2022"
										
										elem.text =  textfile_temp.split("introduction")[1].split("acknowledgements")[0].replace(special,'X')
										
										tree.write(os.path.splitext(os.path.basename(i))[0]+'.xml') 
									
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
			f.close()



def movetxt():
	
		listFichierPdf = os.listdir('.')
		dir_path = os.path.dirname(os.path.abspath(__file__))
		
		for i in listFichierPdf :
				if i.endswith(".txt"):
	
						
						cmd = 'mv '+ os.path.splitext(os.path.basename(i))[0]+'modif.txt' + ' ' + os.path.splitext(os.path.basename(i))[0]
						print (cmd)
						os.system(cmd)
				


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
					
	
		
		
def createXmlByFile(file):
		
	 	filename = (os.path.splitext(file)[0]+".xml")
	 	root = ET.Element("article")
	 	userelement = ET.SubElement(root,"preamble")
	 	userelement1 = ET.SubElement(root,"titre")
	 	userelement2 = ET.SubElement(root,"auteur")
	 	userelement3 = ET.SubElement(root,"abstract")
	 	userelement4 = ET.SubElement(root,"corps")
	 	userelement5 = ET.SubElement(root,"conclusions")
	 	userelement6 = ET.SubElement(root,"biblio")
	 	tree= ET.ElementTree(root)
	 	tree.write(filename)
	 	
	 	
	 	
	 	
	 	
	 	
	 	
def createFichierXmlByFile(file):
	
					  s = os.path.splitext(os.path.basename(file))[0]
					  b= file.replace(' ', '_')
					  os.rename (file , b)
					  cmd=  'pdftotext -nopgbrk ' + b  + ' ' + s +'.txt'
					  os.system( cmd )
					  createXmlFile(s)	
				
				
			   	
def lowerByFile(file):
		
			
			f = open(os.path.splitext(file)[0]+".txt", "r")
			text = f.read()
			
			lines = [text.lower() for line in file]
			with open(os.path.splitext(file)[0]+".txt", "w") as out:
					out.writelines(lines)
			f.close()
			
				
def parsingXmlByFile(file):
	
	
						tree = ET.parse(os.path.splitext(os.path.basename(file))[0]+'.xml',parser=ET.XMLParser(encoding='utf8'))  
						root = tree.getroot()
						titre = os.path.splitext(os.path.basename(file))[0]
						with open(os.path.splitext(file)[0]+".txt", "r") as f:
							for x , line in enumerate(file):
								if x == 3 :
									for elem in root.iter('auteur'):  
										special = u"\u2022"
										elem.text =  line.replace(special,'X')
										tree.write(os.path.splitext(os.path.basename(file))[0]+'.xml',encoding="utf-8")
										
						with open(os.path.splitext(file)[0]+".txt", "r") as f:	
							textfile_temp = f.read()
							for elem in root.iter('titre'):
								
										titre=titre.replace("_"," ") 
										elem.text = titre
							for elem in root.iter('abstract'):  
										elem.text = textfile_temp.split("abstract")[1].split("introduction")[0]
										tree.write(os.path.splitext(os.path.basename(file))[0]+'.xml',encoding="utf-8") 
							for elem in root.iter('biblio'):  
										elem.text = textfile_temp.split("references")[1].split("\n\n")[0]
										tree.write(os.path.splitext(os.path.basename(file))[0]+'.xml',encoding="utf-8") 
							for elem in root.iter('conclusions'):
							
										elem.text =  textfile_temp.split("references")[1].split("conclusions")[0] #### a modifier
										
										tree.write(os.path.splitext(os.path.basename(file))[0]+'.xml') 			
										
							for elem in root.iter('corps'):
										
										special = u"\u2022"
										
										elem.text =  textfile_temp.split("introduction")[1].split("acknowledgements")[0].replace(special,'X')
										
										tree.write(os.path.splitext(os.path.basename(file))[0]+'.xml') 
									
							for elem in root.iter('preamble'):  
										elem.text = os.path.splitext(os.path.basename(file))[0] +"\n"
										tree.write(os.path.splitext(os.path.basename(file))[0]+'.xml',encoding="utf-8") 






def movexmlByFile(file):

					try:
						cmd = 'mv '+ os.path.splitext(os.path.basename(file))[0]+'.xml' + ' ' + os.path.splitext(os.path.basename(file))[0]
					
						os.system(cmd)
					except OSError as err:
						print("OS error: {0}".format(err))		
						

def moveTxtByFile(file):

					try:
						cmd = 'mv '+ os.path.splitext(os.path.basename(file))[0]+'.txt' + ' ' + os.path.splitext(os.path.basename(file))[0]
					
						os.system(cmd)
					except OSError as err:
						
						print("OS error: {0}".format(err))		
						

def parsingTxtByFile(file):

					f = open(os.path.splitext(file)[0]+".txt", "r")
					fichier = open (os.path.splitext(os.path.basename(file))[0]+'modif.txt' , "a")
					for x , line in enumerate(f):
							if x == 3 :
								fichier.write("auteur  : " + line)
								f.close
								fichier.close
													
								
								
					with open(os.path.splitext(file)[0]+".txt", "r") as f:
					
								textfile_temp = f.read()
								titre = os.path.splitext(os.path.basename(file))[0]
								fichier.write("title : " +titre +"\n")
								fichier.write( 'abstract : '+ textfile_temp.split("abstract")[1].split("introduction")[0]+ "\n")
								titre=titre.replace("_"," ")
								fichier.write("preamble: " +titre+ "\n")
								
								fichier.write("biblio : " + textfile_temp.split("references")[1].split("\n\n")[0]+"\n")
								fichier.write("corps : " +textfile_temp.split("references")[1].split("\n\n")[0]+"\n")
								fichier.close
								f.close
														

def createFichierTxtByFile(file):
	
					  s = os.path.splitext(os.path.basename(file))[0]
					  b= file.replace(' ', '_')
					  os.rename (file , b)
					  cmd=  'pdftotext -nopgbrk ' + b  + ' ' + s +'.txt'
					  os.system( cmd )
					  
				

def cli_progress_test(func,end_val, bar_length=20):
    for i in range(0, end_val):
        percent = float(i) / end_val
        hashes = '=' * int(round(percent * bar_length))
        spaces = '' * (bar_length - len(hashes))
        sys.stdout.write("\r"+func+":					[8{0}D] {1}%".format(hashes + spaces, int(round(percent * 100))))
        
        sys.stdout.flush()	
        		


def main (argv):
		start_time = time.time()
		parser = argparse.ArgumentParser()
		parser.add_argument('--delete', action='store_true',default=False,help='Delete all txt and xml and all folder in the current directory')
		parser.add_argument('--xml', action='store_true',default=False,help='convert to xml')
		parser.add_argument('--txt', action='store_true',default=False,help='convert to txt')
		parser.add_argument("-tX", "--targetX",help="targeting one file to convert",nargs="*",dest="targetX")
		parser.add_argument("-tt", "--targetT",help="targeting one file to convert",nargs="*",dest="targetT")						
		
		args = parser.parse_args()
			
		if args.delete:
		
				os.system('rm *.txt')
				os.system('rm *.xml')
				os.system('ls -d  */ | xargs rm -rf')
				cli_progress_test("Deleting       ",90000, bar_length=20)	
				sys.stdout.write("\n")
		if args.txt:
			
				createFolder()
				createFichierTxt() 
				lower()	
				parsingTxt()
				movetxt()
				cli_progress_test("Converting to TXT",90000, bar_length=20)	
				sys.stdout.write("\n")
				#os.system('rm *.txt')
		if args.xml:
				createFolder()
				createFichierXml() 
				lower()	
				
				movexml()
				cli_progress_test("Converting to XML",90000, bar_length=20)	
				sys.stdout.write("\n")
				#os.system('rm *.txt')

		if args.targetX :
			   print(" file to convert {}".format(",".join(args.targetX)))
			   createFolderByFile(format(",".join(args.targetX)))
			   createFichierXmlByFile(format(",".join(args.targetX)))
			   lowerByFile(format(",".join(args.targetX)))
			   createXmlByFile(format(",".join(args.targetX)))
			   parsingXmlByFile(format(",".join(args.targetX)))
			   movexmlByFile(format(",".join(args.targetX)))
			   cli_progress_test("Converting to XML",90000, bar_length=20)	
			   sys.stdout.write("\n")
			  # os.system('rm *.txt')
		   
		if args.targetT:
					
				   print(" file to convert {}".format(",".join(args.targetT)))
				   createFolderByFile(format(",".join(args.targetT)))
				   createFichierTxtByFile(format(",".join(args.targetT)))
				   lowerByFile(format(",".join(args.targetT)))

				   parsingTxtByFile(format(",".join(args.targetT)))
				   moveTxtByFile(format(",".join(args.targetT)))
				   cli_progress_test("Converting to TXT",100000, bar_length=20)	
				   sys.stdout.write("\n")
				   
				
					
						
		
if __name__ == '__main__':
	
	main(sys.argv[1:])

	
	
