"""

5.Create a program that uses a while loop to print a pyramid star pattern with 4 rows, so the output looks like BookMyShow's seat rows:
*
***
*****
*******
<br><br><em><strong>Hint:</strong> Use two nested while loops: one for spaces, one for stars.</em>

"""

rows = 4
i = 1

while i <= rows:
    # print stars (odd numbers: 1, 3, 5, 7)
    j = 1
    while j <= (2 * i - 1):
        print("*", end="")
        j += 1
    
    print()  # move to next line
    i += 1
