import re

hdr = """---
title: 'numpy examples'
---
"""

def trans_examples(infn,outfn):
    """translate numpy .rst file to markdown format"""
    infile = open(infn,"r")
    outfile = open(outfn,"w")

    print(hdr,file=outfile)
    
    q = 0
    for L in infile:
        # find question statement
        if bool(re.search("^#\.",L)):
            # replace '#' with current question number
            L_out = re.sub("^#",str(q),L).strip()
            # get remainder of question
            while True:
                L_next = infile.readline().strip()
                if len(L_next)>0:
                    L_out += (" " + L_next)
                else:
                    break
            # output
            print(L_out,file=outfile)
            q += 1
    return(None)

