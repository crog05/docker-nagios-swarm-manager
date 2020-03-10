# docker-nagios-swarm-manager
This script has been tested on Debian buster.
Docker is docker-ce 5:19.03.7\~3-0~debian-buster
## Goal
This script allows to monitor docker swarm with nagios.
Status is warning if one or more node has failed and manager quorum still ok.
Status is critical if manager nodes have failed and quorum is not good.
## Dependencies
You need to install python3-docker
## Setup
Script has to be installed on docker swarm managers nodes.
## Ansible
Ansible folder contains a basic role to allow setup on a the swarm, nrpe setup.
## Notes
Script is a basic start, needs to be improved, like error handling.
