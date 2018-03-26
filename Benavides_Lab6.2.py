# Mario Benavides
# Status - complete
# This program will read the data from the file 
# and produce a report to the screen.

def main():
        try: # try/except statement
                
                infile = open('race.txt', 'r') # open the file

                total = 0 # purse accumulator
                count = 0 # horse counter
        
                horse_name = infile.readline() # read the first field
                print("Today's Winnings at Belmont Park"
              "\n---------------------------------")    


                while horse_name != '': # read the rest of the fields
                        horse_won = float(infile.readline()) # amount won
                
                        horse_name = horse_name.rstrip('\n') # strip the \n
                

                        print('Horse:', horse_name) # display the record
                        print('Purse: $', format(horse_won, ',.2f')) # display the record
                
                        horse_name = infile.readline() # read the next field

                        count += 1
                        total += horse_won

                        average = total/count
                
                infile.close() # close the file


                print() # aesthetic liberty
                print('The total purse for the day is: $',
                      format(total,  ',.2f')) # print total purse
                print('The average purse for the day is: $',
                      format(average, ',.2f')) # print average purse

        except IOError: # try/except statement
                print('An error occurred trying to read the file', race.txt)

main() # call the main function
