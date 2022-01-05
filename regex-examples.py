#!/usr/bin/env python3

import re


pattern1 = "world"
strz = "Lets go world"
result1 = re.search(pattern1, strz)


           #here
pattern = re.compile(r"here")
sentence = "Hello world I am here"



if result1:
  print("yass queen")
  print(result1)
  print(strz[8:13])
else:
  print("oopsies")