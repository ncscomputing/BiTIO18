#based on work by Kari Hardy and extended and developed by Chris Penn

from mcpi.minecraft import Minecraft

import time
import random

import microbit

mc = Minecraft.create()

WoolColourList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

O = 1 # Orange
S = 6 # Pink / Skin
G = 5# Green
W = 0 # White
R = 14 # Red
SB = 9# Sky blue / cyan
B = 12# Brown
DG = 13 # DARK GREEN
BL = 15 # Black
    
while True:
    
    Steve = [
    [B,  B,  B,   B,  B,  B,  B,  B],
    [B,  B,  B,   B,  B,  B , B,  B],
    [B,  S,  S,   S,  S,  S,  S,  B],
    [S,  S,  S,   S,  S,  S,  S,  S],
    [S,  W,  SB,  S,  S, SB,  W, S],
    [S,  S,  S,   R,  R,  S,  S, S],
    [S,  S,  B,   S,  S,  B,  S, S],
    [S,  S,  B,   B,  B,  B,  S, S],
    ]

#IF a button pressed.
    if microbit.button_a.was_pressed():
        Pixel_Art_Name = "Normal Steve"
        print(Pixel_Art_Name)
        O = 1 # Orange
        S = 6 # Pink / Skin
        G = 5 # Green
        W = 0 # White
        R = 14 # Red
        SB = 9# Sky blue / cyan
        B = 12# Brown
        DG = 13 # DARK GREEN
        BL = 15 # Black
        
        mc.postToChat(Pixel_Art_Name)
        x, y, z = mc.player.getPos()
        for row in Steve:
            y = y - 1
            x = 0
            for pixel in row:
                mc.setBlock(x, y, z+20, 35, pixel)
                x = x + 1

   

#IF b button pressed.
    if microbit.button_b.was_pressed():
        O = random.choice(WoolColourList) # Orange
        S = random.choice(WoolColourList) # Pink / Skin
        G = random.choice(WoolColourList) # Green
        W = random.choice(WoolColourList) # White
        R = random.choice(WoolColourList) # Red
        SB = random.choice(WoolColourList)# Sky blue / cyan
        B = random.choice(WoolColourList)# Brown
        DG = random.choice(WoolColourList) # DARK GREEN
        BL = random.choice(WoolColourList) # Black

        Pixel_Art_Name = "Pop art Steve"
        print(Pixel_Art_Name)
        mc.postToChat(Pixel_Art_Name)
        x, y, z = mc.player.getPos()
        for row in Steve:
            y = y - 1
            x = 0
            for pixel in row:
                mc.setBlock(x, y, z+20, 35, pixel)
                x = x + 1

   
