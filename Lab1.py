import numpy as np
import matplotlib . pyplot as plt
import seaborn as sns # Import seaborn
# Set the seaborn style
sns . set_theme ( style = " whitegrid " )

# This defines the step size h for the numerical c o m p u t a t i o n .
h = 0 . 1
# This creates a grid x from 0 to 2 with intervals of h .
x = np . arange (0 , 2 * np . pi , h )
# This computes the cosine function values for each point in the
grid x .
y = np . cos ( x )
# This calc ula tes the forward d i f f e r e n c e s of y ’ vector ’ divided by
h , which is an a p p r o x i m a t i o n of
the de riva tiv e of cos ( x ) .
forward_diff = np . diff ( y ) / h
# This defines a new grid x_diff that c o r r e s p o n d s to the forward
d i f f e r e n c e s . It excludes the last
point of x since np . diff reduces
the array size by one .
x_diff = x [ : - 1 : ]
# This calc ula tes the exact solution for the de riv ativ e of cos ( x ) ,
which is - sin ( x ) , evaluated at
x_diff .
exact_solution = - np . sin ( x_diff )
# This code block creates a plot showing both the finite d iffe ren ce
a p p r o x i m a t i o n and the exact
solution .
plt . figure ( figsize = ( 12 , 8 ) )
plt . plot ( x_diff , forward_diff , ’ -- ’ , \
label = ’ Finite difference approximation ’)
plt . plot ( x_diff , exact_solution , \
label = ’ Exact solution ’)
plt . legend ()
plt . show ()
# Finally , this computes the maximum error between the numerical
de riva tiv e and the exact solution
, then prints the result .
max_error = max ( abs ( exact_solution - forward_diff ) )
print ( max_error )




# EXAMPLE 3:

# Function and point of interest
x0 = 0 . 7
# Step sizes
h = 2 . ** - np . arange (1 , 30 )
# Finite diff ere nce a p p r o x i m a t i o n of the de riv ativ e
df = ( np . cos ( x0 + h ) - np . cos ( x0 ) ) / h
# True value of the d eri v ati ve
true_value = - np . sin ( x0 )
# Display the results with formatted output
print ( " k | Approximation | Ratio of errors | Relative
differences " )
print ( " ---| - - - - - - - - - - - - - - - - - - - - - | - - - - - - - - - - - - - - - - - |
- - - - - - - - - - - - - - - - - - - - - - " )
previous_approximation = None
previous_error = None
for k in range (1 , len ( h ) + 1 ) :
approximation = df [ k - 1 ]
error = np . abs ( approximation - true_value )
ratio = np . abs ( previous_error / error ) if previous_error is not
None else " "
relative_difference = np . abs (( approximation -
previous_approximation ) /
previous_approximation ) if
previous_approximation is not
None else " "
# Format the output
formatted_approximation = f " { approximation :. 15f } "
formatted_ratio = f " { ratio :. 6f } " if isinstance ( ratio , float )
else ratio
f or m at t ed _ re l at i ve _ di f fe r e nc e = f " { relative_difference :. 10f } "
if isinstance (
relative_difference , float )
else relative_difference
print ( f " { k : < 3 } | { formatted_approximation : < 21 } | { formatted_ratio
: < 17 } | {
f or m at t ed _ re l at i ve _ di f fe r en c e
: < 20 } " )
previous_error = error
previous_approximation = approximation
# Print the true value of the d eri vati ve for reference
print ( f " \ nTrue value of the derivative : { true_value :. 17f } " )