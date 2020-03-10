#!/usr/bin/env python3

import sys
import docker

if __name__ == '__main__':
	client = docker.from_env()
	swarmmanager=client.nodes.list()
	leader=0
	quorum=0
	manager=0
	ready=0
	for nodeid in swarmmanager:
		if nodeid.attrs['Status']['State']=='ready':
			ready +=1
		if 'ManagerStatus' in nodeid.attrs.keys():
			manager +=1
			if nodeid.attrs['ManagerStatus']['Reachability']=='reachable':
				quorum +=1
			if 'Leader' in nodeid.attrs['ManagerStatus'].keys() and nodeid.attrs['ManagerStatus']['Leader']:
				leader +=1
	if leader == 0:
		print ("CRITICAL - No leader")
		sys.exit(2)
	if quorum < (manager//2+1):
		print ("CRITICAL - Manager quorum")
		sys.exit(2)
	if quorum < manager:
		print ("WARNING - Manager failure - quorum OK")
		sys.exit(1)
	if ready < 	len(swarmmanager):
		print ("WARNING - Node failure- manager OK")
		sys.exit(1)
	print ("OK - All node up")
	sys.exit(0)
	
	