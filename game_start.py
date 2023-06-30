import tkinter as tk
from tkinter import simpledialog
import cv2 as cv
import os
import pandas as pd
import numpy as np
from random import choices
import random
from tensorflow import keras
import tensorflow as tf
from csv import writer
import matplotlib.pyplot as plt


class game():
    label_computer_response="Witaj w grze..."
    result_machine=0
    result_human=0
    runda=0
    game_string_result=""
    machine_string_choice=""
    runda_print=0
    remis=['remis']
    m_win=['wygrana maszyny']
    h_win=["wygrana człowieka"]
    trash_talk=['przegrasz']
    df = pd.DataFrame({'1Gracz': pd.Series(dtype='int'),
                       '1Komputer': pd.Series(dtype='int'),
                       '1człowike_wygrał': pd.Series(dtype='int'),
                       '2Gracz': pd.Series(dtype='int'),
                       '2Komputer': pd.Series(dtype='int'),
                       '2człowike_wygrał': pd.Series(dtype='int'),
                       '3Gracz': pd.Series(dtype='int'),
                       '3Komputer': pd.Series(dtype='int'),
                       '3człowike_wygrał': pd.Series(dtype='int'),
                       '4Gracz': pd.Series(dtype='int'),
                       '4Komputer': pd.Series(dtype='int'),
                       '4człowike_wygrał': pd.Series(dtype='int'),
                       '5Gracz': pd.Series(dtype='int'),
                       '5Komputer': pd.Series(dtype='int'),
                       '5człowike_wygrał': pd.Series(dtype='int'),
                       '6Gracz': pd.Series(dtype='int'),
                       '6Komputer': pd.Series(dtype='int'),
                       '6człowike_wygrał': pd.Series(dtype='int'),
                       'wynik': pd.Series(dtype='int')})
    
    def play(self,choice):
            
            
            dataset = pd.read_csv('model_ludzki_input_6.csv')
           
            #AI|
           
    
            
            model = tf.keras.models.load_model('model_ludzki_input_6.h5')
    
            
    
            random_row=random.choices(range(1, 1000))
            dataset = pd.read_csv('model_ludzki_input_6.csv')
            random_row=dataset.iloc[random_row,0:18].values.tolist()
            random_row = sum(random_row, [])
        
            new_data = random_row
            raw_game2= random_row
            model_output= 1
         
            game.runda = game.runda +1
            game.runda_print=game.runda_print+1
            
            if game.runda == 6:
               game.result_human=0
               game.result_machine=0
                
            human_value = float('nan')
            game_result = float('nan')    
            human_value=choice
            
            #wybór maszyny
            raw_game3 = [raw_game2, raw_game2]
            model_output = model.predict(np.array(raw_game3),verbose=0)
            # model maszyny na wybór k,p,n 
            final_model_choice = np.argmax(model_output[0], axis=0)
            
            if final_model_choice == 0:
                machine_choice = 0
                game.machine_string_choice = "Stone"
            elif final_model_choice == 1:
                machine_choice = 1
                game.machine_string_choice = "Paper"
            elif final_model_choice == 2:
                machine_choice = 2
                game.machine_string_choice = "Scissors"
    
             
            if len(raw_game2)>0 and (human_value == 0 or human_value == 1 or human_value == 2):
                raw_game2.append(human_value)
   
                game.df.loc[len(game.df)]= raw_game2    
             
            if human_value== 3:

                game.df.iloc[6:,:].to_csv('C:/Users/szczy/Projekty/S_P_S_final/model_ludzki_input_6.csv',mode='a',index= False, header=False)
          

            if (human_value-machine_choice) % 3 ==1:
                game.game_string_result="You Won!!!"
                game.result_human=game.result_human+1
                
            elif (human_value-machine_choice) % 3 > 1:
                game.game_string_result="You lost!!!"
                game.result_machine=game.result_machine+1
            else:
                game.game_string_result="Draw"
            App.label_computer_response=choices(game.trash_talk)
                
            if human_value == 0 or human_value == 1 or human_value == 2:
                new_data = new_data + [human_value,machine_choice,game_result]
                last_choice = human_value
                if len(new_data) >= 18:
                    raw_game2=new_data[-18:]
            App.changes(self)
        
class App():
    def __init__(self, window=tk.Tk(), window_title="Stone Paper Scissors"):
        self.delay=15
        self.window = window
        self.window_title = window_title
        self.game=game()
        self.init_gui()
        self.window.attributes("-topmost", True)
        self.window.mainloop()

    def init_gui(self):
        

        
        self.window['background']='#713310'
       
        self.response = tk.Label(self.window, text="Witaj w grze ludziku...")
        self.response.config(font=("Arial", 20,"bold","italic"),bg="#713310",fg="#ffdfb3")
        self.response.pack(anchor=tk.CENTER, expand=True)
        
  
        
        self.result = tk.Label(self.window, text="...")
        self.result.config(font=("Arial", 20),bg="#713310",fg="#ffdfb3")
        self.result.pack(anchor=tk.CENTER, expand=True)
        

        
        self.stone = tk.Button(self.window, text="Rock 🗿",bg="#f7c379",fg="#713310",width=25,height=3,font=("Helvetica", 18,"bold"), command=lambda: game.play(self,0))
        self.stone.pack(anchor=tk.CENTER, expand=True)    
        
        self.paper = tk.Button(self.window, text='Paper 📄',bg="#f7c379",fg="#713310", width=25,height=3,font=("Helvetica", 18,"bold"), command=lambda:game.play(self,1))
        self.paper.pack(anchor=tk.CENTER, expand=True)

        self.scissors = tk.Button(self.window, text='Scissors ✄',bg="#f7c379",fg="#713310", width=25,height=3,font=("Helvetica", 18,"bold"), command=lambda: game.play(self,2))
        self.scissors.pack(anchor=tk.CENTER, expand=True)

        self.end = tk.Button(self.window, text="End",bg="#f7c379",fg="#713310", width=25,height=3,font=("Helvetica", 18,"bold"), command=lambda: game.play(self,3))
        self.end.pack(anchor=tk.CENTER, expand=True)


        self.Human = tk.Label(self.window, text="Human points: {} ".format(game.result_human))
        self.Human.config(font=("Arial", 20),bg="#713310",fg="#ffdfb3")
        self.Human.pack(anchor=tk.CENTER, expand=True)
        
        self.Machine = tk.Label(self.window, text="Machine points: {} ".format(game.result_machine))
        self.Machine.config(font=("Arial", 20),bg="#713310",fg="#ffdfb3")
        self.Machine.pack(anchor=tk.CENTER, expand=True)            
    def changes(self):
        self.Human.configure(text="Human points: {} ".format(game.result_human),bg="#713310",fg="#ffdfb3")        
        self.Machine.configure(text="Machine points: {} ".format(game.result_machine),bg="#713310",fg="#ffdfb3")
        self.response.configure(text=choices(game.trash_talk),bg="#713310",fg="#ffdfb3")
        self.result.configure(text="Machine:   {}... {}".format(game.machine_string_choice,game.game_string_result),bg="#713310",fg="#ffdfb3")
    def end(self):
        self.window.destroy()

    
 
   

        
    

app=App() 


                       
            
