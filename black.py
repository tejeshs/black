from git import Repo
import subprocess
import os 
import boto3

def create_loadbalancer():
    client = boto3.client('elb',region_name='us-west-2')
    response = client.create_load_balancer(
    LoadBalancerName='blackproject',
    Listeners=[
        {
            'Protocol': 'HTTP',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'HTTP',
            'InstancePort': 9000,
        },
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'blackproject'
        },
    ]
    )
    print response
    addinstance_lb = client.register_instances_with_load_balancer(
    LoadBalancerName='blackproject',
    Instances=[
        {
            'InstanceId': 'string'
        },
    ]
    )
    print addinstance_lb

def clone_repo():
    git_url = "git@github.com:tejeshs/black.git"
    cwd = os.getcwd()
    repo_name = "black"
    repo_dir = cwd+"/"+repo_name
    print "cloning repo"
    if(not os.path.isdir(repo_dir)):
        os.mkdir(repo_dir)
        Repo.clone_from(git_url, repo_dir)
    subprocess.call(["java","-jar",repo_dir+"/builds/libs/project.jar"])

clone_repo()
create_loadbalancer()
