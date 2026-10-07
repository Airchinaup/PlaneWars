from settings import *  # [2]
from pygame.locals import *  # [2]
from bullet import Bullet  # [
import random 
from explosion import Explosion


class HeroPlane(pygame.sprite.Sprite):
    def __init__(self, images, rate=50):
        """
        英雄飞机
        :param images: 组成飞机的图片列表
        :param rate: 飞机动画的播放频率
        """
        pygame.sprite.Sprite.__init__(self)  # [2]初始化动画精灵
        self._layer = 10  # [2]飞机所在的层级
        self.images = images  # [2]图片列表
        self.image = self.images[0]  # [2]surface对象
        self.rect = self.image.get_rect()  # [2]获取rect对象
        self.mask = pygame.sprite.from_surface(self.image)  # [2]图层蒙版，用于完美碰撞检测
        self.rect.midbottom = [WIDTH / 2, HEIGHT - 10]  # [2]设置飞机初始位置

        self.speedx = 5  # [2]飞机x方向速度
        self.speedy = 5  # [2]飞机y方向速度
        self.hp = 100  # [2]飞机生命数

        self.all_frame = len(self.images)  # [2]总的动画帧数目
        self.frame = 0  # [2]当前动画帧
        self.last_time = 0  # [2]记录上次的时间
        self.rate = rate  # [2]动画播放间隔

        self.last_shot = 0  # [3]上一次发射子弹的时间

    def update(self):
        """移动我方飞机"""
        if self.hp > 0:  # [2]如果我方飞机状态为存活
            keys = pygame.key.get_pressed()  # [2]获取按键
            if keys[K_w] and self.rect.top > 0:  # [2]如果按下 w 键并且没有超过窗口顶部
                self.rect.top -= self.speedy  # [2]飞机向上飞
            if keys[K_s] and self.rect.bottom < HEIGHT:  # [2]如果按下 s 键并且没有超过窗口底部
                self.rect.bottom += self.speedy  # [2]飞机向下飞
            if keys[K_a] and self.rect.left > 0:  # [2]如果按下 a 键并且没有超过窗口底左侧
                self.rect.left -= self.speedx  # [2]飞机向左飞
            if keys[K_d] and self.rect.right < WIDTH:  # [2]如果按下 d 键并且没有超过窗口右侧
                self.rect.right += self.speedx  # [2]飞机向右飞
            if keys[K_j]:  # [3]如果按下 j 键
                self.shoot()  # [3]发射子弹
        else:
            self.kill()  # [2]移出精灵组
            e = Explosion(plane_explosion,self.rect.center)
            allGroup.add(e)

        now = pygame.time.get_ticks()  # [2]获取当前时间
        if now - self.last_time > self.rate:  # [2]每50毫秒更新一帧动画
            self.last_time = now  # [2]更新上次记录的时间为当前时间
            self.frame += 1  # [2]动画帧数加1
            if self.frame >= self.all_frame:  # [2]如果动画播放到最后一个
                self.frame = 0  # [2]重置为第一个
            self.image = self.images[self.frame]  # [2]更新图片

    def shoot(self):
        """[3]发射子弹"""
        now = pygame.time.get_ticks()  # [3]获取当前时间
        if now - self.last_shot > 250:  # [3]射击延时400毫秒
            self.last_shot = now  # [3]更新上次记录的时间为当前时间
            b1 = Bullet(laserBlue02, self.rect.midtop)  # [3]生成子弹对象（中间）
            b2 = Bullet(laserBlue04, self.rect.midleft)  # [3]生成子弹对象（左侧）
            b3 = Bullet(laserBlue04, self.rect.midright)  # [3]生成子弹对象（中间）
            bulletGroup.add(b1, b2, b3)  # [3]添加到子弹精灵组
            allGroup.add(b1, b2, b3)  # [3]添加到所有精灵组

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        """
        敌方飞机的类
        :param image: 图片的surface对象
        """
        pygame.sprite.Sprite.__init__(self)  # [4]初始化动画精灵
        self._layer = 5  # [4]飞机所在的层级
        self.image = image  # [4]surface对象
        self.rect = self.image.get_rect()  # [4]获取rect对象
        self.mask = pygame.sprite.from_surface(self.image)  # [4]图层蒙版，用于完美碰撞检测

        self.rect.top = -HEIGHT  # [4]设置y方向坐标，从顶部一个窗口的位置出发
        self.rect.left = random.randint(0, WIDTH - self.rect.width)  # [4]设置x方向坐标，为随机值

        self.speedx = random.randint(-2, 2)  # [4] X 方向速度(后面会加上根据等级调整调整)
        self.speedy = random.randint(2, 3)  # [4] Y 方向速度(后面会加上根据等级调整调整)
        self.hp = 2  # [4]生命值，初始2点(后面会加上根据等级调整调整)


    def update(self):
        """"更新飞机位置"""
        if self.rect.top < HEIGHT:  # [4]如果没有超过窗口底部
            self.rect.x += self.speedx  # [4]水平方向移动
            self.rect.y += self.speedy  # [4]竖直方向移动
            if self.rect.left < 0 or self.rect.right > WIDTH:  # [4]移动过程中，如果碰到窗口左右边界
                self.speedx = -self.speedx  # [4]水平方向速度取反
        else:
            self.kill()  # [4]如果超过窗口底部，就移出精灵组
        if self.hp <= 0:
            self.kill()
            e = Explosion(plane_explosion,self.rect.center)
            allGroup.add(e)
class Food(pygame.sprite.Sprite):
    def __init__(self, image):
        """
        加血道具，飞机吃了能加血
        :param image: 图片的surface对象
        """
        pygame.sprite.Sprite.__init__(self)  # [4]初始化动画精灵
        self._layer = 6  # [4]层级
        self.image = image  # [4]surface对象
        self.rect = self.image.get_rect()  # [4]获取rect对象
        self.mask = pygame.sprite.from_surface(self.image)  # [4]图层蒙版，用于完美碰撞检测

        self.rect.top = -HEIGHT  # [4]设置y方向坐标，从顶部一个窗口的位置出发
        self.rect.left = random.randint(0, WIDTH - self.rect.width)  # [4]设置x方向坐标，为随机值

        self.speedx = random.randint(-2, 2)  # [4] X 方向速度(后面会加上根据等级调整调整)
        self.speedy = random.randint(2, 3)  # [4] Y 方向速度(后面会加上根据等级调整调整)
        self.energy = 10  # [4]能加血的数值

    def update(self):
        """"更新飞机位置"""
        if self.rect.top < HEIGHT:  # [4]如果没有超过窗口底部
            self.rect.x += self.speedx  # [4]水平方向移动
            self.rect.y += self.speedy  # [4]竖直方向移动
            if self.rect.left < 0 or self.rect.right > WIDTH:  # [4]移动过程中，如果碰到窗口左右边界
                self.speedx = -self.speedx  # [4]水平方向速度取反
        else:
            self.kill()  # [4]如果超过窗口底部，就移出精灵组
            