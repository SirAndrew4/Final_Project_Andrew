def generate_alt_tiles(radius=1,height=1,position=(0,0,0)):
    circle_tile=cmd.polyCylinder(r=radius,h=height,name="ctile_#")
    cmds.move(
        position[0], position[1]+height/2.0, position[2], circle_tile
    )
    return circle_tile
