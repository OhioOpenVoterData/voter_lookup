#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy, os, sys, json

current_dir = os.getcwd()

path = os.path.dirname(current_dir)
if path not in sys.path:
    sys.path.append(path)

from voter_lookup import query, counties

class Root(object):

    _cp_config = {'tools.staticdir.on' : True,
                  'tools.staticdir.dir' : os.path.join(current_dir, 'static'),
                  'tools.staticdir.index' : 'index.html',
    }

    @staticmethod
    def qualified(voter):
        primaries = [v for k, v in voter.items() if k.startswith('PRIMARY') and
                     k.split('/')[-1] in '2013 2014 2015'.split()]
        # Voters are qualified  if they voted in a dem  primary in the
        # last two years, or if they voted in no other primaries.
        return 'D' in primaries or all(p in ('', 'X') for p in primaries)

    def affiliation(voter):
        return voter['PARTY_AFFILIATION']

    headings = [
        #('D', lambda v: "&#x2713;" if Root.qualified(v) else ""),
        ('Precinct', lambda v: v['PRECINCT_NAME']),
        ('County', lambda v: counties.abbrevs[int(v['COUNTY_NUMBER'])-1]),
        ('CD', lambda v: v['CONGRESSIONAL_DISTRICT']),
        ('Name', lambda v: '%s %s' % (v['FIRST_NAME'], v['LAST_NAME'])),
        ('Address', lambda v: '%s %s' % (v['RESIDENTIAL_ADDRESS1'], v['RESIDENTIAL_ZIP'])),
        ]

    @cherrypy.expose
    def lookup(self, **kw):
        active_element = kw.pop('active_element')
        reqnum = kw.pop('reqnum')
        values = dict((k, v) for k, v in kw.items() if v != '')
        results = query.search(values, active_element)
        print results
        headings = ['<th>%s</th>' % h for h in zip(*self.headings)[0]]
        rows = [['<td>%s</td>' % f(v) for h, f in self.headings] for v in results]
        body = ['<tr>%s</tr>' % ''.join(r) for r in [headings] + rows]
        table_preamble = '<table class="pure-table pure-table-striped">'
        table = [table_preamble, ''.join(body), '</table>']
        return json.dumps(dict(result=''.join(table), reqnum=reqnum))

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': int(sys.argv[1]),
                            'server.socket_host': '192.168.1.132'})
    cherrypy.quickstart(Root())
        
