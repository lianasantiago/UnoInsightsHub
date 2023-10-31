from src.simulation_main.UnoSimulation import UnoSimulation, SimulationInputData
from tests.SimulationInputTest import SimulationInputTest
from src.controller.Machine import Machine
from src.bots.PlayerStrategy1 import PlayerStrategy1
from src.utils.CircularVector import CircularVector
from src.entity.ActionCards import ActionCard

class Simulation:
    def __init__(self,number_of_players):    
        self.PLAYERS = self.generating_players()
        self.number_of_players = number_of_players
        self.bot = Machine()
        self.CARDS_INPUT_SIMULATION = SimulationInputTest(self.number_of_players, self.bot) 
        
    def generating_players(self) -> CircularVector:
        PLAYERS = CircularVector(4)
        
        for i in range(0,4):
            player_name = "Player "+str(i)
            ia_player = PlayerStrategy1(player_name)
            PLAYERS.add(ia_player)
        return PLAYERS
    
    def generating_uno_simulation(self):      
        self.initial_players_cards = self.generating_sample_players_cards()
        simulation_data = SimulationInputData(self.bot,self.PLAYERS,self.number_of_players,self.initial_players_cards.copy())

        return UnoSimulation(simulation_data)
    
    def generating_sample_players_cards(self):
        return self.CARDS_INPUT_SIMULATION.test_one_aleatory_sample_players_hands() 
    
    def get_game_first_card(self):
        self.FIRST_CARD = self.CARDS_INPUT_SIMULATION.get_game_first_card()
        return self.FIRST_CARD
    
    def verify_action_card(self,player_hand) -> tuple:
        action_card_count = 0
        normal_card_count = 0
        
        for card in player_hand:
            if isinstance(card,ActionCard):
                action_card_count += 1
            else:
                normal_card_count += 1
        return (action_card_count,normal_card_count)
    
    def get_players_initial_cards(self):
        return self.initial_players_cards
    
    def calculating_probability_of_player_having_card_to_throw_on_hand(self, player_cards):
        count = 0
        for card in player_cards:
            if card.rank == self.FIRST_CARD.rank or card.color ==self.FIRST_CARD.color:
                count += 1
        return count
            