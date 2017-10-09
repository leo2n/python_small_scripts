"""
ping server using Python
"""
import platform
import os 

def ping(host):
    """
    Return True if host: str  responds to a ping request 
    """
    parameters = "-n 1" if platform.system().lower() == "windows" else "-c 1"

    return os.system("ping " + parameters +" " +host) == 0
