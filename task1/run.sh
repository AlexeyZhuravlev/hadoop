#!/bin/bash

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input "input" -output "output" -mapper "mapper.py" -reducer "reducer.py" -file /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -file mapper.py -file reducer.py -numReduceTasks 1
