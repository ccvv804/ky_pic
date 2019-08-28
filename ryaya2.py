import os
import sys # sys 모듈 가져오기
import binascii # binascii 모듈 가져오기
from PIL import Image
directory = os.listdir('/hanzo/rara')
os.chdir('/hanzo/rara')
for file in directory:
    r = file
    faxman = r.find('.png')
    if faxman == -1 :
        print(r+' pass')
    else :
        p90 = Image.open(r)
        p91 = Image.Image.tobytes(p90)
        r9=r.replace(".png", ".rgba")
        r10=r.replace(".png", ".raw")
        r11=r.replace(".png", ".coex")
        r12=r.replace(".png", ".coea")
        z0=open(r9,'bw')
        z0.write(p91)
        z0.close()
        print(p90.width)
        print(p90.height)
        p93 = p90.width
        p94 = p90.height
        p95 = p93.to_bytes(2, byteorder='little')
        p96 = p94.to_bytes(2, byteorder='little')
        print(p95)
        z2 = open(r11,'rb')
        z3 = open(r12,'rb')
        coea = z3.read()
        coex = z2.read()
        z1 = open(r10,'bw')
        z1.write(b'\x53\x48\x49\x4e')
        z1.write(coea)
        z1.write(p95)
        z1.write(b'\x00\x00')
        z1.write(p96)
        z1.write(b'\x00\x00')
        z1.write(coex)
        z2.close
        f01 = 'dummy'
        f91=open(r9,'rb')
        f91.seek(0)
        while f01 != b'' : 
            f01=f91.read(1) #R
            f02=f91.read(1) #G
            f03=f91.read(1) #B
            f04=f91.read(1) #A
            z1.write(f03) #B
            z1.write(f02) #G
            z1.write(f01) #R
            z1.write(f04) #A
        z1.close()
        #p93 = p90.width
        #p94 = p90.height