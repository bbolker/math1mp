import re

def trans_examples(infn,outfn):
    infile = open(infn,"r")
    outfile = open(outfn,"w")

    q = 0
    for L in infile:
        if bool(re.search("^#\.",L)):
            L_out = re.sub("^#",str(q),L).strip()
            while True:
                L_next = infile.readline().strip()
                if len(L_next)>0:
                    L_out += (" " + L_next)
                else:
                    break
            print(L_out,file=outfile)
            q += 1
    return(None)

