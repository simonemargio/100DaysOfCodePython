#  Created by Simone Margio
#  www.simonemargio.im

# Problem: parse the following JSON to get all the values of a key ‘key’ within an array
# Input: json below
# Output: ['key 1', 'key 2', 'key 3']


import json

json_data = """[ 
   { 
      "id":1,
      "key":"key 1",
      "other":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "key":"key 2",
      "other":[ 
         "pink",
         "yellow"
      ]
   },
   { 
      "id":3,
      "key":"key 3",
      "other":[ 
         "black",
         "white"
      ]
   }
]"""

data = []
try:
    data = json.loads(json_data)
except Exception as e:
    print(e)

dataList = [item.get('key') for item in data]
print(dataList)