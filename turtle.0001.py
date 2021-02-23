# План:
# получить координаты точек, нанести координаты точек,
# назвать координаты точек, соединиить координаты точек.

# эта программа наносит звезды созвездия Ориона.
# подготовка
import turtle

turtle.penup()
turtle.hideturtle()

# entering constant variables
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -180

# paint stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)  # left shoulder
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)  # right shoulder
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)  # left star in belt
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # middle star in belt
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)  # right star in belt
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)  # left knee
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)  # right knee
turtle.dot()

# names
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)  # left shoulder
turtle.write("Бетельгейзе")
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)  # right shoulder
turtle.write("Хатиса")
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)  # left star in belt
turtle.write("Альнитак")
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # middle star in belt
turtle.write("Альнилам")
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)  # right star in belt
turtle.write("Минтака")
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)  # left knee
turtle.write("Саиф")
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)  # right knee
turtle.write("Ригель")

# наносим линии
# левое плечо-левая зв на поясе
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# правое плечо-правая звезда
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# левая зв пояса в среднюю звезду пояса
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

# средняя звезда пояса в правая звезда
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# левая звезда пояса в левое колено
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# правая звезда пояса в правое колено
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.penup()

# the end
