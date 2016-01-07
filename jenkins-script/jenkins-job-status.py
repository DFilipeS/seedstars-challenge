#!/usr/bin/env python

import sys
import ast
import urllib

from datetime import datetime

JENKINS_BASE_URL = "https://jenkins.qa.ubuntu.com"
#JENKINS_BASE_URL = "http://192.168.10.10:8080"

def main():
    jenkins_data = ast.literal_eval(urllib.urlopen(JENKINS_BASE_URL + "/api/python?tree=jobs[name,color]").read())
    current_time = str(datetime.now()) # Get the current time string once and use it when it is necessary
    
    for job in jenkins_data['jobs']:
        print "(" + current_time + ") " + job['name'] + " - " + job['color']
    
if __name__ == "__main__":
    main()