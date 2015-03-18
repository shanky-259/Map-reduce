import MapReduce
import sys

mr = MapReduce.MapReduce()

friends=[]
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    value=sorted(value)
    for index in range(len(value)):
        if sorted([key,value[index]]) in friends:
            mr.emit_intermediate(key, value[index])
        else:
            friends.append(sorted([key,value[index]]))
    

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for index in range(len(list_of_values)):
        mr.emit((key,list_of_values[index]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
