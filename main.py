import docx
import pathlib
import os

class Encoder_Decoder():
    def __init__(self):
        self.encodedInput = ''
        self.splitEncodingInput = []
        self.splitDecodingInput = []
        self.decodedInput = ''
        self.file_to_use = ''
        self.Truekey = 0
        self.userInput = ''
        self.keyused = 0
        self.isencoded = 'False'
        self.fileType = ''
        self.file_name = ''
        self.IsEncodedFile = ''

    def EnterKey(self):
        key = input("Enter the Key:\n")
        splitKey = []
        for number in key:
            splitKey.append(int(number))
        self.Truekey = int(sum([number2
                        for number2 in splitKey])/len(splitKey))
        if self.keyused == 0:
            self.keyused = self.Truekey
        elif self.keyused != self.Truekey:
            print("The Decoding Failed.")
            quit()
    
    def SetFile(self):
        self.userInput = input(f"Enter file to be used:\n")
        self.DetectFileType()
        if self.fileType != '.txt':
            print("This File type is not supported")
            quit()
        elif self.fileType == '.txt':
            with open(f'{self.userInput}', 'r') as file:
                self.file_to_use = file.read()
            if pathlib.Path(f'{self.IsEncodedFile}').is_file():
                with open(f'{self.IsEncodedFile}', 'r') as file:
                    self.isencoded = file.read()
            else:
                pass
        
    def DetectFileType(self):
        self.file_name, self.fileType = os.path.splitext(f'{self.userInput}')
        self.IsEncodedFile = f'{self.file_name}IsEncoded{self.fileType}'

    def encode(self):
        self.SetFile()
        self.EnterKey()
        if self.isencoded == 'False':
            for letter in self.file_to_use:
                self.splitEncodingInput.append(ord(letter))
            
            print(self.splitEncodingInput)
            
            for letter in self.splitEncodingInput:
                self.encodedInput += chr(letter + self.Truekey)
                
            with open(f'{self.userInput}', 'w') as file:
                file.write(self.encodedInput)
            with open(f'{self.IsEncodedFile}', 'w') as file:
                file.write("True")
        elif self.isencoded == 'True':
            print("This document is already encoded.")

    def decode(self):
        self.SetFile()
        self.EnterKey()
        if self.isencoded == 'True':
            for letter in self.file_to_use:
                self.splitDecodingInput.append(ord(letter))
            
            print(self.splitDecodingInput)
            
            for letter in self.splitDecodingInput:
                self.decodedInput += chr(letter - self.Truekey)
            
            with open(f'{self.userInput}', 'w') as file:
                file.write(self.decodedInput)
            self.isencoded = 'False'
            with open(f'{self.IsEncodedFile}', 'w') as file:
                file.write("False")
        elif self.isencoded == 'False':
            print("This document is not yet encoded.")
        

Encoder1 = Encoder_Decoder()

Encoder1.encode()

