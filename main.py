
def paint_calc(height, width, cover):
    calculation = (height * width) / cover
    calculation = round(calculation)
    print(calculation + 1)

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

