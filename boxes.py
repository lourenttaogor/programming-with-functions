#boxes
#import math module
import math

manufactured_boxes = int(input("Number of manufactured items "))
pack_per_box = int(input("Number of items per box "))

result = manufactured_boxes / pack_per_box

print(f"For {manufactured_boxes} items, packing {pack_per_box} in each box, you will need {math.ceil(result)} boxes")
