#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
from time import strftime


def do_pack():
    """ A fabric script that generates archive a .tgz archive from the contents of the web_static """

    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    output = local("tar -cvzf {} web_static".format(path))
    if output.failed:
        return None
        return path
