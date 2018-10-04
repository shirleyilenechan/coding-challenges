def flip_and_invert_image(A):
    image_flip = []
    for row in A:
        inverse = row[::-1]
        invert = []
        for num in inverse:
            if num == 1:
                invert.append(0)
            else:
                invert.append(1)
        image_flip.append(invert)
