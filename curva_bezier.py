from tkinter import *
import math

#baseado em https://github.com/NikolaiT/CunningCaptcha/blob/master/python_tests/bezier.py


class Application():
    def __init__(self, master=None):
        self.x = []
        self.y = []
        self.container=Frame(master)
        self.container.pack()

        self.fontePadrao = ("Arial", "10")
        self.intro = Label(self.container, text="Selecione 4 pontos na tela ", fg="blue", font=(self.fontePadrao, "11", "bold"))
        self.intro.pack(side=LEFT)

        self.container2 = Frame(master)
        self.container2["pady"] = 10
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 10
        self.container3.pack()

        self.drawBezier = Button(self.container2, text="Clique para desenhar a curva Bezier", font=(self.fontePadrao), command=self.calculateBezier)
        self.drawBezier.pack()

        self.resetPoints = Button(self.container3, text="Resetar Pontos", font=(self.fontePadrao), command=self.resetPoints)
        self.resetPoints.pack()

        self.curveContainer = Frame(master)
        self.curveContainer["padx"] = 10
        self.curveContainer.pack()

        self.curve = Canvas(self.curveContainer, width=900, height=500)

        self.curve.pack()

        self.initializePoints()

    def calculateBezier(self):
        if(len(self.x) >= 4 and len(self.y) >=4 ):
            self.draw_cubic_bez((self.x[0], self.y[0]), (self.x[1], self.y[1]), (self.x[2], self.y[2]), (self.x[3], self.y[3]))
        else:
            popOut = Toplevel()
            pontos = str(4 - len(self.x))
            label = Label(popOut, text="Ainda falta selecionar "+ pontos +" ponto(s)!", font=("Arial","15"), height=0, width=50)
            label.pack()

    def initializePoints(self):
        #Call the function which get the points the user selected
        self.curve.bind("<Button 1>", self.getPoints)

    def getPoints(self, event):
        self.x.append(event.x)
        self.y.append(event.y)
        print(self.x,self.y)
        print(len(self.x), len(self.y))

    def draw_cubic_bez(self, p1, p2, p3, p4):
        t = 0
        while (t < 1):
            x = self.cubic_bezier_sum(t, (p1[0], p2[0], p3[0], p4[0]))
            y = self.cubic_bezier_sum(t, (p1[1], p2[1], p3[1], p4[1]))
            self.plot_pixel(math.floor(x), math.floor(y))
            t += 0.001

    #Calculate sum for the points given
    def cubic_bezier_sum(self, t, b):
        t2 = math.pow(t, 2)
        t3 = math.pow(t, 3)
        dif_t = 1-t
        dif_t2 = math.pow((1-t), 2)
        dif_t3 = math.pow((1-t), 3)

        return b[0] * dif_t3 + 3 * t * b[1] * dif_t2 + 3*t2*b[2]*dif_t + b[3]*t3

    # Because Canvas doesn't support simple pixel plotting,
    # we need to help us out with a line with length 1 in
    # positive x direction
    def plot_pixel(self, x0, y0):
        self.curve.create_line(x0, y0, x0+1, y0)

    def resetPoints(self):
        self.x = []
        self.y = []
        self.curve.delete("all")


root = Tk()
root.title("Curva de Bezier")
root.geometry("900x500")
root.resizable()
Application(root)
root.mainloop()
