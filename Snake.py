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
# màu sắc
red = pygame.Color(255,0,0)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)
# khai báo biến
snakepos = [100,60]
snakebody = [[100,60],[80,60],[60,60]]
foodx = random.randrange(1,80)
foody = random.randrange(1,60)
if foodx % 2 != 0: foodx += 1
if foody % 2 != 0: foody += 1
foodpos = [foodx * 10, foody * 10]
foodflat = True
direction = 'RIGHT'
changeto = direction
score = 0

# vòng lặp chính
while True:
    pygame.time.delay(100) # tốc độ chơi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # xử lý phím
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_UP:
                changeto = 'UP'
            if event.key == pygame.K_DOWN:
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    # hướng đi
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    # cập nhật vị trí mới
    if direction == 'RIGHT':
        snakepos[0] += m
    if direction == 'LEFT':
        snakepos[0] -= m
    if direction == 'UP':
        snakepos[1] -= m
    if direction == 'DOWN':
        snakepos[1] += m
    #cơ chế thêm khúc dài ra
    snakebody.insert(0,list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score += 1
        foodflat = False
    else:
        snakebody.pop()
    # sản sinh mồi
    if foodflat == False:
        foodx = random.randrange(1,80)
        foody = random.randrange(1,60)
        if foodx %2 != 0: foodx += 1
        if foody %2 != 0: foody += 1
        foodpos = [foodx * 10, foody * 10]
    foodflat = True
    pygame.display.flip()