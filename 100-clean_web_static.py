#!/usr/bin/python3
""" deletes out-of-date archives, using the function do_clean """
import os
from fabric.api import *

env.host = ['34.201.165.238', '100.26.217.108']


def do_clean(number=0)
    """deletes out of date archives
    Args:
        number(int): no of archives to be kept
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(no)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
