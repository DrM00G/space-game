import random
import math
import sys
sys.path.append('src')
from game import Game
from player import Player
from strategies.level1strats.beserker_strat1 import LevelOneBerserkerStrategy
from strategies.level1strats.dumb_strat1 import LevelOneDumbStrategy

for game_num in range(1,6):
    random.seed(game_num)
    first_few_die_rolls = [math.ceil(10*random.random()) for _ in range(7)]
    print('first few die rolls of game {}'.format(game_num))
    print('\t',first_few_die_rolls,'\n')


win_dict={0:0,1:0}
for n in range(20):
  print(n)
  new_game=Game(board_size=[5,5],die_mode="random",sided_die=10)
  player0_strats=LevelOneBerserkerStrategy(0)
  player1_strats=LevelOneDumbStrategy(1)

  player0=Player(0,player0_strats,(2,0),game=new_game,simple_army=True)
  player1=Player(1,player1_strats,(2,4),game=new_game,simple_army=True)
  new_game.setup([player0,player1])
  win_dict[new_game.run_until_winner()]+=1
  # print("BIG WINNER:"+str(new_game.run_until_winner()))
print(win_dict) 