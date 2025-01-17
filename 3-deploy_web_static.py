#!/usr/bin/python3
" a script that creates and distributes an archive to your web servers"

import os.path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['34.201.165.238', '100.26.217.108']

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dtm = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dtm.year, dtm.month, dtm.day, dtm.hour, dtm.minute, dtm.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
def do_deploy(archive_path):
    """An archive to a web server.

    Args:
        archive_path (str): string.
    Returns:
        False if file doesnt exist, true if it does.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
