alphabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

def rotate(words, positions):
    for i in range(0,positions):
        last=words.pop()
        words.insert(0,last)
    
def encodel(l,dl):
    if l == ' ':
        return ' '
    position=alphabet.index(l)
    return alphabet[position+int(dl)]
        
if __name__ == "__main__":
    texto=input("Entre texto:")
    dl=input("Entre desplazamiento letras:")
    dp=input("Entre desplazamiento palabras:")

    ltexto = list(texto);
    enctextoList=[]
    for l in list(texto):
        enctextoList.append(encodel(l,dl))
    separator = ''
    enctexto=separator.join(enctextoList)
    words=enctexto.split(' ')
    rotate(words,int(dp))
    print("Texto cifrado: ", ' '.join(words))

