
from tkinter import *
import random



names = []
global questions_answers
asked=[]

questions_answers = {

  1:["Guess the shape using the given information. Has four regions of negative charge around the central atom.All regions are bonded and the bond angle is 109 degrees.","Tetrehedral", "Linear","Trigonal planar","Bent",'Tetrehedral',1],
  2:["What does P.S.B.P stand for?",'Protein Strand Blood System',"Particle Structure Bond Propertie","Propertie Structure Bond Particle","Peanut Sandwhich Banana Smoothie",'Particle Structure Bond Propertie',2],
  3:["State the type of Solid, particle and attractive forces between the perticles in Ag (silver)",'Metal, atoms particle, metallic bonding','Ionic, Ion particle, Ionic bond','Molecular, molecule particles, intermolecular bond','Covalent network, atoms,covalent bonding','Metal, atoms particle, metallic bonding',1],
  4:["Which statement best defines a polar molecule?",'Polar molecules occur when there is an electronegativity difference between the bonded atoms.','Polar molecules occur when electrons are shared equal between atoms of diatomic molecule.','Polar bears','A chemical reaction or physical change is if heat is absorbed by the system from the surroundings','Polar molecules occur when there is an electronegativity difference between the bonded atoms.',1],
  5:["Which of the list of characteristics best define the term, Exothermic",'Temperature of surrounding increases. Energy is being transferred  from system to the surrounding. Bond making releases energy.','Temperature of surrounding decreases. energy is being transferred from surrounding to the system. Bond breaking requires energy.','Temperature of surrounding increases. Energy is being transferred  from system to the surrounding. Bond making releases energy.',1],
  6:["Which of these are properties of a metal solid?",'Malleable and Ductile','Ductile and Hard','Brittle and Hard','Malleable','Malleable and Ductile',1],
  7:[],
  8:[],
  9:[],
  10:[],

}

 

def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()


class Quiz:
    def __init__(self, parent):
 
        background_color="#ffd966"

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100,)
        self.quiz_frame.grid()
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Chemistry NCEA level 2 Quiz", font=("Tw Cen MT","18","bold"),bg=background_color, fg="#000000")
        self.heading_label.grid(row=0, padx=20) 
        
        #label for username
        self.user_label=Label(self.quiz_frame, text="Please enter your name: ", font=("Tw Cen MT","16"),bg=background_color,fg="#000000")
        self.user_label.grid(row=1, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.grid(row=5,  padx=20, pady=20, sticky="e")
        
        #exit Button
        self.exit_button= Button(self.quiz_frame, text="Exit", font=("Helvetica","13","bold"), bg="#dd7e6b", command=self.quiz_frame.destroy)
        self.exit_button.grid(row=5, padx=20, pady=20, sticky="w")

        
        #image
        #logo = PhotoImage(file="road.gif")
        #self.logo = Label(self.quiz_frame, image=logo)  
        #self.logo.grid(row=4,padx=20, pady=20) 
       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) 
        print(names)
        self.quiz_frame.destroy() #Destroy name frame then open the quiz runner
        Questionwindow(root)

class Questionwindow:
  def __init__(self, parent):
    background_color="#ffd966"
    #frame setup
    self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    randomiser()

    #label widget for our heading
    self.question_label=Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen MT","18","bold"),bg=background_color)
    self.question_label.grid(row=1, padx=10, pady=30, sticky="w") 

    #holds values of radio buttons
    self.var1=IntVar()

    #first radio buttom
    self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica","12"), bg=background_color, value=1, variable=self.var1,indicator=3, pady=10)
    self.rb1.grid(row=2, sticky="w")

    #second radio buttom
    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica","12"), bg=background_color, value=2, variable=self.var1, indicator=3 ,pady=10)
    self.rb2.grid(row=3, sticky="w")

   #third radio buttom
    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica","12"), bg=background_color, value=3, variable=self.var1, indicator=3,pady=10)
    self.rb3.grid(row=4, sticky="w")

    #fourth radio buttom
    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica","12"), bg=background_color, value=4, variable=self.var1, indicator=3,pady=10)
    self.rb4.grid(row=5, sticky="w")

    #confirm answer button
    self.confirm_button = Button(self.quiz_frame, text="Confirm",bg="Green")
    self.confirm_button.grid(row=6)






     
           
randomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("Chemistry Quiz") 

    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
