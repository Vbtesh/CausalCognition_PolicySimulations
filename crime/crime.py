import pygame
from random import randint


def calcSatRate(crimeRate):
    return 1 - (crimeRate - 1) / 3

crime = randint(1, 100)
crimeRate = 1.3

sat = randint(1, 100)
satRate =  calcSatRate(crimeRate) # A decrease equivalent to a third of the crime increase


pass