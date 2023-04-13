import PySimpleGUI as sg
# sg.Popup("Mi primera ventanita", button_color=('black','red'))
# sg.PopupYesNo("Pimera ventana yes/no")
# sg.PopupOKCancel("Primera venta Ok/cancel")

# texto = sg.PopupGetText('Titulo', 'Ingresa un texto acá...')
# sg.Popup('Resultados', 'Ingresaste el siguiente texto: ', texto)

#sg.Window(title="Hola Mundo!", layout=[[]], margins=(300, 350)).read()

#margins: permite darle un tamaño en pixels a la ventana
#read(): devuelve una tupla con un evento y los valores de todos los elementos 
# de entrada en la ventana

#----------------------------------------------------------------------------

# layout = [[sg.Text("Hola Mundo!")], [sg.Button("OK")]]

# window = sg.Window("Manejo de eventos", layout, margins=(200, 150))

# while True:
#     event, values = window.read()

#     if event == "OK" or event == sg.WIN_CLOSED:
#         break

# window.close()

#WIN_CLOSED: es la opción de cerrar ventana que tienen todas las ventanas
#El programa termina cuando el usuario hace click en "OK" o cuando cierra
#la ventana utilizando la "x"

#----------------------------------------------------------------------------

layout = [ [sg.Text('Ingresá primer valor'), sg.InputText()],
           [sg.Text('Ingresá segundo valor'), sg.InputText()],
           [sg.Button('Ok'), sg.Button('Cancel')] ]

#layout es de tipo list. y dentro de ella, contiene elementos de tipo list.
#por lo tanto, es una lista de listas.

# window = sg.Window("Segunda Demo", layout, margins=(200, 150))

# while True:
#     event, values = window.read()

#     if event == "Cancel" or event == sg.WIN_CLOSED:
#         break
#     print('Datos ingresados: ', values)

# window.close()

#values es de tipo dict, es decir, es un diccionario

#----------------------------------------------------------------------------

# layout = [[sg.Input('Ingresa algo')], 
#           [sg.Listbox(values=('Item 1', 'Item 2', 'Item 3'))],   
#           [sg.OK()]] 

# sg.Window("Elementos básicos", layout, margins=(200, 150)).read()

#----------------------------------------------------------------------------

# sg.ChangeLookAndFeel('DarkAmber')      

# layout = [[sg.Listbox(values=('Item 1', 'Item 2', 'Item 3'), background_color='yellow', size=(20,3)),
#           [sg.Input('Last input')],
#           [sg.ColorChooserButton("  Elegi color")],
#           [sg.OK()]] ]
# sg.Window("Más elementos ", layout, margins=(200, 150)).read()

layout = [[sg.FileBrowse()], [sg.OK()]]

sg.Window("Nueva Ventanita", layout, margins=(150, 200)).read()

