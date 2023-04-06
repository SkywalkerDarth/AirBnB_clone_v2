#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
from time import strftime

@task
def do_pack():
    """ generates archive a .tgz archie """

    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    output = local("tar -cvzf {} web_static".format(path))
    if output.failed:
        return None
        return path
