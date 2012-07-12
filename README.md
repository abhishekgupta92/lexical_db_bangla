Lexical Database Bangla
=======================
Automatic construction of lexical database for Bangla inspired from Wordnet using a bilingual dictionary and Wordnet.

Usage
=====
1. Download the package.

		python setup.py install
		
2. In your python code

		import lexical_db_bangla
		syns_set=lexical_db_bangla.syns(word)
		print syns_set

where word is any bangla word.
		
Approach
========
For each Bangla word in the billingual (bangla to english dictionary), we need to look up all possible English words. Then we out find out the synsets for those English words from Princeton WordNet, extract the whole network of those synsets and copy that to our target wordnet for Bangla. Then, we try to translate the structure where ever possible, like name of the features attached with each word/synset, the features of these words and of course the actual words into Bangla.

Note
====
The bangla to bangla dictionary have already been generated which is then parsed and used to find the synonymns. You can also generate the same using read_dict.py file. Also, remember the file has a really high memory footprint.
Dumps in the folder english_bangla_datasets have been downloaded from http://www.bengalinux.org/english-to-bengali-dictionary/dumps/. The license for the same can be found in the folder in the file Copying.txt

### Dependencies:
----------------

* [Python] (http://www.python.org)
* [NLTK Library] (http://www.nltk.org)
* Numpy Library (required by nltk)
* NLTK Corpora

After you have installed the NLTK Library, do the following to download the NLTK Corpora:

1. Go to your python shell. Type:

        nltk.download()

2. Download 
   * **Wordnet** Corpora