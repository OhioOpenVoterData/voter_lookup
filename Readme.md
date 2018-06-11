Start a machine running ubuntu 16

sudo bash apt-get update apt-get install python-xapian git python-pip pip install cherrypy
git clone https://github.com/coventry/voter_lookup mkdir voter_lookup/data cd voter_lookup/data export PYTHONPATH=~ python -m voter_lookup.get_data python -m voter_lookup.index_voters python -m voter_lookup.serve 80 
