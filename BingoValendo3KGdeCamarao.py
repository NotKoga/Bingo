import tkinter as tk
import random


class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bingo valendo 3Kg de camarão')


        self.ls_num_sort = []


        self.lbl_result = tk.Label(root,text='',font=('Arial', 16))
        self.lbl_result.pack(pady=20)


        self.btn_sortear = tk.Button(root,text="Sortear",command=self.sortear_numeros , font=('Arial', 16))
        self.btn_sortear.pack(pady=10)


        self.btn_reset = tk.Button(root,text="Reiniciar o jogo",command=self.reset_jogo , font=('Arial', 16))
        self.btn_reset.pack(pady=10)


    def sortear_numeros(self):
            if len(self.ls_num_sort) < 75:
                numSort = random.randint(1, 75)
                while numSort in self.ls_num_sort:
                    numSort = random.randint(1, 75)
                self.ls_num_sort.append(numSort)
                self.lbl_result.config(text=', '.join(map(str, self.ls_num_sort)))
            else:
                self.ls_num_sort.clear()
                
                
    def reset_jogo(self):
        self.lbl_result.config(text='')


if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()