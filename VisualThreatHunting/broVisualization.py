# convert Bro conn logs in JSON format to graphviz files
import json


def createGraphviz(srcIP, destPort, protocol, destIP):
    with open("broViz.dat", "a+") as f:
        # a -> b[label="0.2"];
        # toString = "\t\"" + str(srcIP) + "\" -> \"" + str(destIP) + "\"[label=\"" + str(destPort) + "/" + str(protocol) + "\"];\n"
        toString = "\t\"" + str(srcIP) + "\" -> \"" + str(destIP) + "\";\n"
        f.write(toString)


fname = "conn.log"
outputFile = "broViz.dat"
with open(outputFile, "a+") as f:
    f.write("digraph {\n\trankdir=LR;\n")
with open(fname) as f:
    for line in f:
        parsed_json = json.loads(line)
        createGraphviz(parsed_json['id.orig_h'], parsed_json['id.resp_p'],
                       parsed_json['proto'], parsed_json['id.resp_h'])
with open(outputFile, "a+") as f:
    f.write("}")
# ouput pdf of visualization
cmd = "dot -Tpdf broViz.dat -o broViz.pdf"
Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
