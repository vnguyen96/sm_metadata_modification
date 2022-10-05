#!/usr/bin/python3
import os
import re
import pandas as pd
import csv
import time

comma = r', '
single_quote = '\''
dockerptn = r'docker exec -it stream-manager-suite_stream-manager-service_1 mysql -uroot --password=password -D streamManagerdb -e '
psql1 = r'"UPDATE Stream_Metadata SET jurisdiction= '
route_name = 'route_name= \''
mile_marker = 'mile_marker= \''
traffic_direction = 'traffic_direction= \''
latitude = 'latitude= \''
longitude = 'longitude= \''
name = 'name= \''
metadata_add = open("metadata_add_script.sh", "wt")

csv_file = input("Enter CSV File Location:")
with open(csv_file) as cam_info:
    csv_reader=csv.DictReader(cam_info,delimiter=',')
    line_count=0
    for row in csv_reader:
        combine = dockerptn + psql1 + single_quote + row['jurisdiction'] + single_quote + comma + route_name + row['route_name'] + single_quote + comma + mile_marker + row['mile_marker' ] + single_quote + comma + traffic_direction + row['traffic_direction'] + single_quote + comma + latitude + row['latitude'] + single_quote + comma + longitude + row['longitude'] + single_quote + ' WHERE ' + name + row['name'] + single_quote + '"' + '\n'
        metadata_add.write(combine)
    print('metadata_add_script.sh has been created')