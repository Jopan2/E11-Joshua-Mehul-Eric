import time 
import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--runtime', type= float, required= False)
args = parser.parse_args()
a = time.time() + args.runtime
while time.time()<a:
    itime = int(time.time())
    value = random.random()
    print(itime, value)
    time.sleep(1)


