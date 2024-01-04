from array import array
Die_A = [1,2,3,4,5,6]
Die_B = [1,2,3,4,5,6]
# print function to print elemente in new line
def printOrderly(array):
  for i in array:
    print(i)

def sumOfArray(array):
  ans=0
  for element in array:
    ans = ans+element
  return ans

def sum_Distribution(Die_A,Die_B):
  # creating a 2d array and initializing with 0
  sum_Array = [[0 for i in range(len(Die_A))] for j in range(len(Die_B))]
  for a in range(len(Die_A)):
    for b in range(len(Die_B)):
      sum_Array[a-1][b-1] = Die_A[a-1]+Die_B[b-1] 
  return sum_Array

def single_Probability(Die_A,Die_B,sum):
  # to find the probability of any number passed as the sum parameter
  sum_Array = sum_Distribution(Die_A,Die_B)
  count = 0
  for rows in sum_Array:
    for column in rows:
      if(column == sum):
        count = count+1
  # return count(!count check success)
  probability = count/36
  return probability

def all_Probability(Die_A,Die_B):
  prob_dict = {
    "2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0
  }
  for i in range(2,13):
    # used the single_probability method in order to reducet the time and increase reusability of the code
    # print(str(i))(!printing key value pair success!)
    prob_dict[str(i)] = round(single_Probability(Die_A,Die_B,i),4)
  return prob_dict


# to find the all combinations of the given dice along with the restrictions by loki
def posibilities_Calc(curr,free_space,input_values,posibilities,fixed_values,repetition=True):
  # base case
  if(0 == free_space):
    curr = sorted(curr)
    posibilities.add(tuple(curr))
    return posibilities
  # if the repetition of the elements is allowed this runs
  if(repetition):
    for input_value in input_values:
      posibilities_Calc(curr+[input_value],free_space-1,input_values,posibilities,fixed_values,True)
  # if repetition not allowed then this runs
  # to reduce the time and space
  else:
    for i in range(len(input_values)):
          remaining_input_values = input_values[:i] + input_values[i + 1:]
          # print(remaining_input_values) (!test recursion success!)
          posibilities_Calc( curr+ [input_values[i]], free_space - 1,remaining_input_values,posibilities,fixed_values,False )
  return posibilities

# final function that returns the new dice
def transform(die_a,die_b):
  original_possibilities=all_Probability(die_a,die_b)
  #these are fixed values because 1 is needed to get the sum 2(no other possible ways and similirly for 12 we need 4)
  # !!!even with the fixed array as emplty the code will run fine 
  fixed_values_a = [1, 4]  
  input_values_a = [1,2,3,4]
  # free space indicates the required no.of elements neede to make the dice complete
  # !!!if fixed valuse is empty need to make it to 6 since the fixed values are accounte here
  free_space_a = 4
  # possibilities are converted to sets isnce i got multiple duplicates of same array 
  posibilities_a = set()
  new_die_a_possibility = posibilities_Calc(fixed_values_a.copy(),free_space_a,input_values_a,posibilities_a,fixed_values_a,True)
  # print(new_die_a_possibility)(!test all unique possibilities of A success!)
  # similiar to the die A the 1 is needed to get 2 as sum and the 8 is the only option for the 12 to returned, also can be empty just work fine
  fixed_values_b = [1, 8]
  # any number more than 8 will give the sum greater than 12. so the values are capped to maximum of 8 and the 1 & 8 is to be fixed te value is reducd to 2 to 7
  input_values_b = [2,3,4,5,6,7]
  free_space_b = 4
  posibilities_b = set()
  # repetion is set False as the rule only states that it can have as many splots but not as many sides with same spots, will reduce the space required and time too
  new_die_b_possibility = posibilities_Calc(fixed_values_b.copy(),free_space_b,input_values_b,posibilities_b,fixed_values_b,False)
  # print(new_die_b_possibility)(!test all unique possibilities of B success!)
  for a in new_die_a_possibility:
     for b in new_die_b_possibility:
        # print(a,b)(!comparing possibilities success!)
        # converting the tuples to array so that it can be passed to the method in the part_a.py file,reusing the code
        # as the sum of all spots of a six side die is 21 and 2 dice gives the42 so if the sum of the both dice doesnot addup to 42 the set will be ignored
        if((sumOfArray(a)+sumOfArray(b))==42):
          new_sum_possibility = all_Probability(array('i',a),array('i',b))
        # checling every answers to find if any one matches the original probabilities,if matches returning it
          if(original_possibilities == new_sum_possibility):
            New_Die_A = a
            New_Die_B = b
            return New_Die_A,New_Die_B


print("New Dice are")
printOrderly(transform(Die_A,Die_B))
