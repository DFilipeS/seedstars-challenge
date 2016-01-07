#!/usr/bin/env python

import sys
import ast
import urllib
import sqlite3

JENKINS_BASE_URL = "https://jenkins.qa.ubuntu.com"

def main():
    # Retrieve the data from the Jenkins instance
    jenkins_data = ast.literal_eval(urllib.urlopen(JENKINS_BASE_URL + "/api/python?tree=jobs[name,color]").read())
    
    con = sqlite3.connect("jobs-status.db")
    with con:
        cursor = con.cursor()
        
        # Create table on the SQLite database, if it does not exists
        cursor.execute("CREATE TABLE IF NOT EXISTS status(id INTEGER PRIMARY KEY AUTOINCREMENT, job TEXT, status TEXT, timestamp TEXT)")
        
        for job in jenkins_data['jobs']:
            # Print to the console the jobs and their status
            print job['name'] + " - " + job['color'] 
            
            # Store in the SQLite database the current job, status and current timestamp
            cursor.execute("INSERT INTO status(job, status, timestamp) VALUES(?, ?, datetime('now'))", (job['name'], job['color']))
            
        print "Total jobs: " + str(len(jenkins_data['jobs']))
        
if __name__ == "__main__":
    main()