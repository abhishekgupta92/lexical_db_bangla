from xml.dom.minidom import parse

debug=True

#parse ankur-abhidhan.xml
fileName="english_bangla_datasets/ankur-abhidhan.xml"
dom=parse(fileName)
#define rows as element under row
rows=dom.getElementsByTagName("row")
#creates an array
eng_bangla_dictionary={}
bangla_eng_dictionary={}

'''
Sample Entry

	<row>
		<field name="id">80142</field>
		<field name="en_word">cooch.behar</field>
		<field name="pos_tag">NP</field>
		<field name="en_lemma"></field>
		<field name="bn_pronunciation"></field>
		<field name="bn_word">কুচবেহার</field>
		<field name="explanation"></field>
		<field name="example"></field>
		<field name="status">UNEDITED:TIME=1280170484:NEW_ENG_WORD</field>
	</row>
'''

#Parse the xml into the dictionary eng_bangla_dictionary structure, which will be used later.
for row in rows:
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
				if debug:
					print en_word
			elif f.getAttribute("name")=="pos_tag":
				pos_tag=f.childNodes[0].toxml()
				if debug:
					print pos_tag
			elif f.getAttribute("name")=="bn_word":
				bn_word=f.childNodes[0].toxml()
				if debug:
					print bn_word
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

if debug:
	fileName="dictionaries/eng_to_bangla.txt"
	fwrite=open(fileName,'w')
	lines=[]
	#Write the contents in the file
	for key in eng_bangla_dictionary.keys():
		value=eng_bangla_dictionary[key]
		lines.append(str(key)+";"+str(value)+"\n")

	fwrite.writelines(lines)
	fwrite.close()

#print eng_bangla_dictionary
#print bangla_eng_dictionary

'''
nltk.download()
- install wordnet

.similar (google, nltk)

synsets

go to wordnet wali directory
-> start writing code to prepare an identical bangla wordnet

tweak, nltk to be able to use the new bangla wordnet
'''
	
