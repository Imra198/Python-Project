from graphics import *

def finalPatch(basePoint, win, colour):
    baseX = basePoint.getX()
    baseY = basePoint.getY()

    for i in range(10):
        square = Rectangle(Point(baseX + i * 5, baseY + i * 5),
                           Point(baseX + 100 - i * 5, baseY + 100 - i * 5))
        square.draw(win)
        square.setFill(colour)

def penultimatePatch(basePoint, win, colour):
    baseX = basePoint.getX()
    baseY = basePoint.getY()

    for i in range(0, 20, 5):
        rects = [
            Rectangle(Point(baseX + i, baseY), Point(baseX + i + 5, baseY + 20)),
            Rectangle(Point(baseX + 40 + i, baseY), Point(baseX + 45 + i, baseY + 20)),
            Rectangle(Point(baseX + 80 + i, baseY), Point(baseX + 85 + i, baseY + 20)),
            Rectangle(Point(baseX + 20 + i, baseY + 20), Point(baseX + 25 + i, baseY + 40)),
            Rectangle(Point(baseX + 60 + i, baseY + 20), Point(baseX + 65 + i, baseY + 40)),
            Rectangle(Point(baseX + i, baseY + 40), Point(baseX + i + 5, baseY + 60)),
            Rectangle(Point(baseX + 40 + i, baseY + 40), Point(baseX + 45 + i, baseY + 60)),
            Rectangle(Point(baseX + 80 + i, baseY + 40), Point(baseX + 85 + i, baseY + 60)),
            Rectangle(Point(baseX + 20 + i, baseY + 60), Point(baseX + 25 + i, baseY + 80)),
            Rectangle(Point(baseX + 60 + i, baseY + 60), Point(baseX + 65 + i, baseY + 80)),
            Rectangle(Point(baseX + i, baseY + 80), Point(baseX + i + 5, baseY + 100)),
            Rectangle(Point(baseX + 40 + i, baseY + 80), Point(baseX + 45 + i, baseY + 100)),
            Rectangle(Point(baseX + 80 + i, baseY + 80), Point(baseX + 85 + i, baseY + 100)),
        ]
        for rect in rects:
            rect.draw(win)
            rect.setFill(colour)

    for i in range(0, 20, 5):
        rects2 = [
            Rectangle(Point(baseX + 20, baseY + i), Point(baseX + 40, baseY + i + 5)),
            Rectangle(Point(baseX + 60, baseY + i), Point(baseX + 80, baseY + i + 5)),
            Rectangle(Point(baseX, baseY + 20 + i), Point(baseX + 20, baseY + 25 + i)),
            Rectangle(Point(baseX + 40, baseY + 20 + i), Point(baseX + 60, baseY + 25 + i)),
            Rectangle(Point(baseX + 80, baseY + 20 + i), Point(baseX + 100, baseY + 25 + i)),
            Rectangle(Point(baseX + 20, baseY + 40 + i), Point(baseX + 40, baseY + 45 + i)),
            Rectangle(Point(baseX + 60, baseY + 40 + i), Point(baseX + 80, baseY + 45 + i)),
            Rectangle(Point(baseX, baseY + 60 + i), Point(baseX + 20, baseY + 65 + i)),
            Rectangle(Point(baseX + 40, baseY + 60 + i), Point(baseX + 60, baseY + 65 + i)),
            Rectangle(Point(baseX + 80, baseY + 60 + i), Point(baseX + 100, baseY + 65 + i)),
            Rectangle(Point(baseX + 20, baseY + 80 + i), Point(baseX + 40, baseY + 85 + i)),
            Rectangle(Point(baseX + 60, baseY + 80 + i), Point(baseX + 80, baseY + 85 + i)),
        ]
        for rect in rects2:
            rect.draw(win)
            rect.setFill(colour)

def antepenultimatePatch():
    size = 5
    validColours = ['red', 'green', 'blue', 'magenta', 'orange', 'cyan']
    listColour = []

    while len(listColour) < 3:
        colour = input("Please enter a colour (red, green, blue, magenta, orange, cyan): ").lower()
        matched = False
        for valid in validColours:
            if colour == valid or (len(colour) > 0 and colour[0] == valid[0]):
                listColour.append(valid)
                matched = True
                break
        if not matched:
            print(f"{colour} is invalid. Please try again.")

    colour1, colour2, colour3 = listColour

    win = GraphWin("AntepenultimatePatch", size * 100, size * 100)

    for y in range(0, size * 100, 100):
        for x in range(0, size * 100, 100):
            basePoint = Point(x, y)
            if x == 0:
                penultimatePatch(basePoint, win, colour1)
            elif x == 100 and y in [100, 200, 300, 400]:
                penultimatePatch(basePoint, win, colour3)
            elif x == 200 and y in [200, 300, 400]:
                penultimatePatch(basePoint, win, colour1)
            elif x == 300 and y in [300, 400]:
                penultimatePatch(basePoint, win, colour3)
            elif x == 400 and y == 400:
                penultimatePatch(basePoint, win, colour1)
            else:
                finalPatch(basePoint, win, colour2)

    win.getMouse()
    win.close()

def runFinalPatch():
    win = GraphWin("Final Patch", 200, 200)
    basePoint = Point(10, 10)
    colour = input("Enter a colour for finalPatch: ").lower()
    finalPatch(basePoint, win, colour)
    win.getMouse()
    win.close()

def runPenultimatePatch():
    win = GraphWin("Penultimate Patch", 200, 200)
    basePoint = Point(10, 10)
    colour = input("Enter a colour for penultimatePatch: ").lower()
    penultimatePatch(basePoint, win, colour)
    win.getMouse()
    win.close()

def main():
    print("Choose which patch function to run:")
    print("1: finalPatch")
    print("2: penultimatePatch")
    print("3: antepenultimatePatch")

    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == '1':
        runFinalPatch()
    elif choice == '2':
        runPenultimatePatch()
    elif choice == '3':
        antepenultimatePatch()
    else:
        print("Invalid choice. Please run the program again and enter 1, 2, or 3.")

if __name__ == "__main__":
    main()