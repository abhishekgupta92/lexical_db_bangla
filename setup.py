#!/usr/bin/env python

import sys
from distutils.core import setup

sys.argv=[sys.argv[0],'install']

setup(name='Lexical Database for Bangla',
      version='1.0',
      description='Lexical Database for Bangla based on Wordnet and a bilingual dictionary',
      author='Abhishek Gupta',
      author_email='abhishekgupta.iitd@gmail.com',
      url='http://github.com/abhishekgupta92/lexical_db_bangla',
      py_modules=['bangla_dict'],
      package_dir={'data':'bangla_dicts'},
      package_data={'data': ['bangla.dict']},
     )