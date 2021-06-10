#import
import pygame,random,time,sys
pygame.init()
# load hình ảnh
m = 20 # kích thước chiều cao và chiều rộng
Imgbody = pygame.transform.scale(pygame.image.load('body.png'),(m,m))
Imghead = pygame.transform.scale(pygame.image.load('body.png'),(m,m))
Imgfood = pygame.transform.scale(pygame.image.load('Diem.jpg'),(m,m))
# tạo cửa sổ
gameSurface = pygame.display.set_mode((735,475))
pygame.display.set_caption('Snake Slap Slip Slup')
# màu sắc
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)
# khai báo biến
snakepos = [100,60]
snakebody = [[100,60],[80,60],[60,60]]
foodx = random.randrange(1,71)
foody = random.randrange(1,45)
if foodx % 2 != 0: foodx += 1
if foody % 2 != 0: foody += 1
foodpos = [foodx * 10, foody * 10]
foodflat = True
direction = 'RIGHT'
changeto = direction
score = 0
# hàm gameover
def game_over():
    gfont = pygame.font.SysFont('consolas',40)
    gsurf = gfont.render('Game over!',True,red)
    grect = gsurf.get_rect()
    grect.midtop = (360,150)
    gameSurface.blit(gsurf,grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(5) #time wait to exit
    pygame.quit()
    sys.exit()
# hàm show_score
def show_score(choice = 1):
    sfont = pygame.font.SysFont('consolas',20)
    ssurf = sfont.render('Score: {0}'.format(score),True,black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (70,20)
    else:
        srect.midtop = (360,230)
    gameSurface.blit(ssurf,srect)
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
                pygame.event.post(pygame.evet.Event(pygame.QUIT))
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
        foodx = random.randrange(1,71)
        foody = random.randrange(1,45)
        if foodx %2 != 0: foodx += 1
        if foody %2 != 0: foody += 1
        foodpos = [foodx * 10, foody * 10]
    foodflat = True
    #  cập nhật lên cửa sổ
    gameSurface.fill(white)
    for pos in snakebody:
        gameSurface.blit(Imgbody,pygame.Rect(pos[0],pos[1],m,m))
        #pygame.draw.rect(gameSurface,blue,pygame.Rect(pos[0],pos[1],m,m))
    gameSurface.blit(Imghead,pygame.Rect(snakebody[0][0],snakebody[0][1],m,m)) # head
    gameSurface.blit(Imgfood,pygame.Rect(foodpos[0],foodpos[1],m,m))
    #pygame.draw.rect(gameSurface,gray,pygame.Rect(foodpos[0],foodpos[1],m,m))
    # xử lý di chuyển đụng 4 cạnh biên
    if snakepos[0] > 710 or snakepos[0] < 10:
        game_over()
    if snakepos[1] > 450 or snakepos[1] < 10:
        game_over()
    # xử lý tự ăn chính mình
    for b in snakebody[1:]:
        if snakepos[0] == b[0] and snakepos[1] == b[1]:
            game_over()
    # đường viền
    pygame.draw.rect(gameSurface,gray,(10,10,715,455),2)
    show_score()
    pygame.display.flip()