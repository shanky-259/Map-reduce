# Map-reduce
This repository contains some simple applications of a basic MapReduce framework built in python.

The Mapreduce.py file is a basic MapReduce framework which demonstrates how a MapReduce
algorithm works in a real environment.The 7 other .py files use this MapReduce framework
to perform distributed computing in a virtual sense.The mappers(one or more machines) 
work in parallel to reduce the computation time and workload which would otherwise be 
handled by a single machine.The output from the mapper is fed to the reducers by the 
MapReduce framework which emits the result by performing the required action on a key and 
its values.
