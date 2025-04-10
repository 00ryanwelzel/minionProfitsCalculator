import re
from contextlib import nullcontext

from bs4 import BeautifulSoup

class Minion:
    miniontype = None
    miniongreatestmaterial = None
    minionspeed = None
    matmagnitude = None

    def __int__(self, type, mat, speed, mag):
        self.miniontype = type
        self.miniongreatestmaterial = mat
        self.minionspeed = speed
        self.matmagnitude = mag




