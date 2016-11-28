# visualization
This repo contains scripts i created to visualize different types of data

- translateToGraphviz.py
 - This script contains steps to visually represent your PAN configuration with graphviz
    1. Export pan config to csv
     1. https://indeni.com/how-to-export-palo-alto-networks-firewalls/
     2. column headers
        1. name, to, from, source, destination, source-user, category, application, service, hip-profiles, tag, action, description, group, log-setting, disable-server-response-inspection, log-start, log-end, negate-source, negate-destination, disabled, rule-type
    2. make sure the policies.csv file you end up with is in the same directory as the python scripts
    3. run translateToGraphviz.py
      1. usage: python translateToGraphviz.py
    4. install graphviz
      1. http://www.graphviz.org/
    5. open .dot file with graphviz
