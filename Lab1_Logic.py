from PyQt6.QtWidgets import *
from Lab1_Screen1 import *
from Lab1_Screen2 import *
from Lab1_Screen3 import *
import csv

cameron_votes: int = 0
allison_votes: int = 0
diego_votes: int = 0

class Screen1(QMainWindow, Ui_MainWindow11):
    def __init__(self) -> None:
        """Initializes the first screen of the voting program"""
        super().__init__()
        self.setupUi(self)
        
        self.button_vote.clicked.connect(self.open_voting_menu)
        self.button_exit.clicked.connect(self.close_current_window)

    def open_voting_menu(self) -> None:
        """Opens the second screen of the voting program and closes the first one"""
        self.window2 = Screen2()
        self.window2.show()
        self.close_current_window()

    def close_current_window(self) -> None:
        """Closes the first window and ends the program entirely"""
        self.close()

class Screen2(QMainWindow, Ui_MainWindow12):
    STARTING_VALUE = 0
    def __init__(self) -> None:
        """Initializes the second screen of the voting program"""
        super().__init__()
        self.setupUi(self)

        self.cameron = self.STARTING_VALUE
        self.allison = self.STARTING_VALUE
        self.diego = self.STARTING_VALUE

        self.button_finish_voting.clicked.connect(self.open_final_screen)
        self.button_add_cameron.clicked.connect(lambda: self.adding_vote('cameron'))
        self.button_add_allison.clicked.connect(lambda: self.adding_vote('allison'))
        self.button_add_diego.clicked.connect(lambda: self.adding_vote('diego'))
        self.button_sub_cameron.clicked.connect(lambda: self.subtracting_vote('cameron'))
        self.button_sub_allison.clicked.connect(lambda: self.subtracting_vote('allison'))
        self.button_sub_diego.clicked.connect(lambda: self.subtracting_vote('diego'))
        
    def adding_vote(self, candidate) -> None:
        """Adds a vote to whichever candidates' button was pressed"""
        setattr(self, candidate, getattr(self, candidate) + 1)

    def subtracting_vote(self, candidate) -> None:
        """Adds a vote from whichever candidates' button was pressed and ensures the number of votes cannot be negative"""
        checking_value = getattr(self, candidate)
        if checking_value > 0:
            setattr(self, candidate, checking_value - 1)

    def open_final_screen(self) -> None:
        """Calls the vote_fix() function, closes the second voting window, and opens the final window of the program"""
        self.vote_fix()
        self.window3 = Screen3()
        self.window3.show()
        self.close_current_window()

    def vote_fix(self) -> None:
        """Saves the local voting variables to their global equivalents so the final screen has access to them"""
        global cameron_votes
        cameron_votes = str(self.cameron)

        global allison_votes
        allison_votes = str(self.allison)

        global diego_votes
        diego_votes = str(self.diego)
        
    def close_current_window(self) -> None:
        """Closes the second window"""
        self.close()

class Screen3(QMainWindow, Ui_MainWindow13):
    def __init__(self) -> None:
        """Initializes the third screen of the voting program"""
        super().__init__()
        self.setupUi(self)

        self.button_save_election.clicked.connect(self.finish_program)
        self.label_cameron_result.setText(cameron_votes)
        self.label_allison_result_2.setText(allison_votes)
        self.label_diego_result_3.setText(diego_votes)


    def finish_program(self) -> None:
        """Calls the save_results() and close() function, ending the program"""
        self.save_results()
        self.close()

    def save_results(self) -> None:
        """Appends the results of the election to a csv file, header is created if the file needs to be created"""
        with open('election_results.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            if csvfile.tell() == 0:
                writer.writerow(['Candidate', 'Votes'])
                writer.writerow([])

            writer.writerow(['Cameron', cameron_votes])
            writer.writerow(['Allison', allison_votes])
            writer.writerow(['Diego', diego_votes])
            writer.writerow([])




        
       