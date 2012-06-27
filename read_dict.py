from xml.dom.minidom import parse
from nltk.corpus import wordnet

#parse ankur-abhidhan.xml
fileName="english_bangla_datasets/ankur-abhidhan.xml"
fileDict="bangla_dicts/bangla.dict"

debugMode=True

bangla_dict={}
eng_bangla_dictionary={}
bangla_eng_dictionary={}

dom=parse(fileName)
print "Parsed the XML file"

rows=dom.getElementsByTagName("row")

#Parse the xml into the dictionary eng_bangla_dictionary structure, which will be used later.
for row in rows:
	try:
		fields=row.getElementsByTagName("field")
		entry=False
		for f in fields:
			if f.getAttribute("name")=="status":
				if f.childNodes[0].toxml() != "EMPTY" or f.childNodes[0].toxml()!='OBSOLETE':
					entry=True
				
		if entry:
			for f in fields:
				if f.getAttribute("name")=="en_word":
					en_word=f.childNodes[0].toxml()

				elif f.getAttribute("name")=="pos_tag":
					pos_tag=f.childNodes[0].toxml()

				elif f.getAttribute("name")=="bn_word":
					bn_word=f.childNodes[0].toxml()

			#specifies key and value for dictionary
			key=en_word
			value=(pos_tag,bn_word)

			#Check if the key already exists or not. If it does append the value, else intialize the array as well.
			if eng_bangla_dictionary.has_key(key)==False:
				eng_bangla_dictionary[key]=[]
			eng_bangla_dictionary[key]=value
		
			key=bn_word
			value=(pos_tag,en_word)

			#Check if the key already exists or not. If it does append the value, else intialize the array as well.
			if bangla_eng_dictionary.has_key(key)==False:
				bangla_eng_dictionary[key]=[]
			bangla_eng_dictionary[key]=value
	except:
		pass

print "Parsed the Bilingual dictionary into two dictionary structures"

#For all Bangla words in bangla to english dictionary
for i,bn_word in enumerate(bangla_eng_dictionary.keys()):
		bn_syns=[]
		
		#Find corresponding English Word
		(pos_tag,en_word)=bangla_eng_dictionary[bn_word]

		#Find synyonyms in English
		syns1=[l.name for s in wordnet.synsets(en_word) for l in s.lemmas]
		
		#Remove the duplicates, and the key itself.
		syns=list(set(syns1))
		try:
			syns.remove(en_word)
		except:
			pass
			
		#Wordnet.synset(en_word+".n.01").lemma_names

		#Find Bangla Equivalent of the synonyms from the dictionary
		for s in syns:
			try:
				bword=eng_bangla_dictionary[s]
				#^^ returns a tuple (pos_tag,bn_word)
				bn_syns.append(bword[1])
			except:
				pass

		#key=bn_word
		#value=bn_syns
		if bn_syns != []:
			bangla_dict[bn_word]=bn_syns
		#if i>20:
		#		break

print "Prepared the dictionary."
print "Number of words in the dictionary are",len(bangla_dict.keys())

fwrite=open(fileDict,'w')
lines=[]
for key in bangla_dict.keys():
	syns=bangla_dict[key]
	
	if not syns:
		continue

	syns=map(lambda s:s.encode('utf-8'),syns)
	value=",".join(syns)
	lines.append(str(key.encode('utf-8'))+";"+value+"\n")

fwrite.writelines(lines)
fwrite.close()