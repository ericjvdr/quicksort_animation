#
# Eric van der Roest 
# CPSC 335
#
# Quicksort Animation
#


import pygame, sys, time


# initialize the animation and create resources
def init():
    pygame.init()
    Win = pygame.display.set_mode((850, 500))
    pygame.display.set_caption("Quicksort Animation")


def draw(arr):

    # rectangle data
    x = 40
    y = 40
    width = 20

    clock = pygame.time.Clock()
    WIN = pygame.display.set_mode((850, 500))
    WIN.fill((0, 0, 0))

    # draw rectangles for each item in array
    for i in range(len(arr)):
        pygame.draw.rect(WIN, (174, 185, 252), (x + 25 * i, y, width, arr[i] * 7))

    # update portion of screen    
    pygame.display.update()

    # animation speed
    clock.tick(10)


def partition(arr, low, high):

    # index of smaller element 
    i = (low - 1)

    # pivot 
    pivot = arr[high]

    for j in range(low, high):

        # if current index is smaller than pivot 
        if arr[j] <= pivot:

            # increment index of smaller element 
            i = (i + 1)
            arr[i], arr[j] = arr[j], arr[i]

    draw(arr)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)


def quicksort(arr, low, high):
    if low < high:

        # pi is partitioning index
        pi = partition(arr, low, high)

        # sort the partitions
        quicksort(arr, low, pi - 1)
        draw(arr)
        quicksort(arr, pi + 1, high)


def run_animation(arr, n):

    # main loop for the animation 
    while True:

        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # make the most recently drawn screen visible
        pygame.display.flip()

        print(arr)
        quicksort(arr, 0, n - 1)


if __name__ == '__main__':
    init()

    arr = [ 12, 24, 25, 28, 11, 30, 6, 17, 22, 16,
            29, 10, 1, 4, 20, 26, 23, 21, 14, 8,
            7, 18, 9, 5, 19, 2, 3, 13, 27, 15 ]
    n = len(arr)
    
    run_animation(arr, n)