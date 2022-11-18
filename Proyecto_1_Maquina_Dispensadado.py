#Proyecto Programado 1 Python
#Hecho por Manuel Zapata/ Astrid/ Karen
#Modulos usados Tkinter, time.

#Importación de Modulos para el manejo de interfaz
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import time
from datetime import date

from timeit import default_timer
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

#Definición de la Ventana Principal del Menú
ventana =Tk()
ventana.title("Máquina Dispensadora")
ventana.configure(background="#CCCCFF")
ventana.geometry("1000x650")
ventana.resizable(False,False)
transaccion=0

#Definición de ventanas secundarias y sus funciones
def comprar_w(): #Funcion de venta y cobro de productos
    ventana.withdraw()
    comprarWindow=Toplevel()
    comprarWindow.title("Comprar/Buy")
    comprarWindow.minsize(800,550)
    comprarWindow.configure(background="#CCCCFF")
    comprarWindow.resizable(width=NO,height=NO)
    lienzo=Canvas(comprarWindow,width=700,height=400,bg="#CCCCFF")
    lienzo.place(x=50,y=60)
    #Aca van las funciones para la ventana de ventas
    
    
    def Data():#Esta funcion creara la matriz de datos para estar trabajando el archivo txt de productos
        a_file = open("archivo.txt", "r")
        list_of_lists = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            list_of_lists.append(line_list)
        
        return list_of_lists
        
    def Pagar():#Funcion para generar ventana de metodo de pago del producto, así como el vuelto
        comprarWindow.withdraw()
        ventanaPago=Toplevel()
        ventanaPago.title("Pagar/Pay")
        ventanaPago.minsize(600,550)
        ventanaPago.configure(background="#CCCCFF")
        ventanaPago.resizable(width=NO,height=NO)
        #print("Seleccion de producto: " + str(var.get()))
        lienzo=Canvas(ventanaPago,width=500,height=400,bg="#CCCCFF")
        lienzo.place(x=50,y=60)
        def finalizarCompra():#Funcion que finaliza la compra y genera el vuelto de la persona, luego se regresa a ventana principal
            tipo_moneda=moneda.get()
            if tipo_moneda==1:
                print("tipo de moneda seleccionada: "+str(tipo_moneda))
            elif tipo_moneda==2:
               print("tipo de moneda seleccionada: "+str(tipo_moneda))
            elif tipo_moneda==3:
                print("tipo de moneda seleccionada: "+str(tipo_moneda))

            a_file = open("archivo.txt", "r")#Se abre el archivo para ser leído y generar una matriz de datos

            list_of_lists = []
            for line in a_file:
                stripped_line = line.strip()
                line_list = stripped_line.split()
                list_of_lists.append(line_list)
                #print(list_of_lists)
            a_file.close()


            archivo=open("archivo.txt","w")#Se crea el método de escritura para editar el archivo
            pos=len(list_of_lists)
            option=var.get()
            
            for i in range(pos):
                if option!=i:
                    line=archivo.writelines(str(list_of_lists[i][0])+" "+
                    str(list_of_lists[i][1])+" "+
                    str(list_of_lists[i][2])+" "+
                    str(list_of_lists[i][3])+" "+
                    str(list_of_lists[i][4])+" "+
                    str(list_of_lists[i][5])+" "+
                    str(list_of_lists[i][6])+"\n")
                else:
                    line=archivo.writelines(str(list_of_lists[i][0])+" "+
                    str(list_of_lists[i][1])+" "+
                    str(int(list_of_lists[i][2])-1)+" "+  #Acá se resta el producto vendido
                    str(list_of_lists[i][3])+" "+
                    str(list_of_lists[i][4])+" "+
                    str(list_of_lists[i][5])+" "+
                    str(int(list_of_lists[i][6])+int(list_of_lists[i][5]))+"\n")#Acá se suma el precio a las ventas totales del producto
            archivo.close()



            opcion=moneda.get()
            pos=var.get()
            vuelto=0
            datos=Data()
            pago=0
            #print("VEEEERRRRRR: "+str(opcion))

            try:
                if opcion==1:
                    #print("Billete de mil")
                    vuelto=1000-int(datos[pos][5])
                    #print(vuelto)
                    pago=1000
                    messagebox.showinfo(message="Venta exitosa, su vuelto es: "+str(vuelto), title="vuelto")
                elif opcion==2:
                    #print("Billete de 500")
                    vuelto=500-int(datos[pos][5])
                    #print(vuelto)
                    pago=500
                    messagebox.showinfo(message="Venta exitosa, su vuelto es: "+str(vuelto), title="vuelto")
                elif opcion==3:
                    #print("Moneda de 500")
                    vuelto=500-int(datos[pos][5])
                    #print(vuelto)
                    pago=500
                    messagebox.showinfo(message="Venta exitosa, su vuelto es: "+str(vuelto), title="vuelto")
            except:
                messagebox.showinfo(message="Error", title="vuelto")
            #print("VUELTO "+str(vuelto))
            #print(list_of_lists)

            new=open("movimientos.txt","a")#Se crea el archivo de movimientos
            global transaccion
            today = date.today()
            transaccion+=1
            fecha=today.strftime("%m/%d/%y")
            t=time.localtime()
            tiempo=time.strftime("%H:%M", t)
            
            line=new.writelines("EN "+str(transaccion)+" "+fecha+" "+tiempo +" "+str(datos[pos][0])+" "+str(datos[pos][1])+" "+str(1)+" "
                                +str(int(datos[pos][3])-int(datos[pos][2]))+" "+str(datos[pos][5])+" "+str(pago)+" "+str(vuelto)+" "+str(datos[pos][2])
                                +" "+str(datos[pos][6])+"\n")
            new.close()
            
            ventanaPago.destroy()
            ventana.deiconify()##Reaparece la ventana principal
            
        def boton_pago():#Este boton se activa para realizar el pago cuando se selecciona un producto de entrada
            opcion=moneda.get()
            pos=var.get()
            vuelto=0
            datos=Data()
            if opcion==0:
                botonHome = Button(ventanaPago, text="Pagar/Pay", command=finalizarCompra,bg="#BF1134",fg="white",font=("Helvetica",15),state="disable")
                botonHome.place(x=50,y=475)
            else:
                botonHome = Button(ventanaPago, text="Pagar/Pay", command=finalizarCompra,bg="#BF1134",fg="white",font=("Helvetica",15),state="normal")
                botonHome.place(x=50,y=475)
            
                    
                    
            
        
          
        #Variabe de tipo mondeda
        moneda=IntVar()
        #Seleccion de método de Pago billete de mil, billete de 500 y moneda de 500
        radiobutton1=tk.Radiobutton(lienzo,text="Billete ₡1000",bg="#CCCCFF",  variable=moneda, value=1, command=boton_pago)
        radiobutton1.deselect()
        radiobutton1.place(x=10,y=20)
        radiobutton2=tk.Radiobutton(lienzo,text="Billete ₡500",bg="#CCCCFF",  variable=moneda, value=2, command=boton_pago)
        radiobutton2.deselect()
        radiobutton2.place(x=10,y=50)
        radiobutton3=tk.Radiobutton(lienzo,text="Moneda ₡500",bg="#CCCCFF",  variable=moneda, value=3, command=boton_pago)
        radiobutton3.deselect()
        radiobutton3.place(x=10,y=80)

        label1=tk.Label(ventanaPago,text="Seleccione el tipo de Pago",font=("Times New Roman","15"),foreground="Black",width=25, height=1, bg="#CCCCFF")
        label1.place(x=15,y=30)
        productos=Data()
        label2=tk.Label(lienzo,text="Monto a Pagar: "+str(productos[var.get()][5]),font=("Times New Roman","15"),foreground="Black",width=30, height=1, bg="#CCCCFF")
        label2.place(x=30,y=350)
        label3=tk.Label(lienzo,text="Producto a Comprar: "+productos[var.get()][1],font=("Times New Roman","15"),foreground="Black",width=30, height=1, bg="#CCCCFF")
        label3.place(x=20,y=250)
        label4=tk.Label(lienzo,text="Disponible: "+ productos[var.get()][2],font=("Times New Roman","15"),foreground="Black",width=30, height=1, bg="#CCCCFF")
        label4.place(x=20,y=300)
        
            

        ventanaPago.mainloop()
        
    def close():#Funcion para cerrar el programa
        comprarWindow.destroy()
        ventana.deiconify()##Reaparece la ventana principal
    def GetVariable():#Funcion que captura el codigo del producto a comprar y habilita el boton de compra
        opcion=var.get()
        if opcion==0:
            botonHome = Button(comprarWindow, text="Pagar", command=close,bg="#BF1134",fg="white",font=("Helvetica",15),state="disable")
            botonHome.place(x=50,y=475)
        else:
            botonPagar=Button(comprarWindow, text="Pagar", command=Pagar,bg="#BF1134",fg="white",font=("Helvetica",15),state="normal")
            botonPagar.place(x=50,y=475)
            
            
        
        
    

    
        
    a_file = open("archivo.txt", "r")#Leyendo el archivo de texto de productos disponibles

    m_datos = [] #Variable que lee el archivo de texto con los productos disponibles
    for line in a_file:#Ciclo que genera una matriz con los datos leidos del archivo .txt de los producto disponibles
        stripped_line = line.strip()
        line_list = stripped_line.split()
        m_datos.append(line_list)
    #print("-----Lista Generada------")
    #print(m_datos)
    #print(type(m_datos[1][2]))
    a_file.close()

    
    var=IntVar()
   
    #Etiquetas para la ventana de Compras
    
    label1=tk.Label(comprarWindow,text="Producto/Product",font=("Times New Roman","10"),foreground="Black",width=15, height=1, bg="#CCCCFF")
    label1.place(x=52,y=35)
    label2=tk.Label(comprarWindow,text="Precio/Price",font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label2.place(x=185,y=35)
    label3=tk.Label(comprarWindow,text="Producto/Product",font=("Times New Roman","10"),foreground="Black",width=15, height=1, bg="#CCCCFF")
    label3.place(x=400,y=35)
    label4=tk.Label(comprarWindow,text="Precio/Price",font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label4.place(x=540,y=35)
    label5=tk.Label(comprarWindow,text="Disponible",font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label5.place(x=280,y=35)
    label6=tk.Label(comprarWindow,text="Disponible",font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label6.place(x=635,y=35)
    label7=tk.Label(lienzo,text=m_datos[1][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label7.place(x=215,y=20)
    label8=tk.Label(lienzo,text=m_datos[2][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label8.place(x=215,y=50)
    label9=tk.Label(lienzo,text=m_datos[3][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label9.place(x=215,y=80)
    label10=tk.Label(lienzo,text=m_datos[4][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label10.place(x=215,y=110)
    label11=tk.Label(lienzo,text=m_datos[5][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label11.place(x=215,y=140)
    label12=tk.Label(lienzo,text=m_datos[6][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label12.place(x=215,y=170)
    label13=tk.Label(lienzo,text=m_datos[7][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label13.place(x=215,y=200)
    label14=tk.Label(lienzo,text=m_datos[8][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label14.place(x=215,y=230)
    label15=tk.Label(lienzo,text=m_datos[9][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label15.place(x=560,y=20)
    label16=tk.Label(lienzo,text=m_datos[10][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label16.place(x=560,y=50)
    label17=tk.Label(lienzo,text=m_datos[11][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label17.place(x=560,y=80)
    label18=tk.Label(lienzo,text=m_datos[12][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label18.place(x=560,y=110)
    label19=tk.Label(lienzo,text=m_datos[13][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label19.place(x=560,y=140)
    label20=tk.Label(lienzo,text=m_datos[14][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label20.place(x=560,y=170)
    label21=tk.Label(lienzo,text=m_datos[15][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label21.place(x=560,y=200)
    label22=tk.Label(lienzo,text=m_datos[9][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label22.place(x=560,y=230)

    
    #Definición de botones en ventana de compras
    
    
    botonHome = Button(comprarWindow, text="Cancelar/Cancel", command=close,bg="#BF1134",fg="white",font=("Helvetica",15),state="normal")
    botonHome.place(x=590,y=475)
    radiobutton1=tk.Radiobutton(lienzo,text="1 Coca Lata                ₡500",bg="#CCCCFF",  variable=var, value=1, command=GetVariable)
    radiobutton1.deselect()
    radiobutton1.place(x=10,y=20)
    radiobutton2 = tk.Radiobutton(lienzo,text="2 Coca Lata Light      ₡500",bg="#CCCCFF", variable=var, value=2, command=GetVariable)
    radiobutton2.deselect()
    radiobutton2.place(x=10,y=50)
    radiobutton3 = tk.Radiobutton(lienzo,text="3 Coca Desechable   ₡1000",bg="#CCCCFF", variable=var, value=3, command=GetVariable)
    radiobutton3.deselect()
    radiobutton3.place(x=10,y=80)
    radiobutton4 = tk.Radiobutton(lienzo,text="4 Fanta Lata               ₡500",bg="#CCCCFF", variable=var, value=4, command=GetVariable)
    radiobutton4.deselect()
    radiobutton4.place(x=10,y=110)
    radiobutton5 = tk.Radiobutton(lienzo,text="5 Fanta Desechable  ₡500",bg="#CCCCFF", variable=var, value=5, command=GetVariable)
    radiobutton5.deselect()
    radiobutton5.place(x=10,y=140)
    radiobutton6 = tk.Radiobutton(lienzo,text="6 Pepsi Lata               ₡500",bg="#CCCCFF", variable=var, value=6, command=GetVariable)
    radiobutton6.deselect()
    radiobutton6.place(x=10,y=170)
    radiobutton7 = tk.Radiobutton(lienzo,text="7 Pepsi Desechable  ₡500", bg="#CCCCFF",variable=var, value=7, command=GetVariable)
    radiobutton7.deselect()
    radiobutton7.place(x=10,y=200)
    radiobutton8 = tk.Radiobutton(lienzo,text="8 Gin Lata                  ₡500", bg="#CCCCFF",variable=var, value=8, command=GetVariable)
    radiobutton8.deselect()
    radiobutton8.place(x=10,y=230)
    radiobutton9 = tk.Radiobutton(lienzo,text="9 Coca Light                   ₡500", bg="#CCCCFF",variable=var, value=9, command=GetVariable)
    radiobutton9.deselect()
    radiobutton9.place(x=350,y=20)
    radiobutton10 = tk.Radiobutton(lienzo,text="10 Fresco Leche              ₡500", bg="#CCCCFF",variable=var, value=10, command=GetVariable)
    radiobutton10.deselect()
    radiobutton10.place(x=350,y=50)
    radiobutton11 = tk.Radiobutton(lienzo,text="11 Galleta Chiki               ₡500", bg="#CCCCFF",variable=var, value=11, command=GetVariable)
    radiobutton11.deselect()
    radiobutton11.place(x=350,y=80)
    radiobutton12 = tk.Radiobutton(lienzo,text="12 Pinguino                     ₡500", bg="#CCCCFF",variable=var, value=12, command=GetVariable)
    radiobutton12.deselect()
    radiobutton12.place(x=350,y=110)
    radiobutton13 = tk.Radiobutton(lienzo,text="13 Platanitos verdes       ₡500", bg="#CCCCFF",variable=var, value=13, command=GetVariable)
    radiobutton13.deselect()
    radiobutton13.place(x=350,y=140)
    radiobutton14 = tk.Radiobutton(lienzo,text="14 Platanitos maduros   ₡500", bg="#CCCCFF",variable=var, value=14, command=GetVariable)
    radiobutton14.deselect()
    radiobutton14.place(x=350,y=170)
    radiobutton15 = tk.Radiobutton(lienzo,text="15 Takis                            ₡500", bg="#CCCCFF",variable=var, value=15, command=GetVariable)
    radiobutton15.deselect()
    radiobutton15.place(x=350,y=200)
    radiobutton16 = tk.Radiobutton(lienzo,text="16 Papas                          ₡500", bg="#CCCCFF",variable=var, value=16, command=GetVariable)
    radiobutton16.deselect()
    radiobutton16.place(x=350,y=230)
    
    


    comprarWindow.mainloop()


def password():#Se genera la ventana para la captura de la contrase del adminiostrador
    ventana.withdraw()
    ventana_pasword=Toplevel()
    ventana_pasword.title("Administrador/Administrator")
    ventana_pasword.minsize(300,250)
    ventana_pasword.configure(background="#CCCCFF")
    ventana_pasword.resizable(width=NO,height=NO)
    password=StringVar()


    #Se definen ventanas para la ventana de administrador, así como funciones de esta parte.
    def contraseña():#Funcion que verifica la contraseña del administrador
        contraseña="admin"
        p=password.get()
        if contraseña==p:
            messagebox.showinfo(message="Contraseña correcta: ", title="Administrador")
            ventana_pasword.destroy()
            ventana_admin()
        else:
            messagebox.showinfo(message="Contraseña Incorrecta: ", title="Administrador")

    def ventana_admin():#Ventana con las opciones del administrador
        ventana.withdraw()
        ventana_admin=Toplevel()
        ventana_admin.title("ADMINISTRADOR")
        ventana_admin.minsize(730,600)
        ventana_admin.configure(background="#CCCCFF")
        ventana_admin.resizable(width=NO,height=NO)

        #Se definen botones y labels para esta seccion del código
        #creacion de frame
        frame_admin=Frame(ventana_admin)
        frame_admin.configure(background="#CCCCFF")
        frame_admin.pack(fil=BOTH, expand=1)
        #creacion de un lienzo o canvas para para administrador
        my_canvas=Canvas(frame_admin,width=600,height=400,bg="#CCCCFF")
        #my_canvas.configure(background="#CCCCFF")
        #my_canvas.pack(side=RIGHT,fill=BOTH,expand=1)
        my_canvas.pack(expand=1)
        my_canvas.place(x=50,y=60)

        #lienzo=Canvas(ventanaPago,width=500,height=400,bg="#CCCCFF")
        #lienzo.place(x=50,y=60)
        #Creacion del scroll bar
        my_scrollbar=ttk.Scrollbar(frame_admin,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        #Configuracion del canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        #Creacion de otro frame dentro del canva
        second_frame=Frame(my_canvas)
        #Agregar el nuevo frame a la ventana administrador
        my_canvas.create_window((0,0),window=second_frame,anchor="nw")
        #Botones de ventana admin
        opcion=IntVar()

        #Funciones de los botones de la ventana administrador
        def cerrar_Admin():
            ventana_admin.destroy()
            ventana.deiconify()
        def Reset():
            archivo=open("movimientos.txt","w")
            line=archivo.writelines("Tipo #Transaccion Date Time Code Descripcion Cantidad Vendidas Monto Pago Vuelto Existencia Ventas"+"\n")
            archivo.close()
            ventana_admin.destroy()
            messagebox.showinfo(message="Datos Reiniciados", title="Administrador")
            ventana.deiconify()

        def Venta_R():#Resumen de ventas diarias
            a_file = open("movimientos.txt", "r")#Leyendo el archivo de texto de productos disponibles

            m_datos = [] #Variable que lee el archivo de texto con los productos disponibles
            for line in a_file:#Ciclo que genera una matriz con los datos leidos del archivo .txt de los producto disponibles
                stripped_line = line.strip()
                line_list = stripped_line.split()
                m_datos.append(line_list)
            #print("-----Lista Generada------")
            #print(m_datos)
            #print(type(m_datos[1][2]))
            a_file.close()
            pos=len(m_datos)
            for i in range(pos):
                tk.Label(second_frame,text=m_datos[i][4]+" "+m_datos[i][5]+" "+m_datos[i][11]+" "+m_datos[i][7]+" "+m_datos[i][12]
                                ,font=("Helvetica",10),foreground="Black",
                                width=70, height=1, bg="#CCCCFF").grid(row=i,column=0)

        def Venta_D():#Ventas detalladas 
            a_file = open("movimientos.txt", "r")#Leyendo el archivo de texto de productos disponibles

            m_datos = [] #Variable que lee el archivo de texto con los productos disponibles
            for line in a_file:#Ciclo que genera una matriz con los datos leidos del archivo .txt de los producto disponibles
                stripped_line = line.strip()
                line_list = stripped_line.split()
                m_datos.append(line_list)
          
            a_file.close()
            pos=len(m_datos)
            for i in range(pos):
                tk.Label(second_frame,text=m_datos[i][4]+" "+m_datos[i][5]+" "+m_datos[i][1]+" "+m_datos[i][2]+" "+m_datos[i][3]
                         +" "+m_datos[i][6]+" "+m_datos[i][8],font=("Helvetica",10),foreground="Black",width=70, height=1, bg="#CCCCFF").grid(row=i,column=0)
            
            
            
            
            
        
        
        boton_reset=Button(ventana_admin,text="Corte/Reset",font=("Helvetica",12),background="Magenta",command=Reset)#.grid(row=10,column=20)
        boton_reset.place(x=50,y=500)
        boton_Apagar=Button(ventana_admin,text="Apagar/Off",font=("Helvetica",12),background="Magenta",command=ventana.destroy)#.grid(row=12,column=20)
        boton_Apagar.place(x=210,y=500)
        boton_VentaR=Button(ventana_admin,text="Venta/Resume",font=("Helvetica",12),background="Magenta",command=Venta_R)#.grid(row=14,column=20)
        boton_VentaR.place(x=350,y=500)
        boton_VentaD=Button(ventana_admin,text="Detallada/Detailed",font=("Helvetica",12),background="Magenta",command=Venta_D)#.grid(row=16,column=20)
        boton_VentaD.place(x=510,y=500)
        boton_return=Button(ventana_admin,text="Regresar/Return",font=("Helvetica",12),background="Magenta",command=cerrar_Admin)#.grid(row=16,column=20)
        boton_return.place(x=50,y=550)
        
        #Labels
        label=tk.Label(ventana_admin,text="Administrador/Administrator",font=("Helvetica",20),foreground="Black",width=30, height=1, bg="#CCCCFF")#.grid(row=500,column=200)
        label.place(x=120,y=10)
        
        
        
        


        
        
        
        


        
        

    def close():#Ventana para cerrar la ventana pasword
        ventana_pasword.destroy()
        ventana_admin()
    #Botones para la captura y verificacion de la contraseña de administrador
    label=tk.Label(ventana_pasword,text="Ingrese contraseña/ Enter pasword",foreground="Black",width=30, height=1, bg="#CCCCFF")
    label.place(x=40,y=50)
    E_password=Entry(ventana_pasword,show="*",textvariable=password,width=20)
    E_password.place(x=85,y=80)
    boton_pasword=Button(ventana_pasword,text="Ingresar",font=("Helvetica",12),background="Magenta",command=contraseña)
    boton_pasword.place(x=110,y=120)


    ventana_pasword.mainloop()#Loop de la ventana password de ingresos a datos de administrador

        
def Ventana_about():#Se define la venta about del creador de la aplicacion
    ventana.withdraw()
    ventana_about=Toplevel()
    ventana_about.title("Acerca de/About")
    ventana_about.minsize(800,650)
    ventana_about.configure(background="#CCCCFF")
    ventana_about.resizable(width=NO,height=NO)
    #Definicion de fucion cerrar para ventana aboout
    def cerrar_about():
        ventana_about.destroy()
        ventana.deiconify()



    #Creacion de etiquetas para la ventana about
    Label=tk.Label(ventana_about,text="Country/País: Costa Rica",font=("Times New Roman","15"),foreground="Black",width=30, height=1, bg="#CCCCFF")
    Label.place(x=230,y=20)
    Label2=tk.Label(ventana_about,text="Universidad de Costa Rica/ Ingeniería Electrica",font=("Times New Roman","15"),foreground="Black",width=50, height=1, bg="#CCCCFF")
    Label2.place(x=120,y=50)
    Label3=tk.Label(ventana_about,text="Programación Bajo Plataformas Abiertas",font=("Times New Roman","15"),foreground="Black",width=30, height=1, bg="#CCCCFF")
    Label3.place(x=230,y=80)
    Label4=tk.Label(ventana_about,text="II Semestre 2022",font=("Times New Roma","15"),foreground="Black",width=30, height=1, bg="#CCCCFF")
    Label4.place(x=230,y=110)
    Label5=tk.Label(ventana_about,text="Student/Estudiante: Karen Campos Murillo    ",font=("Times New Roman","15"),foreground="Black",width=30, height=1, bg="#CCCCFF")
    Label5.place(x=230,y=140)
    Label7=tk.Label(ventana_about,text="Student/Estudiante: Astrid Jiménez Hernández",font=("Times New Roman","15"),foreground="Black",width=50, height=1, bg="#CCCCFF")
    Label7.place(x=150,y=170)
    Label8=tk.Label(ventana_about,text="Student/Estudiante: Manuel Zapata Zamora    ",font=("Times New Roman","15"),foreground="Black",width=30, height=1, bg="#CCCCFF")
    Label8.place(x=230,y=200)
    Label9=tk.Label(ventana_about,text="Intrucciones: Para el uso de este programa se debe tener isntalado python 3.10",font=("Times New Roman","15"),foreground="Black",
                    width=60, height=1, bg="#CCCCFF")
    Label9.place(x=100,y=230)
    Label10=tk.Label(ventana_about,text="Para el manejo de datos se usan archivos txt para guardar informacion de ventas",font=("Times New Roman","15"),foreground="Black",
                    width=60, height=1, bg="#CCCCFF")
    Label10.place(x=100,y=260)
    
    #Creacion del boton return a pantalla principal del programa
    boton_regresar=Button(ventana_about,text="Regresar",font=("Helvetica",15),background="Magenta",command=cerrar_about)
    boton_regresar.place(x=350, y= 500)


    

    

    
    



    ventana_about.mainloop()
    
    
    
    
    
    


#Definicón de Labels en la ventana Principal
Label1=tk.Label(text="Welcome/Bienvenido",font=("Times New Roman","20"),foreground="Black",width=30, height=1, bg="#CCCCFF")

#Definición de Botones para la ventana Principal
boton_comprar=Button(ventana,text="Buy/Comprar",font=("Helvetica",15),background="Magenta",command=comprar_w)
boton_admin=Button(ventana,text="Administrador/Administrator",font=("Helvetica",15),background="Magenta",command=password)
boton_about=Button(ventana,text="About",font=("Helvetica",15),background="Magenta",command=Ventana_about)


#Colacación de los Label y botones en ventana principal
#Labeles
Label1.place(x=250,y=50)
#Botones
boton_comprar.place(x=400, y= 150)
boton_admin.place(x=350,y=250)
boton_about.place(x=430,y=350)



ventana.mainloop() #Loop de la ventana principal del sistema de la aplicación
