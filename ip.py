import socket
import sys
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket created")
except socket.error as err:
    print("creation failed")
port=8080

try:
    host_ip=socket.gethostbyname('www.sharda.ac.in')
except socket.gaierror:
    print("errro in resolving host")

