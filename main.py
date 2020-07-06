#Copyright (c) 2020, Marinos Papadakis
#All rights reserved.
#This source code is licensed under the MIT License found in the LICENSE file in the root directory of this source tree.

from findresponse import findresponse
from speak import speechrec
from responses import response, botname

# Variable to check if main has been executed before
r = False

def main():
    # Check if main has been executed before (if yes do not print the same response)
    global r
    if not r:
        response(f"Hello! I am {botname} bot!")
        r = True
    # Find appropriate response for user's microphone input
    findresponse(speechrec())
    # Call main after program responds
    main()

# Call main
if __name__ == "__main__":
    main()