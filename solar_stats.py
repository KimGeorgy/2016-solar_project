from solar_objects import Star, Planet
from math import sqrt
from solar_main import*
import numpy as np
import matplotlib.pyplot as plt


def create_stats(space_objects, physical_time):
    """создает данные для всех элементов
    """

    for body in space_objects:
        if body.type == 'star':
            for object in space_objects:
                v_abs = sqrt(object.Vx ** 2 + object.Vy ** 2)
                distance = sqrt((object.x - body.x) ** 2 + (object.y - body.y) ** 2)
                object.stats.append([v_abs, distance, physical_time])


def build_gr():
    with open('stats.txt', 'r') as out_file:
        for line in out_file:
            info = eval(line)
            time = []
            v = []
            r = []
            for i in range(len(info[1])):
                v.append(info[1][i][0])
                r.append(info[1][i][1])
                time.append(info[1][i][2])

        plt.subplot(221)
        plt.plot(time, v)
        plt.xlabel('t, c')
        plt.ylabel('|v|, м/с')
        plt.title('График модуля скорости от времени')

        plt.subplot(222)
        plt.plot(time, r)
        plt.xlabel('t, c')
        plt.ylabel('r, м')
        plt.title('График расстояния до звезды от времени')

        plt.subplot(223)
        plt.plot(r, v)
        plt.xlabel('r, м')
        plt.ylabel('|v|, м/с')
        plt.title('График модуля скорости от расстояния')

        plt.show()
