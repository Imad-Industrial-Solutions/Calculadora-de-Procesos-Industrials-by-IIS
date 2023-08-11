#LLIBRERIES UTILITZADES:
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#DIRECTORIS DE LES FOTOS:
ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#CONFIGURACIÓ DE LA FINESTRA:
window = Tk()
window.title("Calculadora de Procesos Indutrials By Imad Industrial Solutions")
window.geometry("1174x700")
window.configure(bg="#FFFFFF")

#FONS DE LA GUI:
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=1174,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(587.0, 350.0, image=image_image_1)

#TEXT BENVINGUDA:
canvas.create_text(
    12.0,
    16.0,
    anchor="nw",
    text="Benvingut al simulador de processos industrials.\n Aquí podràs simular el teu procés industrial i analitzar-lo!",
    fill="#24386A",
    font=("Inter Regular", 22 * -1)
)
#ENTRADA DE TEXT 1:
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(591.5, 109.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#89ABD8", fg="#000716", highlightthickness=0)
entry_1.place(x=564.0, y=86.0, width=55.0, height=44.0)
#ENTRADA DE TEXT 2:
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(332.5, 297.5, image=entry_image_2)
entry_2 = Text(bd=0, bg="#89ABD8", fg="#000716", highlightthickness=0)
entry_2.place(x=53.0, y=194.0, width=559.0, height=205.0)
entry_2.config(state="normal")  
#ENTRADA DE TEXT 3:
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(336.0, 567.0, image=entry_image_3)
entry_3 = Text(bd=0, bg="#89ABD8", fg="#000716", highlightthickness=0)
entry_3.place(x=60.0, y=448.0, width=552.0, height=236.0)
entry_3.config(state="normal") 

canvas.create_rectangle(848.0, 53.0, 1135.0, 641.0, fill="#89ABD8", outline="")
#TEXT 1:
canvas.create_text(
    30.0,
    102.0,
    anchor="nw",
    text="Quantes estacions vols que tingui la teva industria?",
    fill="#24386A",
    font=("Inter Regular", 20 * -1)
)
#TEXT 2:
canvas.create_text(
    23.0,
    163.0,
    anchor="nw",
    text="Introdueix la producció en unitats/hora (u/h) per cada estació:",
    fill="#24386A",
    font=("Inter Regular", 20 * -1)
)
#TEXT 3:
canvas.create_text(
    275.0,
    416.0,
    anchor="nw",
    text="RESULTATS:",
    fill="#24386A",
    font=("Inter Regular", 20 * -1)
)
#TEXT 4:
canvas.create_text(
    869.0,
    666.0,
    anchor="nw",
    text="Imad Industrial Solutions",
    fill="#24386A",
    font=("Imprima Regular", 24 * -1)
)   
#FOTOS UTILITZADES:

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(994.0, 419.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(991.0, 279.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(991.0, 137.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(991.0, 557.0, image=image_image_5)

#FUNCIÓ PER AL BOTÓ 2:
def button2_clicked():
    num_estacions = int(entry_1.get())
    entry_2.config(state="normal")  
    entry_2.delete("1.0", "end")  
    for i in range(1, num_estacions + 1):
        entry_2.insert("end", f"\nIntrodueix la producció en unitats/hora (u/h) de l'estació {i}: ")
    entry_2.config(state="normal")  

#FUNCIÓ PER AL BOTÓ 1:
def button1_clicked():
    entry_3.config(state="normal")  
    entry_3.delete("1.0", "end")  

    produccions_estacions = entry_2.get("1.0", "end").strip().split("\n")

    n_estacions = len(produccions_estacions)
    temps_cicle = []
    lead_time = []

    for i in range(n_estacions):
        produccio = float(produccions_estacions[i].split(":")[-1].strip())
        calcular_temps_cicle = 60 / produccio
        temps_cicle.append(calcular_temps_cicle)
        lead_time = sum(temps_cicle)

    entry_3.insert("end", "TEMPS DE CICLE:\n")
    for i in range(n_estacions):
        entry_3.insert("end", f"El temps de cicle de l'Estació {i+1}: {temps_cicle[i]:.0f} min/uni\n")

    entry_3.insert("end", f"\nLEAD TIME:\nEl lead time es de: {lead_time:.1f} minuts\n")

    takt_time = max(temps_cicle)
    entry_3.insert("end", f"\nTAKT TIME:\nEl takt tme de l'industria es de: {takt_time} minuts\n")

    coll_de_botella = temps_cicle.index(max(temps_cicle)) + 1
    entry_3.insert("end", f"\nCOLL DE BOTELLA:\nL'estació que esta fen coll de botella es l'estació : {coll_de_botella}     \n")
    entry_3.config(state="normal")  

    wip = lead_time * 1/takt_time
    entry_3.insert("end",f"\nWORK IN PROGRES:\nEl work in progres es de : {wip} unitats\n")
    entry_3.config(state="disabled")

#BOTÓ 1:
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button1_clicked,
    relief="flat"
)
button_1.place(x=671.0, y=274.0, width=106.0, height=48.0)

#BOTÓ 2:
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button2_clicked,
    relief="flat"
)
button_2.place(x=661.0, y=85.0, width=105.0, height=48.0)
window.wm_resizable(False,False)
window.iconbitmap(relative_to_assets("i_i_s_proceses_calculator_logo_akc_icon.ico")) 

window.mainloop()
