def find_linear_regression_line(points):
    # Separate points into X and y to fit LinearRegression model
    points_x = [[point[0]] for point in points]
    points_y = [point[1] for point in points]
    print("X points: ", points_x, "Length: ", len(points_x))
    print("Y points: ", points_y, "Length: ", len(points_y))

    # Fit points to LinearRegression line
    clf = LinearRegression().fit(points_x, points_y)

    # Get parameters from line
    coef = clf.coef_[0]
    intercept = clf.intercept_
    print("Coefficients: ", coef, "Intercept: ", intercept)
    return coef, intercept

def intersection_x(coef1, intercept1, coef2, intercept2):
    """Returns x-coordinate of intersection of two lines."""
    x = (intercept2-intercept1)/(coef1-coef2)
    return x

def draw_linear_regression_line(coef1, intercept1, intersection_x, imshape=[540,960]):

    # Get starting and ending points of regression line, ints.
    point_one = (int(intersection_x), int(intersection_x * coef1 + intercept1))
    print("Point one: ", point_one)
    point_two = (imshape[1], int(imshape[1] * coef1 + intercept1))
    print("Point one: ", point_one, "Point two: ", point_two)
    # Draw line using cv2.line
    cv2.line(img, point_one, point_two, color, thickness)