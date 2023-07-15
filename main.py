from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap.scrolled import ScrolledFrame
import os
import champs_info
import random

root = Tk()

scrollFrame = ScrolledFrame(root, bootstyle='dark')
scrollFrame.pack(expand=True, fill='both')

def main(scrollFrame):


    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    BG = '#363636'
    FG = 'white'
    secColor = '#AE9666'
    greenBox = '#34A804'
    orangeBox = '#C6A155'
    redBox = '#892222'
    champNames = []

    root.title('LoLdleV2')
    root.geometry(f'{width}x{height}')
    root.state('zoomed')
    root.iconbitmap('window_icon.ico')

    # ----------------------------------------------------IMAGES-------------------------------------------------------------
    infoFrameImage = Image.open('imgs_objects/infoFrame.png').resize((400, 200))
    infoFrameImage = ImageTk.PhotoImage(infoFrameImage)

    inputButtonImage = Image.open('imgs_objects/inputButton.png').resize((50, 50))
    inputButtonImage = ImageTk.PhotoImage(inputButtonImage)

    inputButtonImage_aux = Image.open('imgs_objects/inputButton.png').resize((52, 52))
    inputButtonImage_aux = ImageTk.PhotoImage(inputButtonImage_aux)

    colorIndicatorsImage = Image.open('imgs_objects/colorIndicatorsFrame.png').resize((400, 200))
    colorIndicatorsImage = ImageTk.PhotoImage(colorIndicatorsImage)

    # ----------------------------------------------------IMAGES-------------------------------------------------------------

    # ----------------------------------------------------FUNCTIONS----------------------------------------------------------
    def champsImages():
        global champNames, imageButtons, imagesFrame, imagesName, champNamesLabel
        champNames = []
        imageButtons = []
        champNamesLabel = []
        path = 'champs_imgs'
        fileList = os.listdir(path)
        imagesFrame = Frame(auxRightFrame)
        imagesFrame.pack(side='left', padx=10, anchor='n')
        imagesNameFrame = Frame(auxRightFrame)
        imagesNameFrame.pack(side='left', padx=10, anchor='n')
        for fileName in fileList:
            curImg = Image.open(f'{path}/{fileName}').resize((65, 65))
            curImg = ImageTk.PhotoImage(curImg)
            champId = os.path.splitext(fileName)[0]

            imageButton = Button(imagesFrame, width=55, height=55, cursor='hand2', image=curImg, border=0,
                                 command=lambda champId=champId: selectImg(champId))
            imageButton.pack()
            imageButton.pack_forget()
            imageButton.image = curImg
            imageButton.config(text=champId)

            imagesName = Label(imagesNameFrame, text=champId, font='Arial 14')
            imagesName.pack()
            imagesName.pack_forget()

            champNames.append(champId)
            champNamesLabel.append(imagesName)
            imageButtons.append(imageButton)

        imagesFrame.configure(bg=BG)
        imagesNameFrame.configure(bg=BG)
        imagesName.configure(bg=BG, fg='white')
        return champNames

    def searchChamps(event):
        inputText = champInput.get().lower()
        if inputText:
            for button, name in zip(imageButtons, champNamesLabel):
                champId = button.cget('text')
                champName = name.cget('text')
                if champId.lower().startswith(inputText):
                    button.pack(anchor='n', pady=3)
                else:
                    button.pack_forget()

                if champName.lower().startswith(inputText):
                    name.pack(anchor='w', pady=17)
                else:
                    name.pack_forget()

                name.configure(bg=BG, fg='white')

    def selectImg(champId):
        champname.set(champId)
        champInput.delete(0, END)
        champInput.insert(0, champId)

    def misteriousChamp(champNames):
        toGuessChamp = random.choice(champNames)
        if '’' in toGuessChamp:
            toGuessChamp = toGuessChamp.replace('’', '')
        if "'" in toGuessChamp:
            toGuessChamp = toGuessChamp.replace("'", '')
        if "." in toGuessChamp:
            toGuessChamp = toGuessChamp.replace(".", '')
        if " " in toGuessChamp:
            toGuessChamp = toGuessChamp.replace(" ", '')
        if toGuessChamp == '':
            pass
        else:
            auxDict = getattr(champs_info, toGuessChamp)
            aux = auxDict()
            print(auxDict)
            return aux

    def compareChamps(aux, imageName, gender, position, specie, resource, range, region):
        champsFrame = Frame(mainFrame, bg=BG)
        champsFrame.pack(pady=5, side='top')

        champ_image = imageName
        champ_gender = aux.get('Gender')
        champ_position = aux.get('Position')
        champ_specie = aux.get('Specie')
        champ_resource = aux.get('Resource')
        champ_range = aux.get('Range Type')
        champ_region = aux.get('Region')

        imageChampion = Image.open(f'champs_imgs/{champ_image}.png').resize((91, 84))
        imageChampion = ImageTk.PhotoImage(imageChampion)

        imageButton = Button(champsFrame, width=89, height=82, image=imageChampion)
        imageButton.pack(side='left', padx=2, pady=3)
        imageButton.image = imageChampion

        genderButton = Button(champsFrame, width=12, height=5, text=f'{gender}', font='Arial 9 bold',
                              fg='black')
        genderButton.pack(side='left', padx=2, pady=3)
        if champ_gender == gender:
            genderButton.configure(bg=greenBox)

        else:
            genderButton.configure(bg=redBox)

        positionButton = Button(champsFrame, width=12, height=5, text=f'{position}', font='Arial 9 bold',
                                fg='black')
        positionButton.pack(side='left', padx=2, pady=3)

        position = position.split(',\n')
        champ_position = champ_position.split(',\n')
        try:
            if champ_position == position:
                positionButton.configure(bg=greenBox)
            elif any(word in champ_position for word in position[0].split()):
                positionButton.configure(bg=orangeBox)
            elif any(word in champ_position for word in position[1].split()):
                positionButton.configure(bg=orangeBox)
            elif any(word in champ_position for word in position[2].split()):
                positionButton.configure(bg=orangeBox)
            else:
                positionButton.configure(bg=redBox)
        except:
            positionButton.configure(bg=redBox)

        specieButton = Button(champsFrame, width=12, height=5, text=f'{specie}', font='Arial 9 bold',
                              fg='black')
        specieButton.pack(side='left', padx=2, pady=3)

        specie = specie.split(',\n')
        champ_specie = champ_specie.split(',\n')
        try:
            if champ_specie == specie:
                specieButton.configure(bg=greenBox)
            elif any(word in champ_specie for word in specie[0].split()):
                specieButton.configure(bg=orangeBox)
            elif any(word in champ_specie for word in specie[1].split()):
                specieButton.configure(bg=orangeBox)
            elif any(word in champ_specie for word in specie[2].split()):
                specieButton.configure(bg=orangeBox)
            else:

                specieButton.configure(bg=redBox)
        except:
            specieButton.configure(bg=redBox)

        resourceButton = Button(champsFrame, width=12, height=5, text=f'{resource}', font='Arial 9 bold',
                                fg='black')
        resourceButton.pack(side='left', padx=2, pady=3)

        if champ_resource == resource:
            resourceButton.configure(bg=greenBox)

        else:
            resourceButton.configure(bg=redBox)

        rangeTypeButton = Button(champsFrame, width=12, height=5, text=f'{range}', font='Arial 9 bold',
                                 fg='black')
        rangeTypeButton.pack(side='left', padx=2, pady=3)

        range = range.split(',\n')
        champ_range = champ_range.split(',\n')

        try:
            if champ_range == range:
                rangeTypeButton.configure(bg=greenBox)
            elif any(word in champ_range for word in range[0].split()):
                rangeTypeButton.configure(bg=orangeBox)
            elif any(word in champ_range for word in range[1].split()):
                rangeTypeButton.configure(bg=orangeBox)
            elif any(word in champ_range for word in range[2].split()):
                rangeTypeButton.configure(bg=orangeBox)
            else:
                rangeTypeButton.configure(bg=redBox)
        except:
            rangeTypeButton.configure(bg=redBox)

        regionButton = Button(champsFrame, width=12, height=5, text=f'{region}', font='Arial 9 bold',
                              fg='black', bg=greenBox)
        regionButton.pack(side='left', padx=2, pady=3)

        region = region.split(',\n')
        champ_region = champ_region.split(',\n')

        try:

            if champ_region == region:
                regionButton.configure(bg=greenBox)
            elif any(word in champ_region for word in region[0].split()):
                regionButton.configure(bg=orangeBox)
            elif any(word in champ_region for word in region[1].split()):
                regionButton.configure(bg=orangeBox)
            elif any(word in champ_region for word in region[2].split()):
                regionButton.configure(bg=orangeBox)
            else:
                regionButton.configure(bg=redBox)
        except:
            regionButton.configure(bg=redBox)

        champsFrame.configure(bg=BG)

        ifCorrect(imageName, imageChampion, champ_gender, gender, champ_position, position, champ_specie, specie,
                  champ_resource, resource, champ_range, range, champ_region, region)

    def ifCorrect(imageName, imageChampion, champ_gender, gender, champ_position, position, champ_specie, specie,
                  champ_resource, resource, champ_range, range, champ_region, region):

        if champ_gender == gender and champ_position == position and champ_specie == specie and champ_resource == resource and champ_range == range and champ_region == region:
            correctGuess = Toplevel(root)
            windowWidth = round(root.winfo_screenwidth() / 2) - 260
            windowHeigth = round(root.winfo_screenheight() / 2) - 290
            correctGuess.geometry(f'600x400+{windowWidth}+{windowHeigth}')
            correctGuess.title('Correto!!')

            frame = Frame(correctGuess)
            frame.pack(expand=True, fill='both')

            text = Label(frame, text='Parabéns', font='Arial 30')
            text.pack(pady=15)

            champImage = Label(frame, image=imageChampion)
            champImage.pack(pady=10)
            champImage.image = imageChampion

            correctChampName = Label(frame, text=imageName, font='Arial 20')
            correctChampName.pack(pady=5)

            restartButton = Button(frame, text='Novo Jogo', font='Arial 20', command=lambda:restartGame(scrollFrame, correctGuess))
            restartButton.pack(pady=25)

            frame.configure(bg=BG)
            text.configure(bg=BG, fg=FG)
            champImage.configure(bg=BG)
            correctChampName.configure(bg=BG, fg=FG)
            restartButton.configure(fg=FG, cursor='hand2')


        else:
            pass

    def getInfo(aux):
        entry = champInput.get()
        imageName = entry
        champNames.remove(entry)
        if '’' in entry:
            entry = entry.replace('’', '')
        if "'" in entry:
            entry = entry.replace("'", '')
        if "." in entry:
            entry = entry.replace(".", '')
        if " " in entry:
            entry = entry.replace(" ", '')
        if entry == '':
            pass
        else:
            auxDict = getattr(champs_info, entry)
            champInfo = auxDict()

            gender = champInfo.get('Gender')
            position = champInfo.get('Position')
            specie = champInfo.get('Specie')
            resource = champInfo.get('Resource')
            range = champInfo.get('Range Type')
            region = champInfo.get('Region')

            compareChamps(aux, imageName, gender, position, specie, resource, range, region)

            if imageName:
                for button, name in zip(imageButtons, champNamesLabel):
                    champId = button.cget('text')
                    champName = name.cget('text')
                    if champId == imageName:
                        imageButtons.remove(button)
                        button.destroy()
                    if champName == imageName:
                        champNamesLabel.remove(name)
                        name.destroy()
                champInput.delete(0, END)
            else:
                pass
    def restartGame(scrollFrame, correctGuess):
        correctGuess.destroy()
        for widget in scrollFrame.winfo_children():
            widget.destroy()
        for name in champNames:
            champNames.remove(name)
        for button in imageButtons:
            button.destroy()
        for nameLabel in champNamesLabel:
            nameLabel.destroy()
        main(scrollFrame)
    # ----------------------------------------------------FUNCTIONS----------------------------------------------------------


    chunkyFrame = Canvas(scrollFrame, width=width, height=height)
    chunkyFrame.pack(fill='both', expand=True)

    auxLeftFrame = Frame(chunkyFrame, bg=BG)
    auxLeftFrame.pack(side='left', fill='both')

    mainFrame = Frame(chunkyFrame, bg=BG)
    mainFrame.pack(side='left', fill='both', expand=True)

    auxRightFrame = Frame(chunkyFrame, bg=BG)
    auxRightFrame.pack(side='left', fill='both')

    mainTitle = Label(mainFrame, text='LoLdle V2', font='Arial 40', fg=FG)
    mainTitle.pack(pady=40)

    infoText = Label(mainFrame, image=infoFrameImage)
    infoText.pack(pady=10)

    champ_inputFrame = Frame(auxRightFrame)
    champ_inputFrame.pack(pady=5)

    champInput = Entry(champ_inputFrame, font='Arial 14', width=27)
    champInput.pack(side='left', pady=10, padx=5)
    champInput.bind('<KeyRelease>', searchChamps)
    searchChamps(None)

    champname = StringVar()

    champNames = champsImages()
    aux = misteriousChamp(champNames)

    inputButton = Button(champ_inputFrame, image=inputButtonImage, borderwidth=0, takefocus=0, cursor='hand2',
                         activebackground=BG, command=lambda: getInfo(aux))
    inputButton.pack(side='left', padx=5)

    champsFrameFirst = Frame(mainFrame)
    champsFrameFirst.pack()

    colorIndicators = Label(auxLeftFrame, image=colorIndicatorsImage)
    colorIndicators.pack()

    whiteSpace = Label(auxLeftFrame)
    whiteSpace.pack(pady=400)

    root.configure(bg=BG)
    chunkyFrame.configure(bg=BG)
    auxLeftFrame.configure(bg=BG)
    mainFrame.configure(bg=BG)
    auxRightFrame.configure(bg=BG)
    mainTitle.configure(bg=BG, fg=FG)
    infoText.configure(bg=BG)
    champ_inputFrame.configure(bg=BG)
    champInput.configure(bg=BG, fg=FG)
    inputButton.configure(bg=BG, activebackground=BG, highlightbackground=BG)
    champsFrameFirst.configure(bg=BG)
    colorIndicators.configure(bg=BG)
    whiteSpace.configure(bg=BG)

    root.mainloop()

if __name__ == '__main__':
    main(scrollFrame)