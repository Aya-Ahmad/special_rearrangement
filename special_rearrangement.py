"""
This function takes a list of integers to rearrange it,
such that all even numbers comes before odd numbers,
while maintaining their relative order.
"""
def SpecialRearrangement( nums ):
    even_numbers = []
    odd_numbers = []
#Iterate a for loop through the input list,
#if even append to even numbers, if odd append to odd numbers
    for i in range ( len(nums) ):
        if nums [ i ] %2 == 0 :
            even_numbers.append( nums[i] )
        else:
            odd_numbers.append( nums[i] )
    nums = even_numbers + odd_numbers
    return nums

length = int ( input (" Hello, please enter the length of your array - no decimal allowed: ") )
#if condition needed here to validate the input
if length <= 0 :
    print ("Please enter a valid number!")
#Ask the user to enter the values of the array and add them into a list
else:
    for i in range( length ):
        list_nums = []
        values = int ( input("Now, enter your favorite whole numbers! "))
        list_nums.append( values )
    # Calling the function
    rearrangement_list = SpecialRearrangement( list_nums )
    print("Check out your values before they get organized!",list_nums)
    print("Voila! Here are your rearranged values!",rearrangement_list)
