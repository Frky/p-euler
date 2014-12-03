
import time
import sys

problems_solved = range(1, 22)

# Checking the number of arguments
if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + " N \n\t(where N is the ID of the problem to solve, --all to solve all problems)"

    
if sys.argv[1] == "--all":
    # Solving all problems for which we have a solution
    
    for pid in problems_solved:
        # Importing the corresponding object
        # Package is src.p<PID>
        package = "src.p" + str(pid)
        # object is P<PID>
        name = "p" + str(pid)
        # Let's import
        Problem = getattr(__import__(package, fromlist=[name]), name)
        
        # Construction of a problem object
        p = Problem(pid)
        
        # Start chronometer
        start_time = time.time()
        # Call the solver function 
        res = p.solve()
        # Stop the chronometer
        elapsed_time = time.time() - start_time
        
        # Display the results
        if (elapsed_time < 60) :
            print "[{0}][ok] Result: {1} (obtained in {2}s)".format(pid, res, elapsed_time)
        else:
            print "[{0}][ko] Result: {1} (obtained in {2}s)".format(pid, res, elapsed_time)

else:
    # Solving the corresponding problem

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
