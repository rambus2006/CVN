import pygame

pygame.init() #초기화 하는 함수 - 무조건 있어야 한다. 

#게임 창 크기 
background = pygame.display.set_mode((480,360))
pygame.display.set_caption("SONOL")

#캐릭터의 좌표값 (창 크기를 2로 나눈 값 )
x_ch = background.get_size()[0]//2
y_ch = background.get_size()[1]//2
#창이 떠있을 때를 True라고 하고
play = True

#변수 play를 true -> false로 바꿔 창을 닫는다.창 안에서 실행하기 위해서는 while문 안에 명령어를 써야 한다. 
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        #화살표키 눌렀을 때 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("왼쪽 화살표")
            if event.key == pygame.K_RIGHT:
                print("오른쪽 화살표")
                

#배경 
background.fill((255,0,0))
#https://www.youtube.com/watch?v=QCKm6BK3IcE&list=PLz2iXe7EqJOMp5LozvYa0qca9E4OBkevW&index=2
pygame.display.update()
pygame.quit()