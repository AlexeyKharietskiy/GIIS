import tkinter as tk

from src.model.algorithms.triangulation.FortuneAlgorithm import Voronoi
from view.window import Window



class VoronoiApp(Window):
    RADIUS = 3
    LOCK_FLAG = False

    def __init__(self, master, cont):
        super().__init__(master, cont)
        self.title("Voronoi")
        self.geometry("520x600")

        
        self.frmMain = tk.Frame(self, relief=tk.RAISED, borderwidth=1)
        self.frmMain.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        self.w = tk.Canvas(self.frmMain, width=500, height=500)
        self.w.config(background='white')
        self.w.bind('<Button-1>', self.onDoubleClick)
        self.w.pack(padx=5, pady=5)

        self.frmButton = tk.Frame(self)
        self.frmButton.pack(fill=tk.X, padx=5, pady=5)

        self.btnCalculate = tk.Button(self.frmButton, text='Calculate', width=25, command=self.onClickCalculate)
        self.btnCalculate.pack(side=tk.LEFT, padx=5)
        self.btnClear = tk.Button(self.frmButton, text='Clear', width=25, command=self.onClickClear)
        self.btnClear.pack(side=tk.LEFT, padx=5)

    def pack_all(self):
        self.frmMain.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
        self.w.pack(padx=5, pady=5)
        self.frmButton.pack(fill=tk.X, padx=5, pady=5)
        self.btnCalculate.pack(side=tk.LEFT, padx=5)
        self.btnClear.pack(side=tk.LEFT, padx=5)

    def onClickCalculate(self):
        if not self.LOCK_FLAG:
            self.LOCK_FLAG = True
            try:
                pObj = self.w.find_all()
                points = []
                for p in pObj:
                    coord = self.w.coords(p)
                    points.append((coord[0] + self.RADIUS, coord[1] + self.RADIUS))

                vp = Voronoi(points)
                vp.process()
                lines = vp.get_output()
                self.drawLinesOnCanvas(lines)
                print(lines)
            except Exception as e:
                self.LOCK_FLAG = False

    def onClickClear(self):
        self.LOCK_FLAG = False
        self.w.delete(tk.ALL)

    def onDoubleClick(self, event):
        if not self.LOCK_FLAG:
            self.w.create_oval(event.x - self.RADIUS, event.y - self.RADIUS, event.x + self.RADIUS,
                               event.y + self.RADIUS, fill="red")

    def drawLinesOnCanvas(self, lines):
        for l in lines:
            self.w.create_line(l[0], l[1], l[2], l[3], fill='green', width=2)
