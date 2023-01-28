
list_prb = [1,2,3,4,5,6,7,8,9]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def shift_list_right(list,number=1):
    for l in range(number):
        last_element = list[-1]
        for i in range(len(list)-2,0,-1):
            list[i+1] = list[i]
            
        list[1] = list[0]
        list[0] = last_element

def ret_ind(char):
    """returns the index of the input character, referenced by alphabet list.

    Args:
        char (char): input character
    """
    for i in range(len(alphabet)):
        if char == alphabet[i]:
            return i
    return -1
def wordIndex(word):
    """returns a list with the index of the word
    """
    list = []
    for char in word:
        list.append(ret_ind(char))
    return list

def shift_list_left(list,number=1):
    for l in range(number):
        first_element = list[0]
        for i in range(1,len(list)-1):
            list[i-1] = list[i]
            
        list[-2] = list[-1]
        list[-1] = first_element


"""función que me retorne una cadena de caracteres 
   la entrada es una lista de npumeros que representan 
   los índices"""
def getString(list):
    string = ""
    for i in list:
        string += alphabet[i]
    return string


    """recibir la palabra   
       por cada letra de la palabra, hacer el respectivo corrimiento
    """


text_in = input("Ingrese un texto para codificar: ").lower()
number = int(input("indique el número de corrimientos: "))


# ingreso "abd"
# ingreso 3


indexOfWord = wordIndex(text_in)

#indexofword sera [0,1,3]


shift_list_left(alphabet,number)

# alfabeto se converita en ['y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x']

CodifiedString = getString(indexOfWord)

# STRING DEBERIA SER "yza"

print(CodifiedString)
