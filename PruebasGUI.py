import subprocess
import sys

if sys.version_info[0] >= 3:
    from tkinter import Tk, Frame, Button, Label
else:
    from Tkinter import Tk, Frame, Button, Label


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(root, width=40).pack()
        self.title = Label(frame, text="", fg="black").pack()
        self.title1 = Label(
            frame,
            text=("Compra De Top-Up:"),
            fg="black",
        ).pack()
        self.run1 = Button(
            frame,
            command=self.run_1,
            text=("Pruebas Sistema Telemercadeo"),
            fg="black",
        ).pack()
        self.title2 = Label(
            frame,
            text=("Run a Test in Firefox:"),
            fg="black",
        ).pack()
        self.run2 = Button(
            frame,
            command=self.run_2,
            text=("pytest my_first_test.py --firefox"),
            fg="black",
        ).pack()
        self.end_title = Label(frame, text="", fg="black").pack()
        self.quit = Button(frame, text="Cerrar", command=frame.quit).pack()

    def run_1(self):
        subprocess.Popen("pytest C:\QA\DYMM-1155\PruebasFinales\SistemaTelemercadeo\PruebasSistemaTelemercadeo.py --dashboard --html=report.html", shell=True)

    def run_2(self):
        subprocess.Popen("pytest my_first_test.py --firefox", shell=True)


if __name__ == "__main__":
    root = Tk()
    root.title("Sistema Pruebas Selenium")
    root.minsize(320, 420)
    app = App(root)
    root.mainloop()
