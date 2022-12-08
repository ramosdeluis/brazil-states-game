from turtle import Turtle
import pandas as pd


class State(Turtle):
    def __init__(self):
        super(State, self).__init__()
        self.penup()
        self.hideturtle()
        self.data = 0
        self.goto(0, -300)

    def read_csv(self, csv_file):
        self.data = pd.DataFrame(pd.read_csv(csv_file))
        return self.data

    def write_state_name(self, state_name):
        state_name = state_name.strip().title()
        if state_name in list(self.data['state']):
            state_df = self.data.loc[self.data['state'] == f'{state_name}']
            state_index = self.data.loc[self.data['state'] == f'{state_name}'].index[0]
            self.goto(float(state_df[' x'].values), float(state_df[' y'].values))
            self.write(f'{state_name}', move=False, align='center', font=('Arial', 15, 'normal'))
            self.data.drop(labels=state_index, inplace=True)
            return True
        return False
