
import time
import sys

# Checking the number of arguments
if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + " N \n\t(where N is the ID of the problem to solve)"

# The second argument is the ID of the problem to solve
id = int(sys.argv[1])

# Importing the corresponding object
# Package is src.p<ID>
package = "src.p" + str(id)
# object is P<ID>
name = "p" + str(id)
# Let's import
Problem = getattr(__import__(package, fromlist=[name]), name)

# Construction of a problem object
p = Problem(id)

# Printing the text of the problem
print str(p)

# Start chronometer
start_time = time.time()
# Call the solver function 
res = p.solve()
# Stop the chronometer
elapsed_time = time.time() - start_time

# Display the results
if (elapsed_time < 60) :
    print "[ok] Result: {0} (obtained in {1}s)".format(res, elapsed_time)
else:
    print "[ko] Result: {0} (obtained in {1}s)".format(res, elapsed_time)
