

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

test = ['01/12/2017',254,0,-5.2,37,2.2,2000,-17.6,0,0,0,'Winter','No Holiday','Yes']
here = test_list_comprehension(test)
print(here)