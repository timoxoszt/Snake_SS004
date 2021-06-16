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

# khai báo biến
snakepos = [100,60]
snakebody = [[100,60],[80,60],[60,60]]
direction = 'RIGHT'
changeto = direction
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
