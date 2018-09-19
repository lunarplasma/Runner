from time import sleep


# wait 2 seconds, then raise an exception
print("testfile_1 has started!")
sleep(2)
raise Exception("I'm causing myself to fall over.")
