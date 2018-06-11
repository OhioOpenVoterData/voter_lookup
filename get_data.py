import os
from . import index_voters

#assert not os.system('apt-get install libxapian-dev python-xapian git zip')
assert not os.system('wget --no-check-certificate -O SWVF1.gz "https://www6.sos.state.oh.us/ords/f?p=VOTERFTP:DOWNLOAD::FILE:NO:2:P2_PRODUCT_NUMBER:363"')
assert not os.system('wget --no-check-certificate -O SWVF2.gz "https://www6.sos.state.oh.us/ords/f?p=VOTERFTP:DOWNLOAD::FILE:NO:2:P2_PRODUCT_NUMBER:364"')
assert not os.system('wget --no-check-certificate -O SWVF3.gz "https://www6.sos.state.oh.us/ords/f?p=VOTERFTP:DOWNLOAD::FILE:NO:2:P2_PRODUCT_NUMBER:365"')
assert not os.system('wget --no-check-certificate -O SWVF4.gz "https://www6.sos.state.oh.us/ords/f?p=VOTERFTP:DOWNLOAD::FILE:NO:2:P2_PRODUCT_NUMBER:366"')
assert not os.system('for p in SWVF*.gz ; do gunzip $p ; done')
assert not os.system('rm -f *.gz')
assert not os.system('for i in SWVF* ; do mv $i $i.csv ; done')

index_voters.main()
