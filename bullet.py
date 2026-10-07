from settings import *  # [3]
from explosion import Explosion

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        """
        [3]子弹动画精灵
        :param image: 图片的surface对象
        :param pos: 图片的中心位置坐标
        """
        pygame.sprite.Sprite.__init__(self)  # [3]初始化动画精灵
        self._layer = 9  # [3]层级为9，在英雄飞机下面
        self.image = image  # [3]surface对象
        self.rect = self.image.get_rect()  # [3]获取rect对象
        self.mask = pygame.sprite.from_surface(self.image)  # [3]图层蒙版，用于完美碰撞检测
        self.speed = 8  # [3]子弹的飞行速度
        self.damage = 1  # [3]子弹攻击力
        self.rect.center = pos  # [3]调整子弹出发点的位置
        self.hp = 1

    def update(self):
        """[3]更新子弹位置，向前发射，超过边界移除"""
        self.rect.top -= self.speed  # [3]子弹向上移动
        if self.rect.bottom < 0:  # [3]如果移动到窗口上边界
            self.kill()  # [3]移出精灵组
        if self.hp <= 0:
            self.kill()
            e = Explosion(bullet_explosion,self.rect.center)
            allGroup.add(e)



