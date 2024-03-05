import tkinter as tk
from tkinter import messagebox

def verificar_interruptores():
    messagebox.showinfo("Instruções", "Você pode ligar e desligar os interruptores quantas vezes quiser. Tente descobrir qual interruptor controla cada lâmpada.")

def verificar_lampadas():
    estado_lampada1 = var_lampada1.get()
    estado_lampada2 = var_lampada2.get()
    estado_lampada3 = var_lampada3.get()

    if estado_lampada1 == estado_lampada2 == estado_lampada3:
        messagebox.showinfo("Resultado", "Todas as lâmpadas estão no mesmo estado. Tente novamente.")
    elif estado_lampada1 == estado_lampada2:
        messagebox.showinfo("Resultado", "O interruptor 3 controla a lâmpada 1.")
    elif estado_lampada1 == estado_lampada3:
        messagebox.showinfo("Resultado", "O interruptor 2 controla a lâmpada 1.")
    else:
        messagebox.showinfo("Resultado", "O interruptor 1 controla a lâmpada 1.")

root = tk.Tk()
root.title("Descobrir Interruptores e Lâmpadas")

btn_instrucoes = tk.Button(root, text="Instruções", command=verificar_interruptores)
btn_instrucoes.pack(pady=10)

frame_interruptores_lampadas = tk.Frame(root)
frame_interruptores_lampadas.pack()

lbl_lampada1 = tk.Label(frame_interruptores_lampadas, text="Lâmpada 1")
lbl_lampada1.grid(row=0, column=0)
var_lampada1 = tk.IntVar()
check_lampada1 = tk.Checkbutton(frame_interruptores_lampadas, variable=var_lampada1)
check_lampada1.grid(row=0, column=1)

lbl_lampada2 = tk.Label(frame_interruptores_lampadas, text="Lâmpada 2")
lbl_lampada2.grid(row=1, column=0)
var_lampada2 = tk.IntVar()
check_lampada2 = tk.Checkbutton(frame_interruptores_lampadas, variable=var_lampada2)
check_lampada2.grid(row=1, column=1)

lbl_lampada3 = tk.Label(frame_interruptores_lampadas, text="Lâmpada 3")
lbl_lampada3.grid(row=2, column=0)
var_lampada3 = tk.IntVar()
check_lampada3 = tk.Checkbutton(frame_interruptores_lampadas, variable=var_lampada3)
check_lampada3.grid(row=2, column=1)

btn_verificar = tk.Button(root, text="Verificar", command=verificar_lampadas)
btn_verificar.pack(pady=10)

root.mainloop()
