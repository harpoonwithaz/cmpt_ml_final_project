import turtle
from typing import Dict

def calculate_model_performance(actual_values: list, predicted_values) -> Dict[str, int]:
    '''Function that calculates the error percentage of model from actual values and predicted values for each prediction
    
    Args:
        actual_values (list): list of output test values

    Returns:
        percentages (dict): keys representing the percentage range, 
        value representing amount of predictions with error percentage in that range
    '''
    percentages = {
        '0-10': 0,
        '10-20': 0,
        '20-30': 0,
        '30-40': 0,
        '40-50': 0,
        '50-60': 0,
        '60-70': 0,
        '70-80': 0,
        '80-90': 0,
        '90-100': 0,
        '100+': 0
    }
    
    # Makes sure both the values have same amounts
    if len(actual_values) == len(predicted_values):
        for i in range(len(actual_values)):
            # Avoids dividing by 0
            if not actual_values[i] == 0:
                percentage_error = (abs(actual_values[i] - predicted_values[i]) / actual_values[i]) * 100
                
                # Explicitly checks if percentage bigger than 100
                if percentage_error > 100:
                    percentages['100+'] += 1
                else:
                    index = int(percentage_error//10)
                    
                    # Special case when percentage is greater than 100
                    if index == 10:
                        index = 9

                    # Formats key for the percentages dict
                    key = f'{index*10}-{(index+1)*10}'
                    percentages[key] += 1

    return percentages

def graph_error_percentage(percentages: dict, graph_title: str):
    '''Function to model the error percentages as a bar graph
    
    Args:
        percentages (dict): Containing error percentages for each prediction
    '''
    # I acknowledge that I used chatgpt to assist me in creating this function.
    # It helped me with method of creating the graph, and how to display the bars on the graph

    keys = percentages.keys()

    # Turtle setup
    screen_width = 720
    screen_height = 540
    font = ('Arial', 10, 'normal')
    axis_font = ('Arial', 10, 'bold')
    title_font = ('Arial', 16, 'bold')

    turtle.setup(screen_width, screen_height)
    turtle.clear()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.title(graph_title)

    # Graph size
    margin = 100
    graph_left = -screen_width // 2 + margin
    graph_bottom = -screen_height // 2 + margin
    graph_width = screen_width - 2 * margin
    graph_height = screen_height - 2* margin

    # Bar values
    bar_spacing = 10
    bars_amount = len(keys)
    bar_width = (graph_width - (bars_amount - 1) * bar_spacing) / bars_amount

    # X axis
    turtle.penup()
    turtle.goto(graph_left, graph_bottom)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.forward(graph_width)

    # Y axis
    turtle.penup()
    turtle.goto(graph_left, graph_bottom)
    turtle.setheading(90) # Points turtle up
    turtle.pendown()
    turtle.forward(graph_height)

    # Chatgpt helped create this piece next code
    # Y axis labels
    increments = 5
    values = list(percentages.values())
    max_value = max(values) if values else 1 # How high the tallest bar will be
    for i in range(increments + 1):
        y_val = i * max_value / increments
        y_pos = graph_bottom + (y_val / max_value) * graph_height

        # Graph increment
        turtle.penup()
        turtle.goto(graph_left - 5, y_pos)
        turtle.pendown()
        turtle.goto(graph_left, y_pos)

        # Increment label
        turtle.penup()
        turtle.goto(graph_left - 10, y_pos - 5)
        turtle.write(f'{int(y_val)}', align='right', font=font)

    # Bars
    for i, key in enumerate(keys):
        value = percentages[key]
        bar_height = (value / max_value) * graph_height

        x_start = graph_left + (i * (bar_width + bar_spacing))
        y_start = graph_bottom

        # Draw bar
        turtle.penup()
        turtle.goto(x_start, y_start)
        turtle.pencolor('black')
        turtle.fillcolor('steelblue')
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

        # Bar value text
        turtle.penup()
        turtle.goto(x_start + (bar_width / 2), y_start + bar_height + 5)

        # X label
        turtle.goto(x_start + (bar_width / 2), graph_bottom - 20)
        turtle.write(key, align='center', font=font)

    # Horizontal axis title
    turtle.penup()
    turtle.goto(0, graph_bottom - (margin / 2) - 10)
    turtle.write('ERROR RANGE (%)', align='center', font=axis_font)

    # Vertical axis title
    turtle.penup()
    y = 0
    vertical_text = 'AMOUNT OF PREDICTIONS'
    spacing = font[1] + 2
    for char in vertical_text:
        turtle.goto(graph_left - (margin / 2) - 10, y + (len(vertical_text) * spacing) / 2)
        turtle.write(char, align='center', font=axis_font)
        y -= spacing  # move down for next character

    # Graph title
    turtle.penup()
    turtle.goto(0, graph_bottom + graph_height + 30)
    turtle.write(graph_title, align='center', font=title_font)

    turtle.done()