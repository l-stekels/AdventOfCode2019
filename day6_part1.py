from typing import NamedTuple
file = open('day6_input.txt')

example = [
'COM)B',
'B)C',
'C)D',
'D)E',
'E)F',
'B)G',
'G)H',
'D)I',
'E)J',
'J)K',
'K)L',
]

class Star(NamedTuple):
    name: str
    parentName: str

new = set([Star("A", None), Star("B", "A"), Star("C", "B")])

parent = [x for x in new if x.name == "A"]
parent.

# def parseMap(map):
#     # go through line by line each is aaa)bbb
#     for line in map:
#         parent, child = line.split(')')
        
            

# starObjects.parseMap()
