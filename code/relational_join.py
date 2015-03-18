import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line
def mapper(record):
    # key: document identifier
    # value: document contents
    value = record
    if value[0]=='MovieNames':
      mr.emit_intermediate(value[2], value[1:])
    else:
      mr.emit_intermediate(value[1], value[1:])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    sum_r=0
    for j in range(len(list_of_values)-1):
        longlist=[]
        longlist.extend(list_of_values[0])
        longlist.extend(list_of_values[j+1][:])
        mr.emit(longlist)
    for i in range(len(list_of_values)-1):
        sum_r+=list_of_values[i+1][-1]
    mr.emit((list_of_values[0][0],sum_r/float((len(list_of_values)-1))))
            

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
