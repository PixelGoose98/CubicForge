from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

blocks = []
current_block_texture = 'assets\grass.png'  # Default texture
lol = False

for i in range(30):
    for j in range(30):
        block = Button(color=color.white, model='cube', position=(j, 0, i),
                       texture=current_block_texture, parent=scene, origin_y=0.5)
        blocks.append(block)

for i in range(30):
    for j in range(30):
        stone_block = Button(color=color.white, model='cube', position=(j, -1, i),
                             texture='assets\stone.png', parent=scene, origin_y=0.5)
        blocks.append(stone_block)

for i in range(30):
    for j in range(30):
        third_stone_block = Button(color=color.white, model='cube', position=(j, -2, i),
                                   texture='assets\stone.png', parent=scene, origin_y=0.5)
        blocks.append(third_stone_block)

for i in range(30):
    for j in range(30):
        third_stone_block = Button(color=color.white, model='cube', position=(j, -3, i),
                                   texture='assets\stone.png', parent=scene, origin_y=0.5)
        blocks.append(third_stone_block)

def input(key):
    global current_block_texture, lol

    if key == '1' and not lol:
        current_block_texture = 'assets\grass.png'
    elif key == '2' and not lol:
        current_block_texture = 'assets\stone.png'
    elif key == '3' and not lol:
        current_block_texture = 'assets\planks.png'
    elif key == '4' and not lol:
        current_block_texture = 'assets\glass.png'
    elif key == '5' and not lol:
        current_block_texture = 'assets/brick.png'
    elif key == '6' and not lol:
        current_block_texture = 'assets/1.png'
    elif key == '7' and not lol:
        current_block_texture = 'assets/2.png'
    elif key == '8' and not lol:
        current_block_texture = 'assets/3.png'
    elif key == '9' and not lol:
        current_block_texture = 'assets/4.png'
    elif key == '6' and lol:
        current_block_texture = 'assets/5.png'
    elif key == '7' and lol:
        current_block_texture = 'assets/6.png'
    elif key == '8' and lol:
        current_block_texture = 'assets/7.png'
    elif key == '9' and lol:
        current_block_texture = 'assets/8.png'
    elif key == '2' and lol:
        current_block_texture = 'assets\cob.png'
    elif key == '5' and lol:
        current_block_texture = 'assets/bricks2.png'
    elif key == '4' and lol:
        current_block_texture = 'assets/log2.png'
    elif key == '3' and lol:
        current_block_texture = 'assets/log.png'
    elif key == '1' and lol:
        current_block_texture = 'assets/grass2.png'
    elif key == ']' and not lol:
        lol = True
    elif key == '[' and lol:
        lol = False
    

    for block in blocks:
        if block.hovered:
            if key == 'left mouse down':
                new_block = Button(color=color.white, model='cube', position=block.position + mouse.normal,
                                   texture=current_block_texture, parent=scene, origin_y=0.5)
                blocks.append(new_block)
            elif key == 'right mouse down':
                blocks.remove(block)
                destroy(block)

app.run()
