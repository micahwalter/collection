#!/usr/bin/env python

import sys
import json
import os
import os.path
import types
import utils
import sqlite3 as lite

import logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':

    whoami = os.path.abspath(sys.argv[0])

    bindir = os.path.dirname(whoami)
    rootdir = os.path.dirname(bindir)

    datadir = os.path.join(rootdir, 'objects')
    metadir = os.path.join(rootdir, 'meta')

    outfile = os.path.join(metadir, 'objects.sqlite3')

    con = None

    con = lite.connect(outfile)

    with con:

    	cur = con.cursor()
    	cur.execute("DROP TABLE IF EXISTS objects")
    	cur.execute("CREATE TABLE objects(id INT, description TEXT, url text)")

    	for root, dirs, files in os.walk(datadir):
			for f in files:
				path = os.path.join(root, f)
				logging.info("processing %s" % path)
			
				data = json.load(open(path, 'r'))
			
				object_id = data.get('id', [])
				description = data.get('description', [])
				url = data.get('url', [])
			
				cur.execute("INSERT INTO objects VALUES(?,?,?)" , (object_id, description, url)) 
			

		
logging.info("done");