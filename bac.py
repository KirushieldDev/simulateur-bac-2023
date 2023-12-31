from tkinter import *


def general():
    global speAbandonneeEntry, histGeopEntry, lv1pEntry, lv2pEntry, mathspEntry, emcpEntry, epsEntry, histGeotEntry, lv1tEntry, lv2tEntry, mathstEntry, emctEntry, francaisEntry, spe1Entry, spe2Entry, philoEntry, grandOralEntry, noteFinaleTxtVar, resultTxtVar, mentionTxtVar

    generalTitle = Label(
        window, text="GÉNÉRAL", bg="#123", fg="white", font=("Courrier", 25)
    )
    generalTitle.place(x=545, y=30)

    frameAccueil.pack_forget()

    frameControleContinuPrem = Frame(window, bg="#17406B")
    frameControleContinuTerm = Frame(window, bg="#17406B")
    frameEpreuve = Frame(window, bg="#17406B")

    controleContinuPremTitle = Label(
        window,
        text="Contrôle Continu de Première",
        bg="#123",
        fg="white",
        font=("Courrier", 20),
    )
    controleContinuPremTitle.place(x=71, y=160)

    speAbandonnee = Label(
        frameControleContinuPrem,
        text="Spé abandonnée (coef 8)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    speAbandonnee.grid(row=0, column=0)

    speAbandonneeEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    speAbandonneeEntry.grid(row=0, column=1)

    histGeop = Label(
        frameControleContinuPrem,
        text="Histoire Géographie (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    histGeop.grid(row=1, column=0)

    histGeopEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    histGeopEntry.grid(row=1, column=1)

    lv1p = Label(
        frameControleContinuPrem,
        text="LV1 (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    lv1p.grid(row=2, column=0)

    lv1pEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    lv1pEntry.grid(row=2, column=1)

    lv2p = Label(
        frameControleContinuPrem,
        text="LV2 (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    lv2p.grid(row=3, column=0)

    lv2pEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    lv2pEntry.grid(row=3, column=1)

    mathsp = Label(
        frameControleContinuPrem,
        text="Maths (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    mathsp.grid(row=4, column=0)

    mathspEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    mathspEntry.grid(row=4, column=1)

    emcp = Label(
        frameControleContinuPrem,
        text="EMC (coef 1)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    emcp.grid(row=5, column=0)

    emcpEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    emcpEntry.grid(row=5, column=1)

    controleContinuTermTitle = Label(
        window,
        text="Contrôle Continu de Terminale",
        bg="#123",
        fg="white",
        font=("Courrier", 20),
    )
    controleContinuTermTitle.place(x=465, y=160)

    eps = Label(
        frameControleContinuTerm,
        text="EPS (coef 6)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    eps.grid(row=0, column=0)

    epsEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    epsEntry.grid(row=0, column=1)

    histGeot = Label(
        frameControleContinuTerm,
        text="Histoire Géographie (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    histGeot.grid(row=1, column=0)

    histGeotEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    histGeotEntry.grid(row=1, column=1)

    lv1t = Label(
        frameControleContinuTerm,
        text="LV1 (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    lv1t.grid(row=2, column=0)

    lv1tEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    lv1tEntry.grid(row=2, column=1)

    lv2t = Label(
        frameControleContinuTerm,
        text="LV2 (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    lv2t.grid(row=3, column=0)

    lv2tEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    lv2tEntry.grid(row=3, column=1)

    mathst = Label(
        frameControleContinuTerm,
        text="Maths (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    mathst.grid(row=4, column=0)

    mathstEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    mathstEntry.grid(row=4, column=1)

    emct = Label(
        frameControleContinuTerm,
        text="EMC (coef 1)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    emct.grid(row=5, column=0)

    emctEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    emctEntry.grid(row=5, column=1)

    epreuveTitle = Label(
        window, text="Epreuves passées", bg="#123", fg="white", font=("Courrier", 20)
    )
    epreuveTitle.place(x=885, y=160)

    francais = Label(
        frameEpreuve,
        text="Français (coef 10)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    francais.grid(row=0, column=0)

    francaisEntry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    francaisEntry.grid(row=0, column=1)

    spe1 = Label(
        frameEpreuve,
        text="Spé 1 (coef 16)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    spe1.grid(row=1, column=0)

    spe1Entry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    spe1Entry.grid(row=1, column=1)

    spe2 = Label(
        frameEpreuve,
        text="Spé 2 (coef 16)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    spe2.grid(row=2, column=0)

    spe2Entry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    spe2Entry.grid(row=2, column=1)

    philo = Label(
        frameEpreuve,
        text="Philosophie (coef 8)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    philo.grid(row=3, column=0)

    philoEntry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    philoEntry.grid(row=3, column=1)

    grandOral = Label(
        frameEpreuve,
        text="Grand Oral (coef 10)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    grandOral.grid(row=4, column=0)

    grandOralEntry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    grandOralEntry.grid(row=4, column=1)

    frameControleContinuPrem.place(x=80, y=220)
    frameControleContinuTerm.place(x=480, y=220)
    frameEpreuve.place(x=870, y=220)

    resultsButton = Button(
        window,
        text="Calculer",
        bg="#17406B",
        fg="white",
        font=("Courrier", 19),
        command=calculGeneral,
    )
    resultsButton.pack(side=BOTTOM)

    noteFinaleTxtVar = StringVar()
    noteFinaleTxtVar.set("")

    noteFinaleTxt = Label(
        frameEnd,
        textvariable=noteFinaleTxtVar,
        bg="#123",
        fg="white",
        font=("Courrier", 18),
    )
    noteFinaleTxt.grid(row=0, column=0)

    resultTxtVar = StringVar()
    resultTxtVar.set("")

    resultTxt = Label(
        frameEnd,
        textvariable=resultTxtVar,
        bg="#123",
        fg="white",
        font=("Courrier", 18),
    )
    resultTxt.grid(row=0, column=1, padx=50)

    mentionTxtVar = StringVar()
    mentionTxtVar.set("")

    mentionTxt = Label(
        frameEnd,
        textvariable=mentionTxtVar,
        bg="#123",
        fg="white",
        font=("Courrier", 18),
    )
    mentionTxt.grid(row=0, column=2)


def techno():
    global speAbandonneeEntry, histGeopEntry, lv1pEntry, lv2pEntry, mathspEntry, emcpEntry, epsEntry, histGeotEntry, lv1tEntry, lv2tEntry, mathstEntry, emctEntry, francaisEntry, spe1Entry, spe2Entry, philoEntry, grandOralEntry, noteFinaleTxtVar, resultTxtVar, mentionTxtVar

    technoTitle = Label(
        window, text="TECHNOLOGIE", bg="#123", fg="white", font=("Courrier", 25)
    )
    technoTitle.place(x=500, y=30)

    frameAccueil.pack_forget()

    frameControleContinuPrem = Frame(window, bg="#17406B")
    frameControleContinuTerm = Frame(window, bg="#17406B")
    frameEpreuve = Frame(window, bg="#17406B")

    controleContinuPremTitle = Label(
        window,
        text="Contrôle Continu de Première",
        bg="#123",
        fg="white",
        font=("Courrier", 20),
    )
    controleContinuPremTitle.place(x=71, y=160)

    speAbandonnee = Label(
        frameControleContinuPrem,
        text="Spé abandonnée (coef 8)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    speAbandonnee.grid(row=0, column=0)

    speAbandonneeEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    speAbandonneeEntry.grid(row=0, column=1)

    histGeop = Label(
        frameControleContinuPrem,
        text="Histoire Géographie (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    histGeop.grid(row=1, column=0)

    histGeopEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    histGeopEntry.grid(row=1, column=1)

    lv1p = Label(
        frameControleContinuPrem,
        text="LV1 (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    lv1p.grid(row=2, column=0)

    lv1pEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    lv1pEntry.grid(row=2, column=1)

    lv2p = Label(
        frameControleContinuPrem,
        text="LV2 (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    lv2p.grid(row=3, column=0)

    lv2pEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    lv2pEntry.grid(row=3, column=1)

    mathsp = Label(
        frameControleContinuPrem,
        text="Maths (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    mathsp.grid(row=4, column=0)

    mathspEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    mathspEntry.grid(row=4, column=1)

    emcp = Label(
        frameControleContinuPrem,
        text="EMC (coef 1)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    emcp.grid(row=5, column=0)

    emcpEntry = Entry(
        frameControleContinuPrem,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    emcpEntry.grid(row=5, column=1)

    controleContinuTermTitle = Label(
        window,
        text="Contrôle Continu de Terminale",
        bg="#123",
        fg="white",
        font=("Courrier", 20),
    )
    controleContinuTermTitle.place(x=465, y=160)

    eps = Label(
        frameControleContinuTerm,
        text="EPS (coef 6)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    eps.grid(row=0, column=0)

    epsEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    epsEntry.grid(row=0, column=1)

    histGeot = Label(
        frameControleContinuTerm,
        text="Histoire Géographie (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    histGeot.grid(row=1, column=0)

    histGeotEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    histGeotEntry.grid(row=1, column=1)

    lv1t = Label(
        frameControleContinuTerm,
        text="LV1 (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    lv1t.grid(row=2, column=0)

    lv1tEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    lv1tEntry.grid(row=2, column=1)

    lv2t = Label(
        frameControleContinuTerm,
        text="LV2 (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    lv2t.grid(row=3, column=0)

    lv2tEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    lv2tEntry.grid(row=3, column=1)

    mathst = Label(
        frameControleContinuTerm,
        text="Maths (coef 3)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    mathst.grid(row=4, column=0)

    mathstEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    mathstEntry.grid(row=4, column=1)

    emct = Label(
        frameControleContinuTerm,
        text="EMC (coef 1)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    emct.grid(row=5, column=0)

    emctEntry = Entry(
        frameControleContinuTerm,
        bg="#D1F9F2",
        fg="#17406B",
        font=("Courrier", 16),
        width=5,
    )
    emctEntry.grid(row=5, column=1)

    epreuveTitle = Label(
        window, text="Epreuves passées", bg="#123", fg="white", font=("Courrier", 20)
    )
    epreuveTitle.place(x=885, y=160)

    francais = Label(
        frameEpreuve,
        text="Français (coef 10)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    francais.grid(row=0, column=0)

    francaisEntry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    francaisEntry.grid(row=0, column=1)

    spe1 = Label(
        frameEpreuve,
        text="Spé 1 (coef 16)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    spe1.grid(row=1, column=0)

    spe1Entry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    spe1Entry.grid(row=1, column=1)

    spe2 = Label(
        frameEpreuve,
        text="Spé 2 (coef 16)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    spe2.grid(row=2, column=0)

    spe2Entry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    spe2Entry.grid(row=2, column=1)

    philo = Label(
        frameEpreuve,
        text="Philosophie (coef 4)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    philo.grid(row=3, column=0)

    philoEntry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    philoEntry.grid(row=3, column=1)

    grandOral = Label(
        frameEpreuve,
        text="Grand Oral (coef 14)",
        bg="#17406B",
        fg="white",
        font=("Courrier", 16),
    )
    grandOral.grid(row=4, column=0)

    grandOralEntry = Entry(
        frameEpreuve, bg="#D1F9F2", fg="#17406B", font=("Courrier", 16), width=5
    )
    grandOralEntry.grid(row=4, column=1)

    frameControleContinuPrem.place(x=80, y=220)
    frameControleContinuTerm.place(x=480, y=220)
    frameEpreuve.place(x=870, y=220)

    resultsButton = Button(
        window,
        text="Calculer",
        bg="#17406B",
        fg="white",
        font=("Courrier", 19),
        command=calculTechno,
    )
    resultsButton.pack(side=BOTTOM)

    noteFinaleTxtVar = StringVar()
    noteFinaleTxtVar.set("")

    noteFinaleTxt = Label(
        frameEnd,
        textvariable=noteFinaleTxtVar,
        bg="#123",
        fg="white",
        font=("Courrier", 18),
    )
    noteFinaleTxt.grid(row=0, column=0)

    resultTxtVar = StringVar()
    resultTxtVar.set("")

    resultTxt = Label(
        frameEnd,
        textvariable=resultTxtVar,
        bg="#123",
        fg="white",
        font=("Courrier", 18),
    )
    resultTxt.grid(row=0, column=1, padx=50)

    mentionTxtVar = StringVar()
    mentionTxtVar.set("")

    mentionTxt = Label(
        frameEnd,
        textvariable=mentionTxtVar,
        bg="#123",
        fg="white",
        font=("Courrier", 18),
    )
    mentionTxt.grid(row=0, column=2)


def calculTechno():
    noteSpeAbandonnee = float(speAbandonneeEntry.get())
    noteHistGeop = float(histGeopEntry.get())
    noteLv1p = float(lv1pEntry.get())
    noteLv2p = float(lv2pEntry.get())
    noteMathsp = float(mathspEntry.get())
    noteEmcp = float(emcpEntry.get())

    noteEps = float(epsEntry.get())
    noteHistGeot = float(histGeotEntry.get())
    noteLv1t = float(lv1tEntry.get())
    noteLv2t = float(lv2tEntry.get())
    noteMathst = float(mathstEntry.get())
    noteEmct = float(emctEntry.get())

    noteFrancais = float(francaisEntry.get())
    noteSpe1 = float(spe1Entry.get())
    noteSpe2 = float(spe2Entry.get())
    notePhilo = float(philoEntry.get())
    noteGO = float(grandOralEntry.get())

    if (
        noteSpeAbandonnee < 0
        or noteHistGeop < 0
        or noteLv1p < 0
        or noteLv2p < 0
        or noteMathsp < 0
        or noteEmcp < 0
        or noteEps < 0
        or noteHistGeot < 0
        or noteLv1t < 0
        or noteLv2t < 0
        or noteMathst < 0
        or noteEmct < 0
        or noteFrancais < 0
        or noteSpe1 < 0
        or noteSpe2 < 0
        or notePhilo < 0
        or noteGO < 0
    ):
        noteFinaleTxtVar.set("Erreur dans la saisie des notes")

    else:
        noteControleContinu = (
            (noteSpeAbandonnee * 8)
            + (noteHistGeop * 3)
            + (noteLv1p * 3)
            + (noteLv2p * 3)
            + (noteMathsp * 3)
            + (noteEmcp * 1)
            + (noteEps * 6)
            + (noteHistGeot * 3)
            + (noteLv1t * 3)
            + (noteLv2t * 3)
            + (noteMathst * 3)
            + (noteEmct * 1)
        )
        noteEpreuve = (
            (noteFrancais * 10)
            + (noteSpe1 * 16)
            + (noteSpe2 * 16)
            + (notePhilo * 4)
            + (noteGO * 14)
        )
        noteFinale = (noteControleContinu + noteEpreuve) / 100
        noteFinale = round(noteFinale, 2)
        noteFinaleTxtVar.set(f"Note finale : {noteFinale}")

        if noteFinale < 10:
            resultTxtVar.set("Résultat : Pas admis")
            mentionTxtVar.set("Pas de mention")

        elif noteFinale >= 10 and noteFinale < 12:
            resultTxtVar.set("Résultat : Admis")
            mentionTxtVar.set("Pas de mention")

        elif noteFinale >= 12 and noteFinale < 14:
            resultTxtVar.set("Résultat : Admis")
            mentionTxtVar.set("Mention : Assez Bien")

        elif noteFinale >= 14 and noteFinale < 16:
            resultTxtVar.set("Résultat : Admis")
            mentionTxtVar.set("Mention : Bien")

        else:
            resultTxtVar.set("Résultat : Admis")
            mentionTxtVar.set("Mention : Très Bien")


def calculGeneral():
    noteSpeAbandonnee = float(speAbandonneeEntry.get())
    noteHistGeop = float(histGeopEntry.get())
    noteLv1p = float(lv1pEntry.get())
    noteLv2p = float(lv2pEntry.get())
    noteMathsp = float(mathspEntry.get())
    noteEmcp = float(emcpEntry.get())

    noteEps = float(epsEntry.get())
    noteHistGeot = float(histGeotEntry.get())
    noteLv1t = float(lv1tEntry.get())
    noteLv2t = float(lv2tEntry.get())
    noteMathst = float(mathstEntry.get())
    noteEmct = float(emctEntry.get())

    noteFrancais = float(francaisEntry.get())
    noteSpe1 = float(spe1Entry.get())
    noteSpe2 = float(spe2Entry.get())
    notePhilo = float(philoEntry.get())
    noteGO = float(grandOralEntry.get())

    if (
        noteSpeAbandonnee < 0
        or noteHistGeop < 0
        or noteLv1p < 0
        or noteLv2p < 0
        or noteMathsp < 0
        or noteEmcp < 0
        or noteEps < 0
        or noteHistGeot < 0
        or noteLv1t < 0
        or noteLv2t < 0
        or noteMathst < 0
        or noteEmct < 0
        or noteFrancais < 0
        or noteSpe1 < 0
        or noteSpe2 < 0
        or notePhilo < 0
        or noteGO < 0
    ):
        noteFinaleTxtVar.set("Erreur dans la saisie des notes")

    else:
        noteControleContinu = (
            (noteSpeAbandonnee * 8)
            + (noteHistGeop * 3)
            + (noteLv1p * 3)
            + (noteLv2p * 3)
            + (noteMathsp * 3)
            + (noteEmcp * 1)
            + (noteEps * 6)
            + (noteHistGeot * 3)
            + (noteLv1t * 3)
            + (noteLv2t * 3)
            + (noteMathst * 3)
            + (noteEmct * 1)
        )
        noteEpreuve = (
            (noteFrancais * 10)
            + (noteSpe1 * 16)
            + (noteSpe2 * 16)
            + (notePhilo * 8)
            + (noteGO * 10)
        )
        noteFinale = (noteControleContinu + noteEpreuve) / 100
        noteFinale = round(noteFinale, 2)
        noteFinaleTxtVar.set(f"Note finale : {noteFinale}")

        if noteFinale < 10:
            resultTxtVar.set("Résultat : Pas admis")
            mentionTxtVar.set("Pas de mention")

        elif noteFinale >= 10 and noteFinale < 12:
            resultTxtVar.set("Résultat : Admis")
            mentionTxtVar.set("Pas de mention")

        elif noteFinale >= 12 and noteFinale < 14:
            resultTxtVar.set("Résultat : Admis")
            mentionTxtVar.set("Mention : Assez Bien")

        elif noteFinale >= 14 and noteFinale < 16:
            resultTxtVar.set("Résultat : Admis")
            mentionTxtVar.set("Mention : Bien")

        else:
            resultTxtVar.set("Résultat : Admis")
            mentionTxtVar.set("Mention : Très Bien")


window = Tk()
window.geometry("1200x600")
window.title("Simulateur BAC 2023")
window.config(background="#123")

frameAccueil = Frame(window, bg="#123")

generalButton = Button(
    frameAccueil,
    text="Général",
    bg="#146",
    fg="white",
    font=("Courrier", 20),
    width=20,
    height=3,
    command=general,
)
generalButton.pack(pady=50)

technoButton = Button(
    frameAccueil,
    text="Techno",
    bg="#146",
    fg="white",
    font=("Courrier", 20),
    width=20,
    height=3,
    command=techno,
)
technoButton.pack(pady=50)

frameEnd = Frame(window, bg="#123")

frameEnd.pack(side=BOTTOM, pady=30)
frameAccueil.pack(expand=YES)
window.iconbitmap(r"bacIcon.ico")
window.resizable(width=False, height=False)
window.mainloop()
