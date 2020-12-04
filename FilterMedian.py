import numpy
from PIL import Image


def median(image, size):
    MatrixPxil = []
    index = size // 2
    matrixImage_final = []
    matrixImage_final = numpy.zeros((len(image),len(image[0])))

    for i in range(len(image)):

        for j in range(len(image[0])):

            for y in range(size):
                if i + y - index < 0 or i + y - index > len(image) - 1:
                        MatrixPxil.append(0)
                else:
                    if j + y - index < 0 or j + index > len(image[0]) - 1:
                        MatrixPxil.append(0)
                    else:
                        for x in range(size):
                            MatrixPxil.append(image[i + y - index][j + x - index])

            MatrixPxil.sort()
            matrixImage_final[i][j] = MatrixPxil[len(MatrixPxil) // 2]
            MatrixPxil = []
    return matrixImage_final


def main():
    img = Image.open("lizard_noisy.png")
    Matrix = numpy.array(img)
    resulte = median(Matrix , 3)
    img1 = Image.fromarray(resulte)
    img1.show()
    Matrix1 = numpy.array(img1)
    resulte1 = median(Matrix1, 5)
    img2 = Image.fromarray(resulte1)
    img2.show()
    Matrix2 = numpy.array(img2)
    resulte2= median(Matrix2, 8)
    img3 = Image.fromarray(resulte2)
    img3.show()

main()