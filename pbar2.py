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
    "water":["water"],
}

names = ["ginger","squid","rose","noodle","calculator","wafer","seaweed"]

def askme():
    """Ask a series of questions to determine what type of drink to mix"""
    answers={}
    fcount=0
    for qkey, question in questions.items():
        answers[qkey]=input(question + " ")[0].lower() in ["y"]
        if answers[qkey]==False:
            fcount+=1
    if fcount==len(questions):
        answers={"water":True}
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
    dlim=3
    dnum=0
    more=True
    while more:
        answers=askme()
        drink=make(answers)
        if "water" in drink:
            concoction=str(drink[0])
        else:
            concoction=drink_name(answers)
            dnum+=1
        print()
        print("I call this drink the " + concoction + " and the ingredients are: ")
        print()
        for ing in drink:
            print("A " + ing)
        print()
        # Ask for another drink
        more=input("Would you like another drink? ")[0].lower() in ["y"]
        print()
        if dnum>dlim:
            print("This is drink number " + str(dnum) + " for you. I need to cut you off.")
            more=False
    
if __name__ == "__main__":
    main()