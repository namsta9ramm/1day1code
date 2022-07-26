import pygame

pygame.init() #초기화

screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("gaming making")

#이벤트루프
running=True #게임이 진행중인가 확인
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()