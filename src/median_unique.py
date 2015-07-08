import time

import text_utils as txu
import twitter_utils as twu

'''
 Implementing the second feature which would produce the median for tweets in a file ft2.txt

'''

# Calculate the time when the processing starts
start = time.clock()

# The mode of input can be a text file or twitter api json
inp, outp = txu.extract_arguments() 
tweets = twu.get_input(inp)

#initialize the median dictionary
median_dict = {'median': 0.0,
			   'length': 0}
outfile = open(outp, 'w')
for tweet in tweets:
	median_dict = txu.get_median_iterative(tweet, median_dict)
	outfile.write("{0:.2f}".format(round(median_dict['median'],2))+"\n")
outfile.close()

# Calculate the time processing ends
end = time.clock()

# Print total time taken 
print "Total time taken in processing median: ", end - start
