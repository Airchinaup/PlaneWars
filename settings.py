import pygame  # [1]
from image import load_images  # [2]

WIDTH, HEIGHT = 1024, 600  # [1]设置窗口的宽和高
FPS = 100  # [1]游戏帧率

pygame.init()  # [1]初始化 pygame
pygame.mixer.init()  # [1]初始化声音模块
screen = pygame.display.set_mode((WIDTH,HEIGHT))  # [1]生成一个游戏窗口
pygame.display.set_caption("飞机大战")  # [1]设置标题
icon = pygame.image.load(r"D:\PythoProjecT\飞机大战\PNG\icon.png").convert_alpha()  # [1]加载图标图片
pygame.display.set_icon(icon)  # [1]设置图标

# 精灵组
allGroup = pygame.sprite.LayeredUpdates()  # [1]带有层级的精灵组，所有精灵都在改组中，用于在屏幕上显示
bulletGroup = pygame.sprite.Group()  # [3]子弹精灵组，用于碰撞检测
enemyGroup = pygame.sprite.Group()
foodGroup = pygame.sprite.Group()

# [2]加载英雄飞机图片
hero_images = load_images("飞机大战/PNG/Playerships/playerShip.png", 1, 2)  # [2]加载图片
# [3]子弹图片
laserBlue02 = pygame.image.load("飞机大战/PNG/bullets/laserBlue01.png").convert_alpha()  # [3]加载子弹图片
laserBlue04 = pygame.image.load("飞机大战/PNG/bullets/laserBlue04.png").convert_alpha()  # [3]加载子弹图片
# [4]敌方飞机图片
enemy_plane_images = []  # [4]敌方飞机图片列表，用于随机选择其中的图片
for i in range(1, 21):  # [4]加载所有的敌方飞机图片
    filename = "飞机大战/PNG/Enemies/enemy{}.png".format(i)  # [4]获取图片文件名
    image = pygame.image.load(filename).convert_alpha()  # [4]加载图片
    enemy_plane_images.append(image)  # [4]添加到列表

food_image = pygame.image.load("飞机大战/PNG/Power-ups/HP.png").convert_alpha()
plane_explosion = load_images("飞机大战/PNG/Explosion/explosion.png",3,3)
bullet_explosion = load_images("飞机大战/PNG/bullets/bulletExplosion01.png",1,2)