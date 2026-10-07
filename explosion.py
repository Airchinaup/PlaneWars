from settings import *
import pygame
class Explosion(pygame.sprite.Sprite):
    def __init__(self, images, center):
        """
        [6]爆炸特效
        :param images: 爆炸特效图片的surface对象的列表
        :param center: 图片的中心位置
        """
        pygame.sprite.Sprite.__init__(self)
        self._layer = 6  # [6]层级
        self.images = images  # [6]存储爆炸图片的列表
        self.center = center  # [6]记录爆炸中心
        self.image = self.images[0]  # [6]取第一个爆炸图片
        self.rect = self.image.get_rect()  # [6]获取rect对象
        self.rect.center = self.center  # [6]调整中心点的位置
        self.frame = 0  # [6]记录爆炸动画帧
        self.last_time = pygame.time.get_ticks()  # [6]记录上次动画播放的时间

    def update(self):
        self.rect.y += 1
        now = pygame.time.get_ticks()
        if now - self.last_time > 80:
            self.last_time = now
            self.frame += 1
            if self.frame < len(self.images):
                self.image = self.images[self.frame]
            else:
                self.kill()