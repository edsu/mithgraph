#!/usr/bin/env python3

"""
This program fetches MITH's current project data from the research
explorer and saves the edge list of people and projects to data.csv
"""

import csv
import sys
import json

from urllib.request import urlopen

url = "http://mith.umd.edu/wp-content/mu-plugins/mith-research-explorer-data/projects.json"
projects = json.load(urlopen(url))

csv.writer(open("data.csv", "w"))
for project in projects:
    for member in project['member']:
        output.writerow([project['title'], member['name']])
