import random
import tkinter
import math
from random import choice

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
B_LOWER_LIMIT = 5
B_UPPER_LIMIT = 5
BLACK_LINES = random.randint(B_LOWER_LIMIT, B_UPPER_LIMIT)
BLACK_LENGTH = 10

def make_canvas(width, height, title):

    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

def random_color():

    my_list = ['#dd0100'] * 20 + ["#fac901"] * 20 + ["#225095"] * 20 + ["white"] * 40
    color = choice(my_list)
    return color

def biggest_rect_color(my_list):

    color = choice (my_list)
    return color

def generate_lines ():

    lines = []
    lines2 = []

    for i in range (BLACK_LINES):
        position = random.randint (25, CANVAS_WIDTH-25)
        lines.append(position)
        lines2.append(position)

    lines2.sort()

    for i in range(len(lines2)-1):
        if (lines2[i+1] - lines2[i] < 50):
            lines2.clear()
            lines.clear()
            try:
                return generate_lines()
            except RecursionError:
                if BLACK_LINES <= 4:
                    lines = [150, 300, 460, 590]
                else:
                    # ie. BLACK_VERTICALS > 5
                    lines = [55, 350, 500, 604, 725]
                return lines
    return lines


def verticals(canvas):
    """NOTE, verticals cannot be before 25px at WIDTH and beyond 'CANVAS WIDTH - 25',
     And the verticals must be spaced apart by at least 50 px."""

    x_pos_black_verticals = generate_lines()
    black_vertical_pos = [[0,0,0,CANVAS_HEIGHT]] #add left edge to list

    for i in range (len(x_pos_black_verticals)):

        verticals = canvas.create_rectangle(x_pos_black_verticals[i],0,x_pos_black_verticals[i]+BLACK_LENGTH,CANVAS_HEIGHT, fill = "black", outline = "black")
        black_vertical_pos.append([x_pos_black_verticals[i],0,x_pos_black_verticals[i]+BLACK_LENGTH,CANVAS_HEIGHT])

    black_vertical_pos.append([CANVAS_WIDTH, 0, CANVAS_WIDTH, CANVAS_HEIGHT]) #add right edge to list
    black_vertical_pos.sort()
    return black_vertical_pos

def horizontals (canvas):

    y_pos_black_verticals = generate_lines()
    y_pos_black_verticals.sort()
    black_horizontal_pos = [[0,0,CANVAS_WIDTH,0]] #add top edges

    for i in range (len(y_pos_black_verticals)):
        horizontals = canvas.create_rectangle(0,y_pos_black_verticals[i],CANVAS_WIDTH,y_pos_black_verticals[i]+BLACK_LENGTH, fill = "black", outline = "black")
        black_horizontal_pos.append([0,y_pos_black_verticals[i],CANVAS_WIDTH,y_pos_black_verticals[i]+BLACK_LENGTH])

    black_horizontal_pos.append([0, CANVAS_HEIGHT,CANVAS_WIDTH,CANVAS_HEIGHT]) #add bottom edge
    return black_horizontal_pos

def intersections (V, H):

    #get x2y2 top left hand of square
    x2y2 =[]
    for j in range(len(V)-1):
        for i in range (len(H)-1):
            #if Horizontal y2 between Vertical y1 and y2 and if Vertical x2 is between Horizontal x1 and x2
            # if V[j][1] <= H[i][3] <= V[j][3] and H[i][0] <= V[j][2] <= H[i][2]:
            # if H[i][3]
                x2 = V[j][2] #+ 1
                y2 = H[i][3] #+ 1
                x2y2.append([x2,y2])
    print (x2y2)

    #get x1y1 bottom right hand of square

    x1y1 =[]
    for j in range(1,len(V)):
        for i in range (1,len(H)):
                x1 = V[j][0] #- 1
                y1 = H[i][1] #- 1
                x1y1.append([x1,y1])
    print (x1y1)
    return x2y2, x1y1

def last_row(i, list1):
    list2 = []
    for j in range((int(math.sqrt(len(list1))) - 1), len(list1), int(math.sqrt(len(list1)))):
        list2.append(j)
    if i in list2:
        return True
    else:
        return False

def last_column(i, list1):
    list3 = []
    for j in range(len(list1) - int(math.sqrt(len(list1))), len(list1), 1):
        list3.append(j)
    if i in list3:
        return True
    else:
        return False

def options(list1, i, n):

    if n == 1:
        list1[i] = '-'
        # x2y2[i] matches #x1y1[i]
        x2y2 = i
        x1y1 = i
        tup = [x2y2, x1y1]
    if n == 2:
        list1[i] = '-'
        list1[i + 1] = '-'
        # x2y2[i] matches #x1y1[i+1]
        x2y2 = i
        x1y1 = i + 1
        tup = [x2y2, x1y1]
    if n == 3:
        list1[i] = '-'
        list1[i + int(math.sqrt(len(list1)))] = '-'
        # x2y2[i] matches #x1y1[i+ sqrt(len(list1))]
        x2y2 = i
        x1y1 = i + int(math.sqrt(len(list1)))
        tup = [x2y2, x1y1]

    if n == 4:
        list1[i] = '-'
        list1[i + int(math.sqrt(len(list1)))] = '-'
        list1[i + 1] = '-'
        list1[i + int(math.sqrt(len(list1))) + 1] = '-'
        # x2y2[i] matches #x1y1[i + sqrt(len(list1))+1]
        x2y2 = i
        x1y1 = i + int(math.sqrt(len(list1))) + 1
        tup = [x2y2, x1y1]

    return list1, tup

def make_combinations(x2y2,x1y1):

    list1 = []
    combo = []
    for i in range(len(x2y2)):
        list1.append(i)

    for i in list1:

        if str(i) != "-":
            if last_row(i, list1):
                if i == (len(list1) - 1):

                    list1, tup = options(list1, i, 1)
                    combo.append(tup)
                else:

                    n = random.choice([1, 3])
                    list1, tup = options(list1, i, n)
                    combo.append(tup)

            elif last_column(i, list1):

                if list1[i + 1] == "-":
                    list1, tup = options(list1, i, 1)
                    combo.append(tup)
                else:
                    n = random.choice([1, 2])
                    list1, tup = options(list1, i, n)
                    combo.append(tup)
            else:

                if list1[i + 1] == "-":

                    list1, tup = options(list1, i, 3)
                    combo.append(tup)
                else:

                    n = random.choice([1, 2, 3, 4])
                    list1, tup = options(list1, i, n)
                    combo.append(tup)
        else:
            pass

    return combo

def biggest_rectangle(rectangles):

    rectangle_sizes =[]
    for i in range (len(rectangles)):
        area = (rectangles[i][2]-rectangles[i][0]) * (rectangles[i][3] - rectangles[i][1])
        rectangle_sizes.append(area)

    return rectangle_sizes.index(max(rectangle_sizes)), max(rectangle_sizes)/(CANVAS_HEIGHT*CANVAS_HEIGHT)
    # print (max(rectangle_sizes)/(CANVAS_WIDTH*CANVAS_HEIGHT))

def smallest_rectangles(rectangles):
    rectangle_sizes =[]
    for i in range (len(rectangles)):
        area = (rectangles[i][2]-rectangles[i][0]) * (rectangles[i][3] - rectangles[i][1])
        rectangle_sizes.append(area)

    return rectangle_sizes.index(min(rectangle_sizes))

def rectangle_is_small(rectangles):
    area = (rectangles[0][2]-rectangles[0][0]) * (rectangles[0][3] - rectangles[0][1])
    if area / (CANVAS_HEIGHT*CANVAS_WIDTH) * 100 < 3:
        print (str(area / (CANVAS_HEIGHT*CANVAS_WIDTH) * 100) + "Activated left black corner")
        return True
    else:
        return False

def paint_color (canvas, rectangles):

    # find out what the 4 biggest squares are, and give it a random color, delete from list of rectangles, and delete color from list:

    color_list = ["#dd0100", "#fac901", "#225095", "white"] # red  # yellow # blue #white
    print ("len of rectangle list: " + str(len(rectangles)))
    for i in range(4):

        biggest_rect_pos, rect_percentage = biggest_rectangle(rectangles)
        color = biggest_rect_color(color_list)
        print (color)
        canvas.create_rectangle(rectangles[biggest_rect_pos][0], rectangles[biggest_rect_pos][1], rectangles[biggest_rect_pos][2], rectangles[biggest_rect_pos][3], fill=color, outline=color)
        if rect_percentage * 100 > 20:
            print (rect_percentage)
            #split rectangle horizontally or vertically
            if rectangles[biggest_rect_pos][2]-rectangles[biggest_rect_pos][0] > rectangles[biggest_rect_pos][3]-rectangles[biggest_rect_pos][1]:
                #create vertical line
                print ("Divide vertical")
                vertical_x1 = random.randint(rectangles[biggest_rect_pos][0]+50, rectangles[biggest_rect_pos][2]-50)
                canvas.create_rectangle(vertical_x1, rectangles[biggest_rect_pos][1], vertical_x1 + BLACK_LENGTH, rectangles[biggest_rect_pos][3], fill = "black", outline = "black")
                if rect_percentage * 100 > 35:
                    #spread another color over the large line and divide it down further in opposite direction
                    color_list2 = ["#dd0100", "#fac901", "#225095", "white"]
                    print("split divs >40%")
                    color_list2.remove(color)
                    color2 = biggest_rect_color(color_list2)
                    canvas.create_rectangle(vertical_x1 + BLACK_LENGTH,rectangles[biggest_rect_pos][1], rectangles[biggest_rect_pos][2], rectangles[biggest_rect_pos][3], fill = color2, outline = color2)
            else:
                #create horizontal line
                print ("Divide horizontal")
                horizontal_y1 = random.randint(rectangles[biggest_rect_pos][1]+50, rectangles[biggest_rect_pos][3]-50)
                canvas.create_rectangle(rectangles[biggest_rect_pos][0], horizontal_y1, rectangles[biggest_rect_pos][2], horizontal_y1+BLACK_LENGTH, fill = "black", outline = "black")
                if rect_percentage * 100 > 35:
                    # spread another color over the large line and divide it down further in opposite direction
                    color_list2 = ["#dd0100", "#fac901", "#225095", "white"]
                    print("split divs >40%")
                    color_list2.remove(color)
                    color2 = biggest_rect_color(color_list2)
                    canvas.create_rectangle(rectangles[biggest_rect_pos][0],horizontal_y1 + BLACK_LENGTH, rectangles[biggest_rect_pos][2], rectangles[biggest_rect_pos][3], fill=color2, outline=color2)

        del rectangles[biggest_rect_pos]
        color_list.remove(color)

    print("len of rectangle list: " + str(len(rectangles)))
    x = random.randint(1,2)
    print ("Black " + str(x))
    print (rectangles)
    for i in range (x):
        smallest_rect_pos = smallest_rectangles(rectangles)
        canvas.create_rectangle(rectangles[smallest_rect_pos][0], rectangles[smallest_rect_pos][1], rectangles[smallest_rect_pos][2], rectangles[smallest_rect_pos][3], fill="black", outline="black")
        del rectangles[smallest_rect_pos]
    print("len of rectangle list: " + str(len(rectangles)))

    #add black balance if remaining list contains black at top left hand corner.
    if (rectangles[0][0] == 0 and rectangles[0][1] == 0) and rectangle_is_small(rectangles):
        canvas.create_rectangle(rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3], fill = "black", outline = "black")
    # elif (rectangles[0][0] == 0 and rectangles[0][1] == 0):

    del rectangles[0]

    #for remaining rectangles
    for i in range(len(rectangles)-1,2,-1):
        color3 = random_color()
        print (color3)
        canvas.create_rectangle(rectangles[i][0], rectangles[i][1], rectangles[i][2], rectangles[i][3], fill = color3, outline = color3)


def main():

    canvas = make_canvas (CANVAS_WIDTH, CANVAS_HEIGHT, "Mondrian")

    #make verticals
    black_vertical_pos = verticals (canvas)
    print (black_vertical_pos)

    #make horizontals
    black_horizontal_pos = horizontals (canvas)
    print (black_horizontal_pos)

    #find intersections
    x2y2, x1y1 = intersections (black_vertical_pos, black_horizontal_pos)

    #make squares
    tups = make_combinations(x2y2,x1y1)
    print (tups)
    rectangles = []
    for j in range(len(tups)):
        rectangles.append(x2y2[tups[j][0]])
        rectangles[j].extend(x1y1[tups[j][1]])

    #color rectangles
    """RULES FOR COLOR: canvas have to contain all 5 colors. 
    The domineering color should not be black"""
    paint_color (canvas, rectangles)

    canvas.update()
    canvas.mainloop()

if __name__ == '__main__':
    main()
