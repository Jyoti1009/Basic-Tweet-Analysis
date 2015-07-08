import time

import text_utils as txu
import twitter_utils as twu

'''
Implementing the first feature which would produce the total count for each word in a file ft1.txt
'''

# Calculate the time when the processing starts
start = time.clock()

inp, outp = txu.extract_arguments() 
# The mode of input can be a text file or twitter api json
tweets = '\n'.join(twu.get_input(inp))

words = txu.extract_words(tweets)
counter = txu.get_counter(words)
txu.write_file("\n".join("{} \t\t\t\t\t {}".format(k, v) for k, v in sorted(dict(counter).items())),outp)

# Calculate the time processing ends
end = time.clock()

# Print total time taken 
print "Total time taken in processing word count: ", end - start
