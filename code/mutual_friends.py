import MapReduce
import sys

mr = MapReduce.MapReduce()
friends=[]
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    current=[key,value]
    friends.append([key,value])
    
    for i in range(len(friends)):
        if len(friends)>1:
            if current[0] in friends[i][1] and friends[i][0] in current[1]:
                if [val for val in current[1] if val in friends[i][1]]!=[]:
                    mr.emit_intermediate(current[0]+"-"+friends[i][0],[val for val in current[1] if val in friends[i][1]])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for i in range(len(list_of_values)):
        mr.emit((key, list_of_values[i]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

