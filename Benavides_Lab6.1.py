# Mario Benavides
# Status - Complete
# This program will read in the horses’ names and 
# amounts as keyboard input and write them to a file.   

def main():
        try: # try/except statement
                
                outfile = open('race.txt', 'w') # create the text file
        
                another = 'y' # variable to control the loop
        
                while another == 'y' or another =='Y':
                        horse_names = input('What is the horses name? ') # horse data
                        horse_won = float(input('Amount won for the day? ')) # horse data
                        while horse_won < 0: # input validation
                                horse_won = float(input('Error: dollar amount entered'
                                                        'should be a positive number: ')) 
                
                        outfile.write(horse_names + '\n') # write to the file
                        outfile.write(str(horse_won) + '\n') # write to the file
                
                        another = input('Enter another horse? (Y for yes, N for no): ') # control loop
        
                outfile.close() # close the file


        except ValueError: # try/except statement
                print('Error: Dollar amount entered should be a valid integer.') # a number, not a word

# call the main function.       
main()
