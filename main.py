import discord
from discord.ext import commands
import tictactoe

#Initializes important discord.py variables
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '>>', intents = intents)


#Checks if bot is up and running
@client.event
async def on_ready():
    print('Bot is ready.')


"""
Main command of the program that allows a user to challenge another user with the >>challenge command. If the user accepts, a game of tic tac toe will begin. If they do not
accept in 10 minutes, the program will end the command.
"""
@client.command()
async def challenge(ctx, *, member):
    await ctx.send(f'{member} has been challenged to a game of tic tac toe.\n Will you accept the challenge? Reply with <<yes or <<no.')

    #def check and await client.wait_for were taken from stack overflow to take in inputs, though the splitting of author to get from a specific user was all me
    #acts as a checker to ensure the proper channel and user and response is being collected when the program prompts a user for input
    def check(msg):
        author = str(msg.author).split('#')
        author = author[0]
        return author == member and msg.channel == ctx.channel and \
        msg.content.lower() in ["<<yes", "<<no"]

    #prompts the user for a yes or no on whether to accept the challenge or not
    msg = await client.wait_for('message', check=check, timeout=600)

    if msg.content.lower() == "<<yes":
        #initializes Player class in the tictactoe.py module and responds to the user with instructions on how to play
        player = tictactoe.Player()
        await ctx.send("You said yes!\n"
                       "The game now begins. Use the << command and select a number between 1-9 for a position on the board, with no spaces. Challenged goes first.")

        #more checks. P1 checks for the challenged user, while P2 checks for the challenger. Therefore the challenged user always goes first
        def check_p1(msg):
            author = str(msg.author).split('#')
            author = author[0]
            # print(author)
            return author == member and msg.channel == ctx.channel and \
                   msg.content.lower() in ["<<1", "<<2", "<<3", "<<4", "<<5", "<<6", "<<7", "<<8", "<<9"]

        def check_p2(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
                   msg.content.lower() in ["<<1", "<<2", "<<3", "<<4", "<<5", "<<6", "<<7", "<<8", "<<9"]

        #gameloop, with the turn lists returning the information from the tictactoe.py module for each turn, and the checker determining the gamestate
        while True:
            turn1_list = None
            turn2_list = None
            checker_1 = None
            checker_2 = None

            #turn1 loop, which loops until a valid response is given, then returns a gamelist from the tictactoe.py module in addition to a checker
            while True:
                turn_1 = await client.wait_for('message', check=check_p1)
                turn1_list = player.turn1(turn_1.content.lower())
                #Since recursion didn't seem to work with async statements very well the loop just ensures the square being inputted is valid
                if turn1_list == False:
                    await ctx.send("Square already taken!")
                #And if valid the information is recorded as a gameboard string, which is outputted by the bot
                else:
                    checker_1 = turn1_list[0]
                    board = turn1_list[1]
                    await ctx.send(board)
                    break

            #The checker then determines if a win or tie gamestate has occured, ending the game in both situations
            if checker_1 == False:
                await ctx.send('Player 1 wins!')
                break
            elif checker_1 == True:
                await ctx.send("Game ended in a tie!")
                break


            #The turn 2 loop functions identically
            while True:
                turn_2 = await client.wait_for('message', check=check_p2)
                turn2_list = player.turn2(turn_2.content.lower())
                if turn2_list == False:
                    await ctx.send("Square already taken!")

                else:
                    checker_2 = turn2_list[0]
                    board = turn2_list[1]
                    await ctx.send(board)
                    break


            if checker_2 == False:
                await ctx.send('Player 2 wins!')
                break
            elif checker_2 == True:
                await ctx.send("Game ended in a tie!")
                break

    else:
        await ctx.send("You said no!")


#Provides simple information to user on where to place their squares, usable mid-game
@client.command()
async def board_help(ctx):
    gameboard_border = '--------'

    gameboard_top = ' 1 ' + '|' + ' 2 ' + '|' + ' 3 ' + '\n'
    gameboard_middle = ' 4 ' + '|' + ' 5 ' + '|' + ' 6 ' + '\n'
    gameboard_bottom = ' 7 ' + '|' + ' 8 ' + '|' + ' 9 '
    gameboard_edge = '--+--+--\n'

    gameboard = gameboard_top + gameboard_edge + gameboard_middle + gameboard_edge + gameboard_bottom
    msg = gameboard + '\n' + '\nThe following numbers are assigned to each square. Enter the number to select the square.'
    await ctx.send(msg)

#runs client using token
client.run("TOKEN")
