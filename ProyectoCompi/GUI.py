import sys
import tkinter
import tkinter as tk

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
import customtkinter as ctk
from tkinter import *
from tkinter import filedialog as fd

import LineNumbers
from generated.MonkeyLexer import MonkeyLexer
from generated.MonkeyParser import MonkeyParser
from myVisitor import myVisitor


class StdOutRedirect:
    def __init__(self,  text: tk.Text) -> None:
        self._text = text

    def write(self,  out: str) -> None:
        self._text.insert(tk.END,  out)

    def flush(self):  # needed for file like object
        pass

class App():
    def __init__(self):
        ctk.set_appearance_mode("dark")
        self.window = ctk.CTk()
        self.window.title("REPL MONKEY")
        self.window.geometry("1350x600")

        #widgets
        self.Frame_header = ctk.CTkFrame(master=self.window, height=55, bg="snow")
        self.Frame_header.pack(side=TOP, fill=X)
        self.barra = ctk.CTkFrame(master=self.window, width=100, relief=tk.RAISED, bd=2)
        self.barra.pack(side=LEFT, fill=Y)
        self.Frame_right = ctk.CTkFrame(self.window)
        self.Frame_right.grid_rowconfigure(0, weight=1)
        self.Frame_right.grid_columnconfigure(0, weight=1)
        self.tk_textbox = tkinter.Text(self.Frame_right, highlightthickness=0, )
        self.tk_textbox.grid(row=0, column=0, sticky="nsew")
        self.ctk_textbox_scrollbar = ctk.CTkScrollbar(self.Frame_right, command=self.tk_textbox.yview)
        self.ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")
        self.tk_textbox.configure(yscrollcommand=self.ctk_textbox_scrollbar.set, font=("Arial", 12))
        self.In = LineNumbers.LineNumbers(self.window, self.tk_textbox, width=2)
        self.In.pack(side=LEFT, fill=BOTH)
        self.Frame_right.pack(side=LEFT, fill=Y)

        self.Frame_left = ctk.CTkFrame(self.window)
        self.Frame_left.grid_rowconfigure(0, weight=1)
        self.Frame_left.grid_columnconfigure(0, weight=1)
        self.tk_textbox1 = tkinter.Text(self.Frame_left, highlightthickness=0, bg="black", fg="white", insertbackground="white")
        self.tk_textbox1.grid(row=0, column=0, sticky="nsew")
        self.ctk_textbox_scrollbar1 = ctk.CTkScrollbar(self.Frame_left, command=self.tk_textbox1.yview)
        self.ctk_textbox_scrollbar1.grid(row=0, column=1, sticky="ns")
        self.tk_textbox1.configure(yscrollcommand=self.ctk_textbox_scrollbar1.set)
        self.Frame_left.pack(side=LEFT, fill=Y)
        sys.stdout = StdOutRedirect(self.tk_textbox1)

        #buttons
        self.button1 = ctk.CTkButton(master=self.Frame_header, text="Ejecutar", fg_color="green", hover_color="yellowgreen", command=self.button_event)
        self.button1.pack(side=RIGHT)
        self.button3 = ctk.CTkButton(master=self.Frame_header, text=" ", image=PhotoImage(file='eliminar1.png').subsample(5),
                                     hover_color="LightSkyBlue", command=self.cleartextinput, width=7)
        self.button3.pack(side=RIGHT)

        self.button2 = ctk.CTkButton(master=self.barra, text="Open", command=self.open_text_file)
        self.button2.pack(side=TOP)
        self.tk_textbox1.bind("<Return>", self.enter)
        self.tk_textbox1.bind("<Control_R><r>", self.espacio)
    #functions

    def cleartextinput(self): #lIMPIA LA CONSOLA
        self.tk_textbox1.delete("1.0", "end")

    def run(self):
        self.window.mainloop()

    def button_event(self):#permite recibir lo que se encuentra en el TextBox y convertirlo en un archivo
        #.txt para ser procesado
        nombrearch = open("test1.txt", "w", encoding="utf-8")
        nombrearch.write(str(self.tk_textbox.get(1.0, ctk.END)))
        nombrearch.close()
        self.ejecutar("test1.txt")


    def enter(self, event): #permite recibir lo que se encuentra en la consola y convertirlo en un archivo
        #.txt para ser procesado
        nombrearch = open("test2.txt", "w", encoding="utf-8")
        nombrearch.write(str(self.tk_textbox1.get(1.0, ctk.END)))
        nombrearch.close()
        self.ejecutar("test2.txt")

    def espacio(self, event):
        self.tk_textbox1.insert(END, '\n')


    def ejecutar(self, nombre): #instancia el lexer y el parser para enviar el código y que este sea compilado.
        input = FileStream(nombre)
        lexer = MonkeyLexer(input)
        lexer.removeErrorListeners()
        lexer.addErrorListener(self.ThrowingErrorListener())

        stream = CommonTokenStream(lexer)
        parser = MonkeyParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(self.ThrowingErrorListener())

        try:
            tree = parser.program()
            vist = myVisitor()
            vist.visit(tree);
            print("*** Compilacion terminada. ***\n")

        except Exception as e:
            print(e)

    def open_text_file(self): #Permite abrir los archivos del sistema para la búsqueda
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        f = fd.askopenfile(filetypes=filetypes)
        self.tk_textbox.insert('1.0', f.read())

    class ThrowingErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            lista = []
            string = f'line {line-1}: {column}  msj:  {msg}'
            lista.append(string)
            for error in lista:
                print(error)


if __name__ == '__main__':
    Objeto_ventana = App()
    Objeto_ventana.run()
