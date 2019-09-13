import numpy as np
from Interceptor_V2 import Init, Draw, Game_step
import random

Init()
Game_step(2)
for stp in range(1000):
    action_button = random.randint(0,3)
    r_locs, i_locs, c_locs, ang, score = Game_step(action_button)

    if stp in [15,16]:
        print("Stp", stp)
        print("r_locs{}\ni_locs{}\n c_locs{}\n ang{} \nscore{}".format(r_locs, i_locs, c_locs, ang, score))
    Draw()

print(score)

# City(-4600, -2100, 800)
# City(-2100, -400, 800)

rocket_pix = 0.1

def Draw_matix(r_locs, i_locs, c_locs, ang, score):
    width = 10000  # [m]
    height = 4000  # [m]

    input = np.zeros((width, height))

    #r_locs: Location of each rocket in the game (x,y)
    for r in r_locs:
        input[int(r[0] + 0.5*width),int(r[1])] = 1

    #i_locs: Location of each interceptor in the game (x,y)
    for intr in i_locs:
        input[int(intr[0] + 0.5*width),int(intr[1])] = 7

    #c_locs: Location of each city in the game (x, width)
    for c in c_locs:
        x= int(c[0] + 0.5 * width)
        city_width = c[1]
        for w in range(city_width):
            input[x+w,0] = 2




# plt.plot(r.x, r.y, '.y')




# #
#
#     plt.cla()
#     plt.rcParams['axes.facecolor'] = 'black'
#     for r in rocket_list:
#         plt.plot(r.x, r.y, '.y')
#     for intr in interceptor_list:
#         plt.plot(intr.x, intr.y, 'or')
#         C1 = plt.Circle((intr.x, intr.y), radius=turret.prox_radius, linestyle='--', color='gray', fill=False)
#         ax = plt.gca()
#         ax.add_artist(C1)
#     for c in city_list:
#         plt.imshow(c.img, extent=[c.x - c.width / 2, c.x + c.width / 2, 0, c.img.shape[0]])
#         plt.set_cmap('bone')
#     for e in explosion_list:
#         P1 = plt.Polygon(e.verts1, True, color='yellow')
#         P2 = plt.Polygon(e.verts2, True, color='red')
#         ax = plt.gca()
#         ax.add_artist(P1)
#         ax.add_artist(P2)
#     plt.plot(turret.x, turret.y, 'oc', markersize=12)
#     plt.plot([turret.x, turret.x + 100 * np.sin(np.deg2rad(turret.ang))],
#              [turret.y, turret.y + 100 * np.cos(np.deg2rad(turret.ang))], 'c', linewidth=3)
#     plt.plot(turret.x_hostile, turret.y_hostile, 'or', markersize=12)
#     plt.axes().set_aspect('equal')
#     plt.axis([-world.width / 2, world.width / 2, 0, world.height])
#     plt.title('Score: ' + str(world.score))
#     plt.draw()
#     plt.pause(0.001)
