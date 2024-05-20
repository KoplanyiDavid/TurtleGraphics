import turtle as t
import random as rd

# Extracting the colors from the original painting (img.jpg)
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("img.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Make the paint using the colors
t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
color_list = [(202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124),
              (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72),
              (145, 178, 148), (91, 73, 75), (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172),
              (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155),
              (175, 99, 101), (176, 192, 209)]
tim.setheading(220)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, rd.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
