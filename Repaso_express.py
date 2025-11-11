import  tkinter as tk


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

etiqueta1 = tk.Label(ventana, text="Primer número: ")
etiqueta1.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

etiqueta2 = tk.Label(ventana,text="Segundo número: ")
etiqueta2.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

resultado = tk.Label(ventana, text="El resultado es: ")
resultado.pack(pady=10)


def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        total = num1 + num2
        resultado.config(text=f"El resultado es {total}")
    except ValueError:
        resultado.config(text="ERROR, ingresa números")

def restar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        total = num1- num2
        resultado.config(text=f"El resultado es: {total}")
    except ValueError:
        resultado.config(text=f"ERROR, ingresa números")

def multiplicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        total = num1* num2
        resultado.config(text=f"El resultado es: {total}")
    except ValueError:
        resultado.config(text="ERROR, ingresa números")

def dividir():
    try:
        num1= float(entrada1.get())
        num2 = float(entrada2.get())
        if num2 == 0:
            resultado.config(text=f"ERROR, no se puede dividir entre 0")
        total = num1/num2
        resultado.config(text=f"El resultado es: {total}")
    except ValueError:
        resultado.config(text=f"ERROR, ingresa números")


boton_suma = tk.Button(ventana, text="Suma", command=sumar, bg="white")
boton_suma.pack(pady=5, fill="x", padx=50)

boton_resta = tk.Button(ventana, text="Resta", command=restar, bg="red")
boton_resta.pack(pady=5, fill="x", padx=50)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar, bg="blue")
boton_multiplicar.pack(pady=5, fill="x", padx=50)

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir, fg= "red", bg="black")
boton_dividir.pack(pady=5, fill="x", padx=50)

def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.config("Resultado: ")

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, bg="yellow")
boton_limpiar.pack(pady=5, fill="x", padx=50)

ventana.mainloop()