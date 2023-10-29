import tkinter as tk
from tkinter import messagebox

# Función para resolver el problema 1
def resolver_problema_1():
    # Los números telefónicos pares deben terminar en dígitos pares (0, 2, 4, 6, 8).
    # El primer dígito no puede ser 0, 1, 8, ni 9, por lo que puede ser del 2 al 7.
    primer_digito_opciones = [str(i) for i in range(2, 8)]
    total_combinaciones = len(primer_digito_opciones) * 10**7
    resultado = f"Para encontrar números telefónicos pares en Guatemala, los pasos son:\n"
    resultado += f"1. El primer dígito puede ser {', '.join(primer_digito_opciones)}.\n"
    resultado += f"2. Los otros 7 dígitos pueden ser cualquiera de los 10 dígitos (0-9).\n"
    resultado += f"3. Por lo tanto, hay {total_combinaciones} números telefónicos pares posibles."
    messagebox.showinfo("Problema 1 - Respuesta", resultado)

# Función para resolver el problema 2
def resolver_problema_2():
    A = set("octubre")  # Cambiar el nombre del mes si es necesario
    B = set("abcdefghij")  # Las primeras 10 letras del abecedario

    resultado = "Para encontrar la intersección de los conjuntos A y B, los pasos son:\n"
    resultado += f"1. A = {' '.join(A)}\n"
    resultado += f"2. B = {' '.join(B)}\n"
    interseccion = A.intersection(B)
    resultado += f"3. La intersección de A y B es {' '.join(interseccion)}."
    messagebox.showinfo("Problema 2 - Respuesta", resultado)

# Función para resolver el problema 3
def resolver_problema_3():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    
    a, b = num1, num2
    resultado = f"Para encontrar el MCD de {a} y {b}, los pasos son:\n"

    # Algoritmo de Euclides
    while b:
        resultado += f"{a} = {a // b} * {b} + {a % b}\n"
        a, b = b, a % b
    
    resultado += f"El MCD es: {a}"
    messagebox.showinfo("Problema 3 - Respuesta", resultado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Resolución de Problemas")
ventana.geometry("400x250")  # Aumenta el tamaño de la ventana

# Botones para resolver problemas
btn_problema_1 = tk.Button(ventana, text="Numeros Telefonicos", command=resolver_problema_1)
btn_problema_2 = tk.Button(ventana, text="Conjuntos", command=resolver_problema_2)
btn_problema_3 = tk.Button(ventana, text="MCD", command=resolver_problema_3)

# Entradas para el problema 3
entry_num1 = tk.Entry(ventana, width=5)
entry_num2 = tk.Entry(ventana, width=5)
label_num1 = tk.Label(ventana, text="Número 1:")
label_num2 = tk.Label(ventana, text="Número 2:")

# Colocar widgets en la ventana
btn_problema_1.pack()
btn_problema_2.pack()
label_num1.pack()
entry_num1.pack()
label_num2.pack()
entry_num2.pack()
btn_problema_3.pack()

ventana.mainloop()
