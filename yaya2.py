import os
import sys # sys 모듈 가져오기
import binascii # binascii 모듈 가져오기
from PIL import Image
directory = os.listdir('/hanzo/yaya')
os.chdir('/hanzo/yaya')
for file in directory:
    r = file
    faxman = r.find('.raw')
    if faxman == -1 :
        print(r+' pass')
    else :
        f=open(r,'rb')
        f.seek(12) # 가로 크기 이동
        xx=f.read(2) # 가로 크기 읽기
        x=binascii.hexlify(xx) # 가로 크기 데이터 변환
        x1=x.decode('ascii')
        f1=x1[0:2] # 가로 크기 1구간
        f2=x1[2:4] # 가로 크기 2구간
        fx=f2+f1 # 가로 길이 산출
        f.seek(16) # 가로 크기 이동
        yy=f.read(2) # 세로 크기 읽기
        y=binascii.hexlify(yy) # 세로 크기 데이터 변환
        y1=y.decode('ascii')
        f3=y1[0:2] # 세로 크기 1구간
        f4=y1[2:4] # 세로 크기 2구간
        fy=f4+f3 # 세로 길이 산출
        dx=int(fx, base=16) # 파일 크기를 10진수로 변환
        dy=int(fy, base=16) # 파일 크기를 10진수로 변환
        dxx=str(dx)
        dyy=str(dy)
        won=r.count('\\')
        r2=r
        while won != 0:
            r1=r.find('\\')
            won = won -1
            r2=r[r1+1:]
            r=r2
        z=open("shin.txt", 'a')
        z.write(r2+' ')
        z.write(dxx+'x')
        z.write(dyy)
        z.write('\n')
        z.close()
        r9=r.replace(".raw", ".rgba")
        r19=r.replace(".raw", ".coex")
        r18=r.replace(".raw", ".coea")
        z3=open(r18,'bw')
        f.seek(4)
        f18=f.read(8)
        z3.write(f18)
        z3.close
        z2=open(r19,'bw')
        f.seek(20)
        f19=f.read(204)
        z2.write(f19)
        z2.close
        z1=open(r9,'bw') # 사진 파일 생성
        f.seek(224) # 파일 위치로 이동
        #data=f.read() # 끝까지 파일을 읽음 (양심불량)
        f01 = 'dummy'
        while f01 != b'' : 
            f01=f.read(1)
            f02=f.read(1)
            f03=f.read(1)
            f04=f.read(1)
            z1.write(f03)
            z1.write(f02)
            z1.write(f01)
            z1.write(f04)
        z1.close() # 파일 저장
        rdata = open(r9,'rb')
        print(r9)
        rawData = rdata.read()
        imgSize = int(dxx), int(dyy)
        print(dxx)
        print(dyy)
        img = Image.frombytes('RGBA',imgSize,rawData,decoder_name='raw')
        r19=r9.replace(".rgba",".png")
        print(r19)
        img.save(r19)