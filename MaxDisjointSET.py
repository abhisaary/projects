##### Functions #####

# Returns lower case version of the char
def symb(char):
  if not char.isalpha():
      return symbDict[char]
  else:
    return char.lower()

# Returns the case/type of the char  
def case(string):
  if not string.isalpha():
    return 'sym'
  elif string.islower():
    return 'low'
  else:
    return 'high'

# Returns true if a set of three cards is a match
def match(card1, card2, card3):
  for i in range(4):
  	# For each attribute, if any two are the same, then it's not a SET
    if len(set([card1[i], card2[i], card3[i]])) == 2:
      return False
  return True

# Take a card in tuple form and compress it to original form
def compressCard(card):
  if card[2] == 'sym':
    char = symbDict[card[1]]
  elif card[2] == 'high':
    char = card[1].upper()
  else:
    char = card[1]
  return card[0] + ' ' + str(char)*card[3]

# Return all SETs that are disjoint from input SET
def disjointSETs(SETs, SET):
  results=[]
  for Set in SETs:
    if len(set(SET + Set)) == 6:
      results.append(Set)
  return results

# Recursive function returns longest branch of disjoint SETs
def maxdisSet(SETs):
  # If the number of sets is 0 or 1, return
  if len(SETs) <= 1:
    return list(SETs)
  # Take first set, and create a set of all disjoint SETs
  currSET = SETs[0]
  disjoint = disjointSETs(SETs[1:], currSET)
  # Run recursive function on the group of disjoint SETs
  left = [currSET] + maxdisSet(disjoint)
  # And on the rest of the SETs
  right = maxdisSet(SETs[1:])
  # Return larger set
  if len(left) >= len(right):
    return left
  else:
    return right

# Print to stdout a SET of three cards
def printSET(SET):
  print()
  for card in SET:
    print(compressCard(card))

# Test whether output is a valid disjoint set of SETs
def validSet(SETs):
  if len(set([x for y in SETs for x in y])) == 3*len(SETs):
    return "Valid Set"
  return "Not a Valid Set"

##### Read in Inputs #####

N = int(input())
cards = list()

# Define bi-directional dictionary to decode shading attribute 
symbDict = {'@': 'a', 'a': '@', '$': 's', 's': '$', '#': 'h', 'h': '#'}

# Create list of all cards with separated attributes
for i in range(N):
  a,b = input().strip().split()
  cards.append((a,symb(b[0]),case(b[0]), len(b)))

##### Find all Sets #####
 
SETs = list()
 
# For each distinct set of three cards, check whether they constitute a SET
for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if match(cards[i], cards[j], cards[k]):
        SETs.append((cards[i], cards[j], cards[k]))

numSETs = len(SETs)        
print(numSETs)
     
##### Find Maximum Disjoint Set #####

# Run recursive function and return max disjoint set
maxdisSETs = maxdisSet(SETs)
    
# Print to stdout  
print(len(maxdisSETs))

for SET in maxdisSETs:
  printSET(SET)