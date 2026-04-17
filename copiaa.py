import tkinter as tk
from tkinter import messagebox
import math

# ---------------- CONFIGURACIÓN ----------------
COLOR_FONDO = "#1F302B"
COLOR_TEXTO = "white"
COLOR_BOTON = "#2E4F4F"
COLOR_BOTON_SEL = "#3A7F7F"

# ---------------- FÓRMULAS ----------------
areas = {
    "Física Clásica": {
        "Velocidad (v = d / t)": "velocidad",
        "Aceleración (a = Δv / t)": "aceleracion",
        "Posición MRUA (x = x₀ + v₀t + ½at²)": "posicion_mrua",
        "Velocidad final MRUA (v = v₀ + at)": "vfinal_mrua",
        "Caída libre (h = ½gt²)": "caida",
        "Fuerza (F = m·a)": "newton",
        "Energía potencial (Ep = mgh)": "epotencial",
        "Energía cinética (Ec = ½mv²)": "ecinetica",
        "Fricción (F = μN)": "friccion"
    },
    "Oscilaciones y Ondas": {
        "Velocidad instantánea (v = ωAcosωt)": "vinst",
        "Período (T = 1/f)": "periodo",
        "Aceleración centrípeta (ac = v²/r)": "acentripeta",
        "Número de onda (k = 2π/λ)": "numonda",
        "Velocidad de fase (v = λf)": "vfase"
    },
    "Electromagnetismo": {
        "Campo eléctrico (E = F/q)": "campo",
        "Potencia eléctrica (P = VI)": "pelec",
        "E = V / d": "campov",
        "Ley de Coulomb": "coulomb",
        "F = qE": "felectrica"
    },
    "Termodinámica": {
        "Calor (Q = mcΔT)": "calor",
        "Trabajo (W = PΔV)": "wtermo",
        "Gas ideal (PV = nRT)": "ideal",
        "Eficiencia (η = W/Q)": "eficiencia",
        "Primera ley (ΔU = Q − W)": "primeraley"
    }
}

FORMULAS_3_DATOS = {
    "posicion_mrua", "ideal", "calor", "coulomb"
}

# ---------------- CÁLCULO ----------------
def calcular():
    try:
        clave = formula_actual
        x = float(entry1.get())
        y = float(entry2.get())
        z = float(entry3.get()) if clave in FORMULAS_3_DATOS else None

        if clave == "velocidad": r = x / y
        elif clave == "aceleracion": r = x / y
        elif clave == "posicion_mrua": r = x + y + 0.5 * z**2
        elif clave == "vfinal_mrua": r = x + y * z
        elif clave == "caida": r = 0.5 * 9.81 * x**2
        elif clave == "newton": r = x * y
        elif clave == "epotencial": r = x * 9.81 * y
        elif clave == "ecinetica": r = 0.5 * x * y**2
        elif clave == "friccion": r = x * y

        elif clave == "vinst": r = x * math.cos(y)
        elif clave == "periodo": r = 1 / x
        elif clave == "acentripeta": r = x**2 / y
        elif clave == "numonda": r = 2 * math.pi / x
        elif clave == "vfase": r = x * y

        elif clave == "campo": r = x / y
        elif clave == "pelec": r = x * y
        elif clave == "campov": r = x / y
        elif clave == "coulomb": r = 9e9 * x * y / z**2
        elif clave == "felectrica": r = x * y

        elif clave == "calor": r = x * y * z
        elif clave == "wtermo": r = x * y
        elif clave == "ideal": r = (x * 8.314 * y) / z
        elif clave == "eficiencia": r = x / y
        elif clave == "primeraley": r = x - y

        resultado.config(text=f"Resultado: {r:.4e}")

    except:
        messagebox.showerror("Error", "Datos incorrectos")

# ---------------- INTERFAZ ----------------
root = tk.Tk()
root.title("Calculadora de Física – SI")
root.geometry("950x620")
root.configure(bg=COLOR_FONDO)

tk.Label(
    root,
    text="Calculadora de Física – Sistema Internacional",
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    font=("Segoe UI", 16, "bold")
).pack(pady=10)

frame_areas = tk.Frame(root, bg=COLOR_FONDO)
frame_areas.pack()

frame_principal = tk.Frame(root, bg=COLOR_FONDO)
frame_principal.pack(pady=10)

frame_formulas = tk.Frame(frame_principal, bg=COLOR_FONDO)
frame_formulas.grid(row=0, column=0, padx=20)

frame_datos = tk.Frame(frame_principal, bg=COLOR_FONDO)
frame_datos.grid(row=0, column=1, padx=20, sticky="n")

formula_actual = None
botones_formulas = []

def seleccionar_formula(nombre, clave, boton):
    global formula_actual
    formula_actual = clave

    for b in botones_formulas:
        b.config(bg=COLOR_BOTON)

    boton.config(bg=COLOR_BOTON_SEL)

    if clave in FORMULAS_3_DATOS:
        mostrar_dato3()
    else:
        ocultar_dato3()

def mostrar_dato3():
    label3.grid()
    entry3.grid()

def ocultar_dato3():
    label3.grid_remove()
    entry3.grid_remove()
    entry3.delete(0, tk.END)

def mostrar_area(area):
    for widget in frame_formulas.winfo_children():
        widget.destroy()
    botones_formulas.clear()

    for texto, clave in areas[area].items():
        b = tk.Button(
            frame_formulas,
            text=texto,
            bg=COLOR_BOTON,
            fg="white",
            font=("Arial", 11),
            width=38,
            pady=6,
            command=lambda t=texto, c=clave, bt=None: seleccionar_formula(t, c, bt)
        )
        b.config(command=lambda t=texto, c=clave, bt=b: seleccionar_formula(t, c, bt))
        b.pack(pady=4)
        botones_formulas.append(b)

for area in areas:
    tk.Button(
        frame_areas,
        text=area,
        font=("Arial", 11, "bold"),
        command=lambda a=area: mostrar_area(a)
    ).pack(side="left", padx=8)

# ---------------- DATOS ----------------
tk.Label(frame_datos, text="Dato 1:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Arial", 11)).grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(frame_datos, font=("Arial", 11))
entry1.grid(row=1, column=0)

tk.Label(frame_datos, text="Dato 2:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Arial", 11)).grid(row=2, column=0, sticky="w")
entry2 = tk.Entry(frame_datos, font=("Arial", 11))
entry2.grid(row=3, column=0)

label3 = tk.Label(frame_datos, text="Dato 3:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Arial", 11))
label3.grid(row=4, column=0, sticky="w")
entry3 = tk.Entry(frame_datos, font=("Arial", 11))
entry3.grid(row=5, column=0)

label3.grid_remove()
entry3.grid_remove()

tk.Button(
    frame_datos,
    text="Calcular",
    font=("Arial", 11, "bold"),
    command=calcular
).grid(row=6, column=0, pady=10)

resultado = tk.Label(
    frame_datos,
    text="Resultado:",
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    font=("Arial", 11, "bold")
)
resultado.grid(row=7, column=0)

# ---------------- MARCA DE AGUA ----------------
tk.Label(
    root,
    text="Christian G. Pech Hu.",
    bg=COLOR_FONDO,
    fg="#AAAAAA",
    font=("Calibri", 9, "italic")
).place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

root.mainloop()
