def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):  # it was and
        return f"Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    return f"Rectangle area: {area()}\n" \
           f"Rectangle perimeter: {perimeter()}"  # no space after area


print(rectangle(2, 10))
print(rectangle('2', 10))
