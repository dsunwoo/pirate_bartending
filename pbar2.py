import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

names = ["ginger","squid","rose","noodle","calculator","wafer","seaweed"]

def askme():
    """Ask a series of questions to determine what type of drink to mix"""
    answers={}
    for qkey, question in questions.items():
        answers[qkey]=input(question + " ")[0].lower() in ["y"]
    return answers

def make(answers):
    """Pick random ingredients for each flavor category given by user to mix drink"""
    ings=[]
    for akey, ans in answers.items():
        if answers[akey]:
            ings.append(random.choice(ingredients[akey]))
        else:
            continue
    return ings

def drink_name(answers):
    """Randomly generate a name based on lists above with chosen ingredients"""
    nlist=[]
    for akey, ans in answers.items():
        if answers[akey]:
            nlist.append(akey)
        else:
            continue
    dname=random.choice(nlist) + " " + random.choice(names)
    return dname
    
def main():
    answers=askme()
    drink=make(answers)
    concoction=drink_name(answers)
    print()
    print("I call this drink the " + concoction + " and it consists of: ")
    print()
    for ing in drink:
        print("A " + ing)
    
    
if __name__ == "__main__":
    main()