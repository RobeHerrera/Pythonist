import sys
argument_list = sys.argv
print("The script has the name: ", "",(sys.argv[0]),"")
print("The number of the arguments is: ",(len(sys.argv)) )
print("The Arguments are", argument_list)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-display")
args = parser.parse_args()
print("args sin vars: " ,args)

args = vars(parser.parse_args())
print("args con vars: ",args)

# print(args.display)

number = 1
if len(sys.argv)==2:
    number = int(sys.argv[1])
    
for i in range(number):
    print("Hello world")       

