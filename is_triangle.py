"""
Judge input there values could structure a triangle : )
"""

def is_triangle(side1, side2, side3):
    """
    input type: float, float, float
    return type: boolean
    """
    if side1 > 0 and side2 > 0 and side3 > 0:
        triangle_value_list = sorted([side1, side2, side3])
        flag = False
        if triangle_value_list[0] + triangle_value_list[1] > triangle_value_list[2] and triangle_value_list[2]-triangle_value_list[1] < triangle_value_list[0] and triangle_value_list[2]-triangle_value_list[0] < triangle_value_list[1]:
            flag = True
        return flag
