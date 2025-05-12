#Task # 1. Read lab manual for details.
def sort_matrix_by_row(matrix):
    new_lst = []
    for row in matrix:
        for i in range(len(row) - 1):
            min = i
            for j in range(i + 1, len(row)):
                if row[j] < row[min]:
                    min = j
            row[i], row[min] = row[min], row[i]
        new_lst.append(row)
    # Use selection sort to solve this problem,
    # return new_lst.
    return new_lst

#Task # 2. Read lab manual for details.
# We have the following rectangles records in a list of dictionaries.
rectangles = [{ "ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"  },
             { "ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue" },
             { "ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
             { "ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
             ]

def sort_rectangles(title):
    for i in range(1, len(rectangles)):
        j = i
        while j >= 1 and rectangles[j][title] < rectangles[j - 1][title]:
            rectangles[j], rectangles[j - 1] = rectangles[j - 1], rectangles[j]
            j -= 1
    return rectangles

    # Using insertion sort to solve this problem.
    # sort by title.
    # return rectangles.
