import numpy as np

ab = np.array([[1.0, 2.0, 4.0, 4.0],
                [2.0, 1.0, -1.0, 2.0],
                [1.0, 2.0, -4.0, 0.0]],
                float) # add array 
                
n = ab.ndim + 1 # lenth of array 
x = np.zeros(n) # x = [0.0.0] 
# Applying mùethode Gauss 
for i in range(n-1): # i= 0 to 2
    for j,y in zip(ab[i+1:, i], range(1,n)): # J = 1 to 3
        factor = j / ab[i,i]  # To get the number that zeros the line after
        ab[i+ y]  = factor * ab[i]  - ab[i + y] # get the array that zeros
print(f"array after zeros  \n {ab} \n") # print array after zeros

x[n-1] = ab[n-1][n]/ab[n-1][n-1] # this is : X3 

for i in range(n-2,-1,-1):
    x[i] = ab[i][n]
    
    
    for j in range(i+1,n):
        # this is rool (القاعدة )
        # B*X2 - A * X3 = C 
        # X3 = C - A * X2 / B  <= div B in the last taps in line 33   
        # هذي قاعدة "علاه درنا اشارة السالب لان 
        # بالسالب كي ندوه لجيهة الاخرة
        # سالب تخليه يقلب الاشار"
        x[i] = x[i] - ab[i][j]*x[j] 
        # print(f"= {x[i]}")
    # this is : X2 and X1  "after looping"       
    x[i] = x[i]/ab[i][i]  # X3 = X3 / B  <== this is the last taps
    # print(f"== {x[i]}")
    
# Displaying solution    
for i in range(n):
    print(f"The solution is x{i+1} : {x[i]} ") # this is the solution