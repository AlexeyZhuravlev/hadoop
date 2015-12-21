#!/bin/bash

javac -cp /usr/lib/hadoop/hadoop-common.jar:/usr/lib/hadoop-mapreduce/hadoop-mapreduce-client-core.jar -d . ./WordCount.java
jar cf WordCount.jar -C . ru
