from tkinter import *      
from tkinter import ttk
from random import randint
from datetime import datetime, date


raam = Tk()
raam.title("Küsi")
raam.geometry("300x100")

kas_küsimus = ['Jah.', 'Ei.', 'Võib-olla.']
millal_küsimus = ['Täna.', 'Homme.', 'Lähiajal.', 'See kuu.', 'Mitte kunagi.']
miks_küsimus = ['Sest nii on.', 'Miks mitte.']
kuidas_küsimus = ['Uuri ise välja.', 'Otsi internetist.', 'Küsi sõbralt.', 'Ei tea.', 'Katseta.']
kes_küsimus = ['Küsis?', 'Sinu vanemad.', 'Mitte keegi.', 'Mina.', 'Sina.']

def vastus():
    küs = küsimus.get().lower()
    if not küs:
        tekstisilt.config(text = 'Palun sisesta küsimus')
    elif 'kas' in küs:
        vastus = kas_küsimus[randint(0, len(kas_küsimus) - 1)]
    elif 'millal' in küs or 'kunas' in küs or 'kuna' in küs:
        vastus = millal_küsimus[randint(0, len(millal_küsimus) - 1)]
    elif 'miks' in küs:
        vastus = miks_küsimus[randint(0, len(miks_küsimus) - 1)]
    elif 'kuidas' in küs:
        vastus = kuidas_küsimus[randint(0, len(kuidas_küsimus) - 1)]
    elif 'mis' in küs and 'kell' in küs:
        now = datetime.now()
        kell = now.strftime('%H:%M')
        vastus = 'Kell on ' + kell
    elif 'mitu' in küs or 'kui palju' in küs:
        vastus = randint(0, 20)
    elif 'päev' in küs and 'mis' in küs:
        täna = date.today()
        format_täna = täna.strftime('%d. aprill %Y')
        vastus = 'Täna on ' + format_täna
    elif 'kes' in küs:
        vastus = kes_küsimus[randint(0, len(kes_küsimus) - 1)]
    else:
        vastus = 'Ma ei oska sellele vastata.'
        
        
    tekstisilt.config(text = vastus)
    

küsimus = ttk.Entry(raam)
küsimus.place(x=60, y=7, width=150)

nupp = ttk.Button(raam, text="Küsi", command=vastus)
nupp.place(x=215, y=5, width=50)

tekstisilt = ttk.Label(raam, text="Küsi minult midagi...")
tekstisilt.place(x=90, y=50)



raam.mainloop()