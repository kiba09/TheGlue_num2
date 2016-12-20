#! /usr/bin/env python

import subprocess
import tempfile
#import threading
#import Queue
import zlib
import base64

def grab_dir(dir,keyword):
	new_index = []

	with tempfile.TemporaryFile() as tempf:
		proc = subprocess.call(("find %s -name '*%s*' "%(dir,keyword)),stdout=tempf,shell=True)

		tempf.seek(0)
		new_index = str(tempf.read()).split(":")
	#print new_index
	return new_index #this will be the data of dirs which bear the keyword's name

def grab_text(dir,keyword,include_file):
	
	#if we want to include only a spesific file then
	# time(sudo find Downloads -name '*apple*' && grep 'apple' --max-count=1 -raInbow --include=*.js Downloads)
	
	if include_file != '':
		include_file = ' '.join([('--include=*.%s'%x) for x in include_file.split(',') ])
	
	print "this is the file pattern"
	print ("grep '%s' --max-count=1 -raInbow %s %s "%(keyword,include_file,dir))
	with tempfile.TemporaryFile() as tempf:
		proc = subprocess.call(("grep '%s' --max-count=1 -raInbow %s %s"%(keyword,include_file,dir)),shell=True,stdout=tempf)
		tempf.seek(0)
		new_index = str(tempf.read())
		
	#.split("\n")
	parsed = ''
	for i in new_index:
		parsed += i
		
	import re

	
	return str(parsed).split("\n") #this will be the data of files that contains the keyword

def quick(dir,keyword):subprocess.call("find %s -name '*%s*' && grep '%s' --max-count=1 -raInbow %s"%(dir,keyword,keyword,dir),shell=True)	



def write_html(indexer,dir,key):
	print "####################################"
	print "GENERATING HTML RESULT SCRIPTS"
	print "####################################"
	get_files = ''
	get_texts = ''
	get_array_of_texts = [] #instead of get_texts = ''
	container = '<html><head><title></title></head><body>'
	len_text = 0
	len_file = 0
	tap,tap2 = '',''

	#try:
	for files in indexer.keys():
		f_key = indexer[files]
		if files == dir:
			for genkey in f_key:
				for gkeyword in genkey.keys():
					keyresult = genkey[gkeyword]
					for keyss in keyresult.keys():
						if keyss == key:
							carries = keyresult[keyss]
							for i in carries.keys():
								j = carries[i] 
								if i == 'files': 									
									for last in j:
										get_files += ('<b style="color:green;">file :</b><br> @ %s<br>'%last)
										tap2 += ("FILE: \n@ %s"%last)
										
										if last != '':
											len_file += 1
								elif i == 'texts':
									for last in j:
										get_array_of_texts.append(last)	
								else: pass
	def parse_text(get_texts,keyword):
		count_text = 0
		res = ''		

		for j in get_texts:
			if key in j:
				j = j.split(":")
				print j
				try:
					res += ("<br><b style='color:red;'>text</b>: <br>@ from file : %s <br> @ line %s <br> @ with byte-ofset and text found : %s %s<br>"%(j[0],j[1],j[2],j[3]))			
					#alter += ("TEXT: \n@ from file : %s\n @ line %s\n %s %s\n\n ")
				except:
					res += ("<br><b style='color:red;'>text </b>: <br>@ from file : %s <br> @ line %s <br>@ with byte-ofset and text found : %s<br>"%(j[0],j[1],j[2]))
					#alter += ("TEXT: \n@ from file : %s\n @ line %s\n %s\n @with text found : %s\n\n")			
				
				count_text += 1
		return res,count_text,tap
	#except:
	#	print "cant do that"
	#	return '',0 #if no results found in the indexer then it would return nothing!

	get_texts,len_text,tap = parse_text(get_array_of_texts,key)
		 


	container += ("<h2>From the directory <b style='color:purple;'>'%s'</b> with a keyword of <b style='color:purple'>'%s'</b></h2>"%(dir,key))
	container += ("<h3>over %s found</h3> :<br> "%(len_text+len_file))
	container += ("<b style='color:green;'>files</b> : %s"%(len_file))
	container += (", <b style='color:red;'>  texts</b>: %s<br><br>"%(len_text))
	container += get_files
	container += get_texts
	container += "</body></html>"		
	
	
	print "this is the container %s"%container				

	filer = open("result.html",'wb')
	filer.truncate()
	filer.write(container)
	filer.close()	
	



def display_results(keyword,dir,indexer):
	''' will display the result of the given keyword '''
	
	from index import indexer
	


def force_alter(keyword,dir,indexer):

	''' if a new file will create in that certain directory it
		will cause the indexer to foce-update itself to be able to
		find if the newfile is actually a result of a given keyword '''

	pass


def write_index(nis):

	up_file = open('index.py','wb')
	up_file.truncate()
	up_file.write("#! /usr/bin/env python")
	up_file.write("# -*- coding: utf-8 -*-")
	up_file.write("\n")
	up_file.write("''' Author: King Bernabe '''")
	up_file.write("''' updated dictionary file '''")
	up_file.write("\n\n")
	up_file.write(nis)
	up_file.close()


def construct_index(indexer,dir,key):
	#plotting the file
	nis = "indexer = {"
	for i_file in indexer.keys():
		i_keyw = indexer[i_file]
		nis += ('\n\t "%s" :[ '%i_file)	
		for i_k in i_keyw:
			nis += ('\n\t {')
			#nis += ('\n\t\t "%s" : {'%i_k)
			for gen_k in i_k.keys():
				name_k = i_k[gen_k]
				nis += ('\n\t\t\t "%s" : {\n'%gen_k)
				for n_k in name_k.keys():
					nis += ('\n\t\t\t\t "%s" : {\n'%n_k)
					prop = name_k[n_k]
					for i_prop in prop.keys():
						nis += ('\t\t\t\t\t "%s" : [\n'%i_prop)
						elements = prop[i_prop]
						for lest in elements:
							if lest is not "":
								nis += ("\t\t\t\t\t   '''%s''',\n"%lest)
								#nis += base64.encodestring(zlib.compress(str(nis)))
						nis += "\t\t\t\t\t  ],\n"
					
					nis += "\n\t\t\t\t},"
				
				nis += "\n\t\t\t},"
			nis += "\n\t\t},"
		nis += "\n\t],"
	nis += "\n}"
	return nis

def display_warning():
	print "[+] Invalid Given Directory or Host"
	print "Make sure the directory is here"
	print "Make sure that the key is in the directory"
	sys.exit()

def check_key_in_doc(key,dir,indexer):

	detect_key = False
	detect_dir = False
	is_key_in_dir = False
	
	#detecting the directory
	try:
		if dir in indexer.keys():
			detect_dir = True
			for i_file in indexer.keys():
				gen_key = indexer[i_file]
				#print "this is the gen %s"%gen_key
				for g_k in gen_key:
					for n_k in g_k.keys():
						i_keyw =  g_k[n_k]
						for k in i_keyw.keys():
							#print "the dir is %s and key is %s"%(i_file,k)
							if i_file == dir and k == key:
								#print "the pattern has been detected"
								is_key_in_dir = True
							
	except:pass			
	
	#detecting the key in the directory
	for i_dir in indexer.keys():
		here = indexer[i_dir]
		for i_files in here:
			for i_key in i_files.keys():
				i_key = i_files[i_key]
				for i_k in i_key.keys():
					if i_k == key:
						detect_key = True
	
	return detect_key,detect_dir,is_key_in_dir
	
if __name__== '__main__':
	#try:
		import sys
		from index import indexer
		import uuid
		enable_html = False	
		try:
			dir = sys.argv[1]#"thefile"
			key = sys.argv[2]#"lapis"
			
			
			if sys.argv[-1] != '':
				include_file = sys.argv[3]
			else:
				include_file = ''
			
			generated_key = 'key-' + str(uuid.uuid1())
		except: display_warning()

		
		checked_key,checked_dir,pattern_checked = check_key_in_doc(key,dir,indexer)
		
		
		print "key %s"%checked_key
		print "directory %s"%checked_dir
		print "pattern %s"%pattern_checked

		if checked_key == True and checked_dir == True and pattern_checked:
			print "[+]Using option number 1"
			print "key and dir detected in the index"
			display_results(key,dir,indexer)
			enable_html= True
		elif ((checked_key == True and checked_dir == False)) and pattern_checked == False:
			"###################initialize finding procedure #######################"
			try:
				k_t,k_d = grab_text(dir,key,include_file),grab_dir(dir,key)
				
			except:
				print "FALSE FALSE"
				display_warning()
			"#######################################################################"
			print "[+]Using option number 2"

			new_index = {generated_key:{ key : { 'files':k_d,
								'texts':k_t,
								'contains':[str(len(k_d)),str(len(k_t))],
									
									},
									},
								}
			#indexer[dir].append(new_index)
		
			indexer.update({dir:[new_index]})
		
			#this is were the indexer is being construct and write
			indexer = construct_index(indexer,dir,key)
			write_index(indexer)
			enable_html = True 
			
		elif ((checked_key == False and checked_dir == True) or(checked_key == False and checked_dir == False) or (checked_key == True and checked_dir == True)) and pattern_checked == False:
			"###################initialize finding procedure #######################"
			try:
				k_t,k_d = grab_text(dir,key,include_file),grab_dir(dir,key)
		
			except: 
				print "FALSE TRUE"
				display_warning()
			"#######################################################################"
			print "[+]Using option number 3"

			put_in_force = False 
			new_index = {generated_key:{ key : { 'files':k_d,
										'texts':k_t,
										'contains':[str(len(k_d)),str(len(k_t))],
											
											},
											},
										}
			if checked_dir == False:
				indexer[dir]=[]
			
			indexer[dir].append(new_index)
			
			#this is were the indexer is being construct and write
			indexer = construct_index(indexer,dir,key)
			write_index(indexer)
			enable_html = True
			
		else:display_warning();enable_html = False	
		print "enable html status !!! %s"%enable_html
		if enable_html == True:
			print "write_html"
			write_html(indexer,dir,key)
	#except:
	#	print "[+] type of ecoding problem : cant display result from html, "	
	#	print "but the index is already create, feel free to see the result in the index.py"
	#	import sys
	#	from index import indexer
	#	import uuid
	#	enable_html = False	
	#	try:
	#		dir = sys.argv[1]#"thefile"
	#		key = sys.argv[2]#"lapis"
	#		sa_inc = sys.argv[3] or ''#"if we want to include *"
	#		generated_key = 'key-' + str(uuid.uuid1())
	#		try:
	#			include_file = sys.argv[3]
	#		except:
	#			include_file = ''
	#	except: display_warning()
	#	quick(dir,key)
