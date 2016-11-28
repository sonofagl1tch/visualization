#!/usr/bin/python
'''
Author: Ryan Nolette
Date Modified: 11/26/2016
#############################
Steps to visually represent your PAN configuration
1) Export pan config to csv
    https://indeni.com/how-to-export-palo-alto-networks-firewalls/
    column headers
        name, to, from, source, destination, source-user, category, application, service, hip-profiles, tag, action, description, group, log-setting, disable-server-response-inspection, log-start, log-end, negate-source, negate-destination, disabled, rule-type
2) make sure the policies.csv file you end up with is in the same directory as the python scripts
3) run translateToGraphviz.py
    usage: python translateToGraphviz.py
4) install graphviz
    http://www.graphviz.org/
5) open .dot file with graphviz
'''
import time #simple timestamping module
import csv #csv interaction module
#from subprocess import call #allows for

#create file to write out to
def createOutputFile():
    file = open( filename, "a" )
    file.write( "digraph d {\n" )
    file.close()

#close file to write out to
def closeOutputFile():
    file = open( filename, "a" )
    file.write( "}" )
    file.close()

#write formatted output to file
def appendToFile(  input  ):
    file = open( filename, "a" )
    file.write( input + "\n")
    file.close()

#read in csv of data
def readInput():
    with open( './policies.csv', 'rU' ) as f:
        reader = csv.reader( f )
        #skip header row
        reader.next()
        for item in reader:
            #add each line to list
            firstList = list( item )
            #send list to get formatted
            format( firstList )
            #print firstList[0]

def format(  input = [] ):
    '''
    PAN headers list locations that i care about for this usage
        0 - name
        1 - to
        2 - from
        3 - source
        4 - destination
        7 - application
        8 - service
        11 - action
    ###################
    format for graphviz
        to/source -> from/destination [ label="application/service/action" ];
    '''
    inputString = "\"" + str(input[1]) + "/" + str(input[3]) + \
                    "\" -> \"" + str(input[2]) + "/" + str(input[4]) + \
                    "\" [ label=\"" + str(input[7]) + "/" + \
                    str(input[8]) + "/" + str(input[11]) + "\" ];"
    appendToFile( inputString )

# def convertToDOT():
#     call(["dot", "-Tpng -O " + filename])

################################################
#create timestamp
timestr = time.strftime( "%Y%m%d-%H%M%S" )
#create filename
filename = "firewall_" + timestr + ".dot"
#run application
createOutputFile()
readInput()
closeOutputFile()
#convertToDOT()
