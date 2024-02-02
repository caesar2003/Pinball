from classes.ball import Ball
def new_ball_spawn(ball_group, ball_count):
    if len(ball_group) == 0:
        Ball(420, 300 , speed= [-1,-5])
    for ball in ball_group:
        if ball.index == 0 and ball.coords.y > 800 and ball_count[0] == False:
            Ball(420, 300 , speed= [-1,-5])
            ball_count[0] = True
        elif ball.index == 1 and ball.coords.y > 800 and ball_count[1] == False:
            Ball(420, 300 , speed= [-1,-5])
            ball_count[1] = True
                # Create a new ball after removing the old one
