from settings import *  # [1]


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        [1]背景，可以滚动
        """
        pygame.sprite.Sprite.__init__(self)  # [1]初始化动画精灵
        self._layer = -1  # [1]背景层在-1，其它层都要在背景层上方
        self.image = pygame.image.load("飞机大战/PNG/background.png").convert()  # [1]surface对象
        self.rect = self.image.get_rect()  # [1]获取rect对象
        self.rect.x = x  # [1]设置坐标
        self.rect.y = y  # [1]设置坐标
        self.next = False  # [1]是否加载了下一个背景
        self.last_time = 0  # [1]记录上次的时间
        allGroup.add(self)  # [1]将精灵添加到精灵组，只要创建了精灵，就会自动加入到精灵组

    def update(self):
        now = pygame.time.get_ticks()  # [1]获取当前时间
        if now - self.last_time > 50:  # [1]每50毫秒更新一帧动画
            self.last_time = now  # [1]更新上次记录的时间为当前时间
            self.rect.y += 1  # [1]移动一个像素
            if self.rect.y > HEIGHT:  # [1]如果背景超过了下边界就移除
                self.kill()
            if not self.next and self.rect.y >= 0:  # [1]如果还没有生成下一个背景并且当前背景的有移动
                Background(0, -(HEIGHT-1))  # [1]新生成一个背景，该背景会自动加入到allGroup精灵组
                self.next = True  # [1]标记为True，表示已经生成下一个背景了
