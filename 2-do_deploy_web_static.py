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
        route = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(files))
        directory = files.split(".")
        run("mkdir -p {}/{}/".format(route, directory[0]))
        new = '.'.join(directory)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new, route, directory[0]))
        run("rm /tmp/{}".format(files))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(route, directory[0], route, directory[0]))
        run("rm -rf {}/{}/web_static".format(route, directory[0]))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current"
            .format(route, directory[0]))
        return True
    except:
        return False
