#!/bin/bash

[ -d downloads ] || mkdir downloads
wget --no-check-certificate -O - "https://www6.sos.state.oh.us/ords/f?p=VOTERFTP:DOWNLOAD::FILE:NO:2:P2_PRODUCT_NUMBER:363" | gunzip -c > downloads/SWVF1.csv
wget --no-check-certificate -O - "https://www6.sos.state.oh.us/ords/f?p=VOTERFTP:DOWNLOAD::FILE:NO:2:P2_PRODUCT_NUMBER:364" | gunzip -c > downloads/SWVF2.csv
wget --no-check-certificate -O - "https://www6.sos.state.oh.us/ords/f?p=VOTERFTP:DOWNLOAD::FILE:NO:2:P2_PRODUCT_NUMBER:365" | gunzip -c > downloads/SWVF3.csv
wget --no-check-certificate -O - "https://www6.sos.state.oh.us/ords/f?p=VOTERFTP:DOWNLOAD::FILE:NO:2:P2_PRODUCT_NUMBER:366" | gunzip -c > downloads/SWVF4.csv
mv downloads/SWVF1.csv downloads/voterfile.csv
tail -n+2 downloads/SWVF2.csv >> downloads/voterfile.csv
tail -n+2 downloads/SWVF3.csv >> downloads/voterfile.csv
tail -n+2 downloads/SWVF4.csv >> downloads/voterfile.csv
