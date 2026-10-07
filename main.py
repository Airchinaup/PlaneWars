import sys  # [1]
import pygame  # [1]
from pygame.locals import *  # [1]
from settings import *  # [1]
from background import Background  # [1]
from plane import HeroPlane, Enemy, Food  # [2]导入我方飞机
import random  # [4]


def main():
    """游戏主界面"""
    clock = pygame.time.Clock()  # [1]设置时钟对象
    Background(0, 0)  # [1]生成游戏背景

    hero = HeroPlane(hero_images)  # [2] 生成英雄飞机
    allGroup.add(hero)  # [2]添加到所有精灵组
    # 时间点
    last_time = pygame.time.get_ticks()
    dead_time = pygame.time.get_ticks()
    
      # [4]记录时间
    while True:
        clock.tick(120)  # [1]设置FPS为60帧
        for event in pygame.event.get():  # [1]游戏事件处理
            if event.type == QUIT:  # [1]退出事件
                pygame.quit()  # [1]退出pygame
                sys.exit()  # [1]退出运行环境

        now = pygame.time.get_ticks()  # [4]获取当前时间
        if now - last_time > 250:  # [4]每250毫秒出现一架敌方飞机
            last_time = now  # [4]更新上次记录的时间为当前时间
            enemy_image = random.choice(enemy_plane_images)  # [4]随机选择一个敌方飞机图片
            enemy = Enemy(enemy_image)  # [4]生成一个敌方飞机对象
            enemyGroup.add(enemy)  # [4]将敌方飞机添加到精灵组
            allGroup.add(enemy)  # [4]将敌方飞机添加到所有精灵组
            if random.randint(1, 25) == 1:  # [4]随机生成食物，概率1/25
                food = Food(food_image)  # [4]生成一个道具
                foodGroup.add(food)  # [4]添加到食物道具精灵组
                allGroup.add(food)  # [4]添加到所有精灵组

        if hero.hp > 0:
            hits = pygame.sprite.spritecollide(hero, enemyGroup, False,pygame.sprite.collide_mask)
            for enemy in hits:
                enemy.hp = 0
                hero.hp -= 50
                if hero.hp <= 0:
                    dead_time = pygame.time.get_ticks()
        if hero.hp > 0:
            hits = pygame.sprite.spritecollide(hero, foodGroup, True,pygame.sprite.collide_mask)
            for hit in hits:
                hero.hp += hit.energy

        hits = (pygame.sprite.groupcollide(bulletGroup,enemyGroup,False,False,pygame.sprite.collide_mask))
        for bullet in hits:
            bullet.hp = 0
            for enemy in hits[bullet]:
                enemy.hp -= 1

        if hero.hp <= 0 and now - dead_time > 1000:
            allGroup.empty()
            return

        allGroup.update()  # [1] 所有精灵调用update()
        allGroup.draw(screen)  # [1] 绘制所有精灵到窗口上

        pygame.display.update()  # [1]刷新屏幕窗口


if __name__ == '__main__':
    # 启动游戏
    main()  # [1]运行主界面

