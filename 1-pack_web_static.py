#!/usr/bin/python3
"""Script that generates a .tgz archive from the contents of the webstatic."""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """Script that generates a .tgz archive of the contents of the webstatic"""
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        if isdir("versions") is False:
            local("mkdir versions")
        data = "versions/web_static_{}.tgz".format(time)
        local('tar -cvzf {} web_static'.format(data))
        return data
    except:
        return None
