#1) შექმენით ფუნქცია, manual_capitalize რომელიც იქნება capitalize ფუნქციის კლონი

def manual_capitalize(text):
    for i in text:  
        if not text:  # if there is no text
            return text
        first = text[0].upper() # using upper making first index big
        second = text[1:] # and others small

    return first + second        

print(manual_capitalize("alamanteraaa"))
        
def manual_title(text):
    words = text.split()  #split words
    capitalized_words = [word[0].upper() + word[1:].lower() for word in words]  # Capitalize each word
    return " ".join(capitalized_words)  # Join the capitalized words back into a string


print(manual_title("alamantera alamantera ona smotrit slovna pantera"))
