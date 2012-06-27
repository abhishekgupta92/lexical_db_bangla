fileDict="bangla_dicts/bangla.dict"

def sample_parser(fileName):
	fread=open(fileName)
	lines=fread.readlines()
	fread.close()
	
	bangla_dict={}

	for line in lines:
		key=line.split(';')[0]
		value=line.split(';')[1].split(",")
		bangla_dict[key]=value
	
	return bangla_dict
	
sample_parser(fileDict)