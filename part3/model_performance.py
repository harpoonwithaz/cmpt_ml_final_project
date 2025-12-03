# =====================================
# Author(s): Oliver Tadaniewicz and Laurenzo Maddatu
# Date: 11/24/2025
# Description: Module to calculate model performance by comparing predicted values to actual values, 
# and visualize the predictions in the error percentage ranges.
# =====================================

import turtle
from typing import Dict

def calculate_model_performance(actual_values: list, predicted_values) -> Dict[str, int]:
    '''Function that calculates the error percentage of model from actual values and predicted values for each prediction
    
    Args:
        actual_values (list): list of output test values.
        predicted_values: predictions from model.

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
                percentage_error = abs((abs(actual_values[i] - predicted_values[i]) / actual_values[i]) * 100)
                
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
        percentages (dict): Containing error percentages for each prediction.
        graph_title (str): Title of window, and at the top of the graph
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
    turtle.colormode(255)
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

        # ----- COLOR GRADIENT LOGIC -----
        # Color by error-range midpoint using a green->yellow->red gradient.
        # 0% -> bright green, 100%+ -> bright red.
        if key == '100+':
            fill = (255, 0, 0)  # Bright red for worst errors
        else:
            parts = key.split('-')
            try:
                low = int(parts[0])
                high = int(parts[1])
            except (ValueError, IndexError):
                low, high = 0, 100
            midpoint = (low + high) / 2
            ratio = midpoint / 100.0  # 0.0 to 1.0
            
            # Enhanced gradient: Green -> Yellow -> Orange -> Red
            if ratio < 0.5:
                # First half: Green to Yellow (0% to 50% error)
                # Green stays high, red increases
                r = int(ratio * 2 * 255)  # 0 to 255
                g = 255  # Stay at max green
                b = 0
            else:
                # Second half: Yellow to Red (50% to 100% error)
                # Red stays high, green decreases
                r = 255  # Stay at max red
                g = int((1.0 - ratio) * 2 * 255)  # 255 to 0
                b = 0
            
            fill = (r, g, b)
        # ----------------------------

        x_start = graph_left + (i * (bar_width + bar_spacing))
        y_start = graph_bottom

        # Draw bar
        turtle.penup()
        turtle.goto(x_start, y_start)
        turtle.pencolor('black')
        turtle.fillcolor(fill)
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

def calculate_accuracy_metrics(percentages: dict) -> dict:
    """
    EXTENSION 1: Calculate comprehensive accuracy metrics from error percentages.
    
    Args:
        percentages (dict): Error percentage distribution
        
    Returns:
        dict: Various accuracy metrics including mean error, median range, and accuracy thresholds
    """
    metrics = {}
    
    # Total predictions
    total = sum(percentages.values())
    metrics['total_predictions'] = total
    
    if total == 0:
        return metrics
    
    # Calculate predictions within acceptable ranges
    metrics['within_10_percent'] = percentages['0-10']
    metrics['within_20_percent'] = percentages['0-10'] + percentages['10-20']
    metrics['within_30_percent'] = sum(percentages[k] for k in ['0-10', '10-20', '20-30'])
    
    # Calculate percentages
    metrics['accuracy_10_pct'] = (metrics['within_10_percent'] / total) * 100
    metrics['accuracy_20_pct'] = (metrics['within_20_percent'] / total) * 100
    metrics['accuracy_30_pct'] = (metrics['within_30_percent'] / total) * 100
    
    # Estimate weighted mean error
    weighted_sum = 0
    for key, count in percentages.items():
        if key == '100+':
            midpoint = 105  # Estimate for 100+ range
        else:
            parts = key.split('-')
            low, high = int(parts[0]), int(parts[1])
            midpoint = (low + high) / 2
        weighted_sum += midpoint * count
    
    metrics['mean_error_estimate'] = weighted_sum / total if total > 0 else 0
    
    return metrics

def print_performance_summary(percentages: dict, metrics: dict):
    """
    EXTENSION 2: Print a formatted summary of model performance.
    
    Args:
        percentages (dict): Error percentage distribution
        metrics (dict): Calculated accuracy metrics
    """
    print('\n' + '='*60)
    print('MODEL PERFORMANCE SUMMARY')
    print('='*60)
    
    print(f'\nTotal Predictions: {metrics["total_predictions"]}')
    print(f'Estimated Mean Error: {metrics["mean_error_estimate"]:.2f}%')
    
    print('\n--- Accuracy Thresholds ---')
    print(f'Predictions within 10% error:  {metrics["within_10_percent"]:>4} ({metrics["accuracy_10_pct"]:.1f}%)')
    print(f'Predictions within 20% error:  {metrics["within_20_percent"]:>4} ({metrics["accuracy_20_pct"]:.1f}%)')
    print(f'Predictions within 30% error:  {metrics["within_30_percent"]:>4} ({metrics["accuracy_30_pct"]:.1f}%)')
    
    
    print('='*60 + '\n')

def compare_prediction_ranges(actual_values: list, predicted_values: list) -> dict:
    """
    EXTENSION 3: Analyze how well predictions match the actual value ranges.
    
    Args:
        actual_values (list): Actual test values
        predicted_values (list): Predicted values
        
    Returns:
        dict: Statistics about prediction ranges vs actual ranges
    """
    if len(actual_values) != len(predicted_values) or len(actual_values) == 0:
        return {}
    
    comparison = {
        'over_predictions': 0,  # Predicted higher than actual
        'under_predictions': 0,  # Predicted lower than actual
        'exact_matches': 0,  # Exactly correct (rare)
        'avg_over_amount': 0,
        'avg_under_amount': 0,
        'max_over': 0,
        'max_under': 0
    }
    
    over_amounts = []
    under_amounts = []
    
    for actual, predicted in zip(actual_values, predicted_values):
        diff = predicted - actual
        
        if abs(diff) < 0.01:  # Close enough to exact
            comparison['exact_matches'] += 1
        elif diff > 0:
            comparison['over_predictions'] += 1
            over_amounts.append(diff)
            comparison['max_over'] = max(comparison['max_over'], diff)
        else:
            comparison['under_predictions'] += 1
            under_amounts.append(abs(diff))
            comparison['max_under'] = max(comparison['max_under'], abs(diff))
    
    if over_amounts:
        comparison['avg_over_amount'] = sum(over_amounts) / len(over_amounts)
    if under_amounts:
        comparison['avg_under_amount'] = sum(under_amounts) / len(under_amounts)
    
    return comparison

def print_prediction_bias(comparison: dict, total: int):
    """
    EXTENSION 4: Print analysis of prediction bias (over/under prediction tendencies).
    
    Args:
        comparison (dict): Comparison statistics from compare_prediction_ranges
        total (int): Total number of predictions analyzed
    """
    if not comparison or total == 0:
        return
    
    # Calculate actual total from comparison data
    actual_total = comparison['over_predictions'] + comparison['under_predictions'] + comparison['exact_matches']
    
    print('\n' + '='*60)
    print('PREDICTION BIAS ANALYSIS')
    print('='*60)
    
    over_pct = (comparison['over_predictions'] / actual_total) * 100
    under_pct = (comparison['under_predictions'] / actual_total) * 100
    exact_pct = (comparison['exact_matches'] / actual_total) * 100
    
    print(f'\nTotal predictions analyzed: {actual_total}')
    print(f'\nOver-predictions:  {comparison["over_predictions"]:>4} ({over_pct:.1f}%)')
    print(f'Under-predictions: {comparison["under_predictions"]:>4} ({under_pct:.1f}%)')
    print(f'Exact matches:     {comparison["exact_matches"]:>4} ({exact_pct:.1f}%)')
    
    if comparison['over_predictions'] > 0:
        print(f'\nAverage over-prediction amount:  {comparison["avg_over_amount"]:.2f}')
        print(f'Maximum over-prediction:         {comparison["max_over"]:.2f}')
    
    if comparison['under_predictions'] > 0:
        print(f'\nAverage under-prediction amount: {comparison["avg_under_amount"]:.2f}')
        print(f'Maximum under-prediction:        {comparison["max_under"]:.2f}')
    
    # Determine bias
    if over_pct > under_pct + 10:
        print('\n⚠ Model tends to OVER-PREDICT (predicts higher than actual)')
    elif under_pct > over_pct + 10:
        print('\n⚠ Model tends to UNDER-PREDICT (predicts lower than actual)')
    else:
        print('\n✓ Model shows balanced prediction (no strong bias)')
    
    print('='*60 + '\n')