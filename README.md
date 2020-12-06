# Covid Bingo

Spice up you work-from-home zoom meetings with word bingo! 
Use this tool to generate any amount of bingo boards for any amount of people, with any words that you want!

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
