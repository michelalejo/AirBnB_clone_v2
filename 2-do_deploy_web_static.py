#!/usr/bin/python3
"""Script that distributes an archive to your web servers"""
from fabric.api import *
from fabric.operations import run, put, sudo
import os
env.hosts = ['66.70.184.249', '54.210.138.75']


def do_deploy(archive_path):
    """Script that distributes an archive to your web servers"""
    if os.path.isfile(archive_path) is False:
        return False

    try:
        files = archive_path.split("/")[-1]
        directory = files.split(".")[0]
        route = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(route, directory))
        run('tar -xzf /tmp/{} -C {}{}/'.format(files, route, directory))
        run('rm /tmp/{}'.format(files))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(route, directory))
        run('rm -rf {}{}/web_static'.format(route, directory))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(route, directory))
        return True
    except:
        return False
