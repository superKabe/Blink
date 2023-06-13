Blink is a simple executable program reminding a the user to take care of their eye health by looking away from the screen every 20 minutes. 

## How to Build

PyInstaller can be used to build and edit this application. 

```pip install pyinstaller```

Once installed, in order to build run: 

```pyinstaller --onefile --windowed --add-data "eye_icon.ico;." Blink.py``` 

The executable can then be found in the generated /dist folder. 


## Usage

If you don't plan to edit the build and just want to install the executable, you can download it off my website *here (currently unavailable lol)*. 

## Contributing

Pull requests are welcome. For changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)