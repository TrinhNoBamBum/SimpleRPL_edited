import RplIcmp
import random
from time import sleep
r = RplIcmp.RplSocket("eth0")
message_header = "\x9b\x01\x00\x00"
while True:
	message = "".join([ chr(random.randrange(255)) for x in range(100) ])
	r.send("fe80::1", message_header + message)
	print "sent one message"
	sleep(0.1)
