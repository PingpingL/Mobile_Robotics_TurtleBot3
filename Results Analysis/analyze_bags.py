from matplotlib.pyplot import cm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd
from bagpy import bagreader
import bagpy
from collections import defaultdict
from cycler import cycler

# b = bagreader('bags/second_try_better_map.bag')
# b = bagreader('bags/first_try_bad_map.bag')
# b = bagreader('bags/third_try.bag')
b = bagreader('bags/fourth_try.bag')

print(b.topic_table)
tf = b.message_by_topic('tf')


df_tf = pd.read_csv(tf)

detections = {'"tag_0': [], '"tag_1': [], '"tag_2': [],
              '"tag_3': [], '"tag_4': [], '"tag_5': []}

tags = ['"tag_0', '"tag_1', '"tag_2', '"tag_3', '"tag_4', '"tag_5']

scale = 1
offset = 0

for msg in df_tf.transforms:
    for tag in tags:
        if msg.split()[11].startswith(tag) and msg.split()[9].startswith('"map'):
            point = (scale*float(msg.split()[15]),
                     scale*float(msg.split()[17]))
            detections[tag].append(point)

fig, ax = bagpy.create_fig(1)

img = plt.imread('bags/fourth_try_map.pgm')
implot = plt.imshow(img, extent=[-19.2, 19.2, -19.2, 19.2])


color = iter(cm.tab10(np.linspace(0, 1, 6)))
actual = {'"tag_4': (-0.4, 2.2), '"tag_0': (-2.5, 2.2), '"tag_5': (1, 0.5),
          '"tag_3': (0.7, -0.4), '"tag_1': (-1.1, -7), '"tag_2': (-0.5, -4.5)}

for tag, data in detections.items():
    xs = [i[0]+offset for i in data][-100:]
    ys = [i[1]+offset for i in data][-100:]
    c = next(color)
    # ax[0].scatter(x=xs, y=ys, label=tag[1:])
    ax[0].scatter(x=actual[tag][0], y=actual[tag][1], color=c,
                  label=f'{tag[1:]} ground truth', marker='o')
    # c = next(color)
    ax[0].scatter(x=np.average(xs), y=np.average(
        ys), label=f'{tag[1:]} centroid', color=c, marker='x')

    cent = [np.average(xs), np.average(ys)]
    gt = [actual[tag][0], actual[tag][1]]

    plt.plot([cent[0], gt[0]], [cent[1], gt[1]], color=c,
             linestyle="--")

ax[0].set_xlabel('X [m]')
ax[0].set_ylabel('Y [m]')
ax[0].set_title('April Tag detections in map frame')
ax[0].margins(x=-0.3, y=-0.3)
plt.subplots_adjust(left=0.05, bottom=0.075, right=0.95, top=0.95)
plt.legend()
plt.savefig('Pics/centroid-gt.jpg')
plt.show()
