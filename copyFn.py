import jenkins
import os
import sys

def copyJob(hostvar,unamevar,pwdvar,sourceJob,destinationJob):
  host = sys.argv[1]
  username = sys.argv[2]
  password = sys.argv[3]
  server = jenkins.Jenkins(host,username=username, password=password)
  print("Job Copy In-Progress")
  sourceJob = sys.argv[4]
  destinationJob = sys.argv[5]
  server.copy_job(sourceJob,destinationJob)
  
copyJob(*sys.argv[1:])
