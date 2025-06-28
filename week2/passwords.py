"""
Author: Okuku Ogorchukwu Lourentta
Purpose: The purpose of this program is to check the strength of a password.
Showed creativity by suggesting a stronger password when the password is weak
"""

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

#show creativity by suggesting a stronger password when the password is weak


def word_in_file(word,filename,case_sensitive=False):
    """"
        This function reads a file (specified by the filename parameter) in which each line of the file contains a single word. If the word passed in the word parameter matches a word in the file the function returns a true otherwise it returns a false. If the parameter case_sensitive is true a case sensitive match is performed. If case_sensitive is false a case insensitive match is performed. The case_sensitive parameter should default to False
    """
    case_sensitive = False
    # Open the file in read mode
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # Read each line in the file
            for line in file:
                #remove any whitespaces from the line
                file_line = line.strip()
                # Check if the word passed  matches a word in the file
                if case_sensitive:
                    if word == file_line:
                        return True
                else:
                    # Convert both the word and the line to lowercase for case-insensitive comparison
                    if word.lower() == file_line.lower():
                        return True
                    
        return False
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return False

def word_has_character(word,character_list):
    """"
        This function loops through each character in the string passed in the word parameter to see if that character is in the list of characters passed in the character_list parameter. If any of the characters in the word are present in the character list return a true, If none of the characters in the word are in the character list return false
    """
    for character in word:
        if character in character_list:
            return True
    return False

def word_complexity(word):
    """"
        This function creates a numeric complexity value based on the types of characters the word parameter contains. One point of complexity is given for each type of character in the word. The function calls the word_has_character function for each of the 4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character a point is added to complexity rating. Since there are 4 kinds of characters the complexity rating will range from 0 to 4. (0 would be returned only if word contained no characters or only contains characters that are not in any of the lists.)
    """
    # Initialize complexity to 0
    complexity = 0
    #check for lowercase
    if word_has_character(word, LOWER):
        complexity += 1
    #check for uppercase
    if word_has_character(word, UPPER):
        complexity += 1
    #check for digits
    if word_has_character(word, DIGITS):
        complexity += 1
    #check for special characters
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity



def password_strength(password,min_length,strong_length):
    """"
        This function checks length requirements, calls word_complexity to calculate the words complexity then determines the password's strength based on the user requirements. It should print the messages defined in the requirements and return the password's strength as a number from 0 to 5. The min_length parameter should have a default value of 10. The strong_length parameter should have a default value of 16
    """
    min_length = 10
    strong_length = 16
    complexity = word_complexity(password)
    length = len(password)
    
    
    # check if word is in the dictionary file
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if word_in_file(password, "wordlist.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0
    
            
    # Check if the password meets the length requirements
    if length < min_length:
        print("Password is too short and is not secure.")
        return 1
    elif length >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    #check the complexity of the password
    if complexity == 0:
        print("Password is weak.")
        return 1
    elif complexity == 1:
        print("Password is weak.")
        return 2
    elif complexity == 2:
        print("Password is moderate.")
        return 3
    elif complexity == 3:
        print("Password is strong.")
        return 4
    elif complexity == 4:
        print("Password is very strong.")
        return 5
    
    
    

def main():
    """"
        Provides the user input loop. The loop asks the user for a password to test. If that password is anything but "q" or "Q" call the password_strength function and report the results to the user. If the user enters "q" or "Q", quit the program.
    """
    while True:
        user_input = input("Please enter a password to test or enter 'q' or 'Q'" )
        if user_input.lower() == 'q' or user_input.lower() == 'Q':
            # If the user enters 'q' or 'Q', quit the program
            print("Goodbye!")
            break
        else:
            strength = password_strength(user_input, 10, 16)
            if strength == 0 or strength == 1 or strength == 2 or strength == 3:
                #showed creativity by suggesting a stronger password when the password is weak
                print("Password is not secure. try hdgajsgjfj$$#@1235") 
            print(f"{strength}")

if __name__ == "__main__":
    # Call the main function to start the program
    main()




