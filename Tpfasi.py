


from tkinter import *
from tkinter.ttk import Combobox
from Bib_File import *
import matplotlib.pyplot as plt

fieldsMMSL =('le nombre de serveur', 'la capacité du système','taux d’arrivée des clients','Taux de service')
fieldsMMS =('le nombre de serveur','taux d’arrivée des clients','Taux de service')
fieldsMM_Infinis = ( 'taux d’arrivée des clients','Taux de service')
fieldsMM1_Infinis_N = ('le nombre de serveur','le nombre de clients','taux d’arrivée des clients','Taux de service')

def  MMS():
      b3 = Button(root, text = 'Calcule des perfermance')
      b3.pack(side = LEFT, padx = 5, pady = 5)
#def  MMSL():   
#def  MM_Infini():  
#def  MM1_Infini_N():       
    
def final_balance(entries):
   # period rate:
   r = (float(entries['Annual Rate'].get()) / 100) / 12
   print("r", r)
   # principal loan:
   loan = float(entries['Loan Principle'].get())
   n = float(entries['Number of Payments'].get())
   q = (1 + r)** n
   monthly = float(entries['Monthly Payment'].get())
   q = (1 + r)** n
   remaining = q * loan - ( (q - 1) / r) * monthly
   remaining = ("%8.2f" % remaining).strip()
   entries['Remaining Loan'].delete(0,END)
   entries['Remaining Loan'].insert(0, remaining )
   print("Remaining Loan: %f" % float(remaining))
def makeformMMS(frame,frame2,frame3,frame4):
    clear(frame2)
    frame2.pack_forget()
    frame2=NONE
    clear(frame3)
    frame3.pack_forget()
    frame3=NONE
    clear(frame4)
    frame4.pack_forget()
    frame4=NONE    
    entries = {}
    i=0
    for field in fieldsMMS:
      lab = Label(frame, width=22, text=field+": ", anchor='w').grid(row =i )
      ent = Entry(frame)
      ent.grid(row=i, column = 4)
      ent.insert(0,"0")
      i=i+1 
      frame.pack( fill = X, padx = 5 , pady = 5)
      entries[field] = ent 
    b1 = Button(frame, text='Calcule des perfermances', command= lambda :CalculeMMS(entries)).grid(row =6, column = 0, sticky = W, pady = 6,padx = 7)
    #b1.pack(side = LEFT, padx = 5, pady = 5)  
    b2 = Button(frame, text='Graph pk ',command= lambda :plottMSS(entries)).grid(row = 6, column = 4, sticky = W, pady = 6)
   
   

    
         

def makeformMMSL(frame,frame2,frame3,frame4):
   clear(frame2)
   frame2.pack_forget()
   frame2=NONE
   clear(frame3)
   frame3.pack_forget()
   frame3=NONE
   clear(frame4)
   frame4.pack_forget()
   frame4=NONE    
   entries = {}
   i=0
   for field in fieldsMMSL:
      lab = Label(frame, width=22, text=field+": ", anchor='w').grid(row =i )
      ent = Entry(frame)
      ent.grid(row=i, column = 4)
      ent.insert(0,"0")
      i=i+1 
      frame.pack( fill = X, padx = 5 , pady = 5)
      entries[field] = ent
   b1 = Button(frame, text='Calcule des perfermances ',command= lambda :CalculeMMSL(entries)).grid(row =6, column = 0, sticky = W, pady = 6,padx = 7)
    #b1.pack(side = LEFT, padx = 5, pady = 5)  
   b2 = Button(frame, text='Graph pk ').grid(row = 6, column = 4, sticky = W, pady = 6)
   return frame
  
   return entries
def makeformMM_Infini(frame,frame2,frame3,frame4):
   clear(frame2)
   frame2.pack_forget()
   frame2=NONE
   clear(frame3)
   frame3.pack_forget()
   frame3=NONE
   clear(frame4)
   frame4.pack_forget()
   frame4=NONE    
   entries = {}
   i=0
   for field in fieldsMM_Infinis:
      lab = Label(frame, width=22, text=field+": ", anchor='w').grid(row =i )
      ent = Entry(frame)
      ent.grid(row=i, column = 4)
      ent.insert(0,"0")
      i=i+1 
      frame.pack( fill = X, padx = 5 , pady = 5)
      entries[field] = ent
  
   b1 = Button(frame, text='Calcule des perfermances ',command= lambda :CalculeMM_Infini(entries)).grid(row =6, column = 0, sticky = W, pady = 6,padx = 7)
    #b1.pack(side = LEFT, padx = 5, pady = 5)  
   b2 = Button(frame, text='Graph pk').grid(row = 6, column = 4, sticky = W, pady = 6)
   return frame
  
   return entries
def makeformMM1_Infini_N(frame,frame2,frame3,frame4):
   clear(frame2)
   frame2.pack_forget()
   frame2=NONE
   clear(frame3)
   frame3.pack_forget()
   frame3=NONE
   clear(frame4)
   frame4.pack_forget()
   frame4=NONE    
   entries = {}
   i=0
   for field in fieldsMM1_Infinis_N:
      lab = Label(frame, width=22, text=field+": ", anchor='w').grid(row =i )
      ent = Entry(frame)
      ent.grid(row=i, column = 4)
      ent.insert(0,"0")
      i=i+1 
      frame.pack( fill = X, padx = 5 , pady = 5)
      entries[field] = ent
   b1 = Button(frame, text='Calcule des perfermances ',command= lambda :CalculeMM1_Infinis_N(entries)).grid(row =6, column = 0, sticky = W, pady = 6,padx = 7)
    #b1.pack(side = LEFT, padx = 5, pady = 5)  
   b2 = Button(frame, text='Graph pk ').grid(row = 6, column = 4, sticky = W, pady = 6)
   return frame
  
   return entries
def clear(frame):
 for widget in frame.winfo_children():
    widget.destroy()
    
    
def CalculeMMS(tab ):
    S=tab['le nombre de serveur'].get()
    lamda=tab['taux d’arrivée des clients'].get()
    mu=tab['Taux de service'].get()
    root = Tk()
    root.title("perfermance de la file MM"+S)
    root.geometry("400x400")
    text = Text(root, wrap=WORD)
    text.place(x=3,y=3)
    text.insert(INSERT,"P° :"+str(get_P0(int(lamda),int(mu) ,int(S)) )+'\n \n')
    text.insert(INSERT,"nb_moy_client_file :"+str(nb_moy_client_f(int(lamda),int(mu) ,int(S)))+"\n \n")
    text.insert(INSERT,"nb_moy_client_system :"+str(nb_moy_client_s(int(lamda),int(mu) ,int(S)))+"\n \n")
    text.insert(INSERT,"temps_sej_file :"+str(temps_sej_f(int(lamda),int(mu) ,int(S)))+"\n \n")
    text.insert(INSERT,"temps_sej_system :"+str(temps_sej_s(int(lamda),int(mu) ,int(S)))+"\n \n")
    text.pack( fill = X, padx =20 , pady = 30)
    print(tab['le nombre de serveur'].get()) 

def CalculeMMSL(tab ):
    S=tab['le nombre de serveur'].get()
    lamda=tab['taux d’arrivée des clients'].get()
    mu=tab['Taux de service'].get()
    L=tab['la capacité du système'].get()
    root = Tk()
    root.title("perfermance de la file MM/"+S+"/"+L)
    root.geometry("400x400")
    text = Text(root, wrap=WORD)
    print(L+"/"+ S+"/"+mu)
    text.place(x=3,y=3)
    text.insert(INSERT,"P° :"+str(get_P0_SL(int(lamda),int(mu) ,int(S),int(L)) )+'\n \n')
    text.insert(INSERT,"nb_moy_client_file :"+str(nf_SL(int(lamda),int(mu),int(S),int(L)))+"\n \n")
    text.insert(INSERT,"nb_moy_client_system :"+str(ns_SL(int(lamda),int(mu) ,int(S),int(L)))+"\n \n")
    text.insert(INSERT,"temps_sej_file :"+str(tf_SL(int(lamda),int(mu) ,int(S),int(L)))+"\n \n")
    text.insert(INSERT,"temps_sej_system :"+str(ts_SL(int(lamda),int(mu) ,int(S),int(L)))+"\n \n")
    text.pack( fill = X, padx =20 , pady = 30)
    print(tab['le nombre de serveur'].get()) 
def CalculeMM_Infini(tab ):
    lamda=tab['taux d’arrivée des clients'].get()
    mu=tab['Taux de service'].get()
    root = Tk()
    root.title("perfermance de la file MM/+00")
    root.geometry("400x400")
    text = Text(root, wrap=WORD)
    text.place(x=3,y=3)
    text.insert(INSERT,"P° :"+str(get_P0_Inf(int(lamda),int(mu)) )+'\n \n')
    text.insert(INSERT,"nb_moy_client_file :"+str(nf(int(lamda),int(mu) ))+"\n \n")
    text.insert(INSERT,"nb_moy_client_system :"+str(ns(int(lamda),int(mu) ))+"\n \n")
    text.insert(INSERT,"temps_sej_file :"+str(tf(int(lamda),int(mu) ))+"\n \n")
    text.insert(INSERT,"temps_sej_system :"+str(ts(int(lamda),int(mu)))+"\n \n")
    text.pack( fill = X, padx =20 , pady = 30)
    print(tab['le nombre de serveur'].get())     
def CalculeMM1_Infinis_N(tab ):
    lamda=tab['taux d’arrivée des clients'].get()
    mu=tab['Taux de service'].get()
    n=tab['le nombre de clients'].get()
    s=tab['le nombre de serveur'].get()
    root = Tk()
    root.title("perfermance de la M/M/S/Infini/N")
    root.geometry("400x400")
    text = Text(root, wrap=WORD)
    text.place(x=3,y=3)
    text.insert(INSERT,"P° :"+str(get_P0_Inf_N(int(lamda),int(mu),int(s) ,int(n)) )+'\n \n')
    text.insert(INSERT,"nf_cilent_file :"+str(nf_Inf_N(int(lamda),int(mu),int(s) ,int(n) ))+"\n \n")
    text.insert(INSERT,"nb_moy_client_system :"+str(ns_Inf_N(int(lamda),int(mu),int(s) ,int(n) ))+"\n \n")
    text.pack( fill = X, padx =20 , pady = 30)
def plottMSS(tab):
    S=tab['le nombre de serveur'].get()
    lamda=tab['taux d’arrivée des clients'].get()
    mu=tab['Taux de service'].get()
    T=[0]
    Z=[]
    for i in range(0,int(tab['le nombre de serveur'].get())):
        T.append(get_Pk(int(lamda),int(mu),int(S),i))
        Z.append(i)
    plt.plot(Z, T)  
    #print( get_Pk(int(lamda),int(mu),int(S),i))
    plt.show()    
     
if __name__ == '__main__':
   root = Tk()
   frameMMS=Frame(root)
   frameMMSL=Frame(root)
   frameMM_Infini=Frame(root)
   frameMM1_Infini_N=Frame(root)
   root.title("TP FILLE D'ATTENTE")
   b1 = Button(root, text = 'MMS',
      command=lambda: makeformMMS(frameMMS, frameMMSL, frameMM_Infini,frameMM1_Infini_N))
   
   b1.pack(side = TOP, padx = 5, pady = 5)
   b2 = Button(root, text = 'MMSL',
       command=lambda: makeformMMSL(frameMMSL,frameMMS,frameMM_Infini,frameMM1_Infini_N))
   b2.pack(side = TOP, padx = 5, pady = 5)
   b3 = Button(root, text = 'M/M/∞',
       command=lambda: makeformMM_Infini(frameMM_Infini,frameMMSL,frameMMS,frameMM1_Infini_N))
   b3.pack(side = TOP, padx = 5, pady = 5)
   b4 = Button(root, text = 'M/M/S/∞/N',
       command=lambda: makeformMM1_Infini_N(frameMM1_Infini_N,frameMM_Infini,frameMMSL,frameMMS))
   b4.pack(side = TOP, padx = 5, pady = 5)
   
   b3 = Button(root, text = 'Quit', command = root.quit)
   b3.pack(side = TOP, padx = 5, pady = 5)
  
   root.mainloop()
