# Covid Bingo

Spice up you work-from-home zoom meetings with word bingo! 
Use this tool to generate any amount of bingo boards for any amount of people, with any words that you want!

The output is given as plain text files, and as an interactive html page.


# Requirements

* Python 3.9


# Usage

1. Clone this repo
2. Add a new dictionary of words under the `dictionaries` folder. Each line in the file is interpreted as a separate word.
3. Add a new `ini` file under the `config` folder. Follow the example of `default-config.ini`
    * This is where you choose all of your options
4. Call the script with your config file
```shell
./generate-bingo-boards --config_file wr-core-eng-config.ini

# Or you can edit already existing default.dict and default-config.ini and use:
./generate-bingo-boards
```

* All files will be in the `output` directory, separated by person 


# Example plain-text output

```
Here are your bingo boards! Print this page out or open it in a text editor! Fill out the spaces as people say the words!


                                                   ##### BOARD 1 #####                                                   
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |       Bus        |    Tradition     |      Squire      |       Cake       |      Salmon      |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |    Gregarious    |      Clique      | Extraterrestrial |    Madagascar    |     Speaker      |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |     Mushroom     |      Trains      |      FREE!       |      Cosmos      |    Pedestrian    |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |  Global Warming  |    Cacophony     |     Cabbage      |    Vegetarian    |     Prestige     |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |       Oven       |     Infinite     |     Miracle      |     Minister     |       Pony       |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
                                                                                                                         



                                                   ##### BOARD 2 #####                                                   
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |     Cabbage      |     Commute      |    Gibberish     |     Miracle      |    Radiation     |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |       Desk       |     Mushroom     |    Gregarious    |      Squire      |   Charcuterie    |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |    Pedestrian    | Extraterrestrial |      FREE!       |       Bus        |      Acquit      |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |       Pie        |     Speaker      |      Nature      |       Zoo        |    Vegetarian    |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |       Pony       |      Canada      |      Trains      |     Lollygag     |    Communist     |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
                                                                                                                         



                                                   ##### BOARD 3 #####                                                   
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |    Hypnotize     |      Poised      |     Mushroom     | Extraterrestrial |      Squire      |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |    Radiation     |  Global Warming  |    Vegetarian    |     Infinite     |    Gregarious    |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |    Gibberish     |    Pneumonia     |      FREE!       |      Salmon      |     Dentist      |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |       Dog        |      Flower      |    Madagascar    |       Bus        |       Desk       |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            |     Speaker      |      Whiff       |    Operation     |     Minister     |   Charcuterie    |             
            |                  |                  |                  |                  |                  |             
            |                  |                  |                  |                  |                  |             
            +------------------+------------------+------------------+------------------+------------------+             
                                                                                                                         



                              Generated with love using github.com/calvincramer/covid-bingo                              

```