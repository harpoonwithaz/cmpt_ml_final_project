

def test_list_comprehension(data):

    my_list = []
    season_map = {
        "Winter": 0,
        "Spring": 1,
        "Summer": 2,
        "Autumn": 3
    }

    # Uses list comprehension to add the items we need to the list, then appends it to inputs list
    # Converts
    my_list.append([
        (
            float(season_map[x]) if i == 11 else
            1.0 if i == 12 and x == "Holiday" else
            0.0 if i == 12 and x == "No Holiday" else
            float(x)
        )
        for i, x in enumerate(data)
        if i not in (0, 1, 13)        # <-- skip these
    ])

    return my_list

'''test = ['01/12/2017',254,0,-5.2,37,2.2,2000,-17.6,0,0,0,'Winter','No Holiday','Yes']
here = test_list_comprehension(test)
print(here)'''


def test(a, b):
    for item1, item2 in a, b:
        print('item 1', item1)
        print('item2', item2)

import turtle

def draw_bar_graph(data: dict, title="Bar Chart"):
    # --- CONFIG ---
    screen_width = 900
    screen_height = 600
    margin = 80
    bar_spacing = 10
    bar_color = "steelblue"
    axis_color = "black"
    font = ("Arial", 10, "normal")
    title_font = ("Arial", 16, "bold")

    # --- SETUP ---
    turtle.setup(screen_width, screen_height)
    turtle.clear()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.title(title)

    # Sort keys in bucket order
    keys = list(data.keys())
    '''if "100+" in keys:
        keys.remove("100+")
        keys.sort(key=lambda k: int(k.split("-")[0]))
        keys.append("100+")
    else:
        keys.sort(key=lambda k: int(k.split("-")[0]))'''

    values = [data[k] for k in keys]
    max_value = max(values) if values else 1

    # Graph area
    graph_left = -screen_width // 2 + margin
    graph_bottom = -screen_height // 2 + margin
    graph_width = screen_width - 2 * margin
    graph_height = screen_height - 2 * margin

    num_bars = len(keys)
    bar_width = (graph_width - (num_bars - 1) * bar_spacing) / num_bars

    # --- AXES ---
    turtle.penup()
    turtle.goto(graph_left, graph_bottom)
    turtle.pendown()
    turtle.pencolor(axis_color)
    turtle.forward(graph_width)  # x-axis

    turtle.penup()
    turtle.goto(graph_left, graph_bottom)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(graph_height)  # y-axis

    # --- Y-AXIS LABELS ---
    ticks = 5
    for i in range(ticks + 1):
        y_val = i * max_value / ticks
        y_pos = graph_bottom + (y_val / max_value) * graph_height

        # tick
        turtle.penup()
        turtle.goto(graph_left - 5, y_pos)
        turtle.pendown()
        turtle.goto(graph_left, y_pos)

        # label
        turtle.penup()
        turtle.goto(graph_left - 10, y_pos - 5)
        turtle.write(f"{int(y_val)}", align="right", font=font)

    # --- BARS ---
    for i, key in enumerate(keys):
        value = data[key]
        bar_height = (value / max_value) * graph_height

        x_start = graph_left + i * (bar_width + bar_spacing)
        y_start = graph_bottom

        # draw bar rectangle
        turtle.penup()
        turtle.goto(x_start, y_start)
        turtle.pencolor(axis_color)
        turtle.fillcolor(bar_color)
        turtle.begin_fill()
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(bar_height)
        turtle.setheading(0)
        turtle.forward(bar_width)
        turtle.setheading(270)
        turtle.forward(bar_height)
        turtle.setheading(180)
        turtle.forward(bar_width)
        turtle.end_fill()

        # bar value text
        turtle.penup()
        turtle.goto(x_start + bar_width / 2, y_start + bar_height + 5)
        turtle.write(str(value), align="center", font=font)

        # x label
        turtle.goto(x_start + bar_width / 2, graph_bottom - 20)
        turtle.write(key, align="center", font=font)

    # --- TITLE ---
    turtle.penup()
    turtle.goto(0, graph_bottom + graph_height + 30)
    turtle.write(title, align="center", font=title_font)

    turtle.done()


# Example Usage:
# data = {
#    "0-10": 3, "10-20": 1, "20-30": 4, "30-40": 6,
#    "40-50": 2, "50-60": 1, "60-70": 0, "70-80": 3,
#    "80-90": 5, "90-100": 1, "100+": 2
# }
# draw_bar_graph(data, "Percentage Distribution")

if __name__ == '__main__':
    data = {
        "0-10": 3, "10-20": 1, "20-30": 4, "30-40": 6,
        "40-50": 2, "50-60": 1, "60-70": 0, "70-80": 3,
        "80-90": 5, "90-100": 1, "100+": 2
    }

    draw_bar_graph(data)