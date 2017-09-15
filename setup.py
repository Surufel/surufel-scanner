# https://github.com/Surufel/surufel-scanner

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name = 'Surufel Scanner',

    version = '1.3',

    description = 'An AV for lab use',
    long_description = long_description

    url = 'http://www.surufel.com',

    author = 'Sifer Aseph'
    
)
