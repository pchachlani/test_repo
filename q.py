#!/usr/bin/python
import re

line2="99.101.82.115 - - [15/Apr/2019:13:43:26 -0400] \"GET /my-module/views/app_main/user_dashboard.html HTTP/1.1\""

print("match the IP address")
matchObj = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line2)
if matchObj:
    print ("matchObj.group(0) : ", matchObj.group(0))
    print ("matchObj.group(1) : ", matchObj.group(1))
    print

print("match the date/time")
matchObj = re.search(r"\[(.*)\]", line2)
if matchObj:
    print ("matchObj.group(0) : ", matchObj.group(0))
    print ("matchObj.group(1) : ", matchObj.group(1))
    print

print("match the IP address and date/time")
matchObj = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) .* \[(.*)\]", line2)
if matchObj:
    print ("matchObj.group(0) : ", matchObj.group(0))
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
    print
