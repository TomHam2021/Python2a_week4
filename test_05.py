import argparse
'''
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
args = parser.parse_args()

print('Hello,', args.name)
# för att köra filen, använd terminalen nedan
# skriv : python test_05.py --name Henry
# och svaret blir: Hello, Heny
'''


parser = argparse.ArgumentParser()
parser.add_argument("-x", "--valueX", type=int, help="Set the value for x")
parser.add_argument("-y", "--valueY", type=int, help="Set the value for y")
parser.parse_args()
args = parser.parse_args()
print("Sum of x and y:", args.valueX + args.valueY)

# >> test_05.py -h
# så får man hjälp hur man ska köra filen
# >> python test_05.py -x "5" -y 4
# ger output:
# >> Sum of x and y: 9
