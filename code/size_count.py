import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    content=""
    sizelist=[]
    key = record[0]
    value = record[1]
    tmp=["large","medium","small","tiny"]
    for index in range(len(tmp)):
        sizelist.append([])
        sizelist[index].append(tmp[index])
        sizelist[index].append(0)
    for w in value:
        content+=w
    words = content.split()
    for w in words:
        if len(w)>=10:
            sizelist[0][1]+=1
        elif len(w)<10 and len(w)>=5:
            sizelist[1][1]+=1
        elif len(w)<5 and len(w)>=2:
            sizelist[2][1]+=1
        elif len(w)<2 and len(w)>=1:
            sizelist[3][1]+=1
        else:
            continue
    mr.emit_intermediate(key,sizelist)

def reducer(key, sizelist):
    # key: word
    # value: list of occurrence counts
    for index in range(len(sizelist)):
        mr.emit((key,sizelist[index]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
