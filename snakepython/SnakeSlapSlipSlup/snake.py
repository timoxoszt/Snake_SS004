#import
import pygame,random,time,sys
pygame.init()
# load hình ảnh
m = 20 # kích thước chiều cao và chiều rộng
Imgbody = pygame.transform.scale(pygame.image.load('body.png'),(m,m))
Imghead = pygame.transform.scale(pygame.image.load('body.png'),(m,m))
Imgfood = pygame.transform.scale(pygame.image.load('Diem.jpg'),(m,m))
# tạo cửa sổ
gameSurface = pygame.display.set_mode((835,635))
pygame.display.set_caption('Snake Slap Slip Slup')
# vòng lặp chính
while True:
    pygame.time.delay(100) # tốc độ chơi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # đường viền
    pygame.draw.rect(gameSurface,gray,(10,10,815,615),2)