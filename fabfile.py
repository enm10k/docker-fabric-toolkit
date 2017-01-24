from fabric.api import (
  local,
  task,
)

@task
def hello():
  local('echo Hello World!')
  local('git --version')
  local('rsync --version')
  local('python -c "import boto3; print(boto3.__version__)"')
