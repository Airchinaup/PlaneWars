"""第6章播放动画中有此功能"""
import pygame  # [2]


def load_images(filename, rows, columns):
    """
    [2]加载动画图片
    :param filename: 图片的文件名
    :param rows: 动画的行数
    :param columns: 动画的列数
    :return: images: 动画帧组成的列表
    """
    images = []  # [2]存储动画帧的列表
    master_image = pygame.image.load(filename).convert_alpha()  # [2]加载动画主图
    master_rect = master_image.get_rect()  # [2]获取序列图的尺寸
    frame_width = master_rect.width//columns  # [2]单个动画帧的宽度
    frame_height = master_rect.height//rows  # [2]单个动画帧的高度
    for row in range(rows):  # [2]根据单个动画帧尺寸切割图片
        for col in range(columns):
            frame_rect = (col * frame_width, row * frame_height, frame_width, frame_height)
            frame_image = master_image.subsurface(frame_rect)
            images.append(frame_image)  # [2]将单个动画帧加入到列表
    return images  # [2]返回动画帧组成的列表
