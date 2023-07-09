# Film Title Guessing Game: "Expert System"
# Show game outline to the user
print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    WELCOME TO THE GAME: GUESSING THE FILM TITLE!     
    2 Subgenres: Super-heroes and Romantic Dramas 
            
            SUPERHEROES:
            1. Catwoman (2004)
            2. Superman Returns (2006)
            3. Captain Marvel (2019)
            4. Aquaman (2018)
            5. Wonder woman (2017)
            6. Captain America: The First Avenger (2011)
            7. Black Panther (2018)
            8. Black Widow (2021)
            9. The Amazing Spider-man (2012)
            10. Batman (2022)
            
            ROMANTIC DRAMAS:
            1. Love, Simon (2018)
            2. A Walk to Remember (2002)
            3. Purple Hearts (2022)
            4. Me Before You (2016)
            5. Lost and Delirious (2001)
            6. Carol (2015)
            7. The Fault in Our Starts (2014)
            8. Call Me by Your Name (2017)
            9. The Notebook (2004)
            10. Imagine Me & You (2005)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

#Ask: Instruction
print("Do you need any instructions before we play?")
if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
    print("""Instructions: In this game, you have to pick from the two sub-genres and choose only ONE (1) movie in mind in the abovementioned list. 
    The system will be guessing the movie by asking you some questions: just type 'yes' or 'no' for your answer.""")

# Start: Ask: What subgenre
print("""

First, let me ask which subgenre does your movie fall into? [Type: superhero/romantic drama]: 
        """)
if input() in ['sp', 'SP', 'S', 's', 'hero', 'HERO', 'superhero', 'SUPERHERO', 'super-hero', 'SUPER-HERO', 'Superheroes', 'superheroes', 'Super-heroes', 'super-heroes', 'SUPER-HEROES']:
    # Q1: Female Superheroes
    print("Great! You chose Superhero; Is the lead superhero a female?: ")
    if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
        print("Does the name of the female superhero starts with letter 'C'?")  # Yes-Q2
        if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
            # Y-Q3
            print("Is she a batman look-alike? (i.e., wears black suit and face cover)?")
            if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                # Catwoman: Batman look-alike
                print("The film title is 'Catwoman (2004)'")
            else:
                # Captain Marvel: MARVEL comics, 'c'
                print("The film title is 'Captain Marvel (2019)'")
        else:
            print('Is the film based on the DC Comic books?: ')  # Q3
            if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                # Wonder Woman: DC comics
                print("The film title is 'Wonder Woman (2017)")
            else:
                # Black Widow: DC comics
                print("The film title is 'Black Widow (2021)'")
    else:  # Male Superheroes
        print("Is the film based on the DC Comic books?: ")  # Q2
        if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
            print("Does this superhero fly?: ")  # Y-Q3
            if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                # Superman: DC comics, 'fly'
                print("The film title is 'Superman (2006)'")
            else:
                print("So does he mostly swim then?: ")  # Y-Q4
                if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                    # Aquaman: MARVEL comics, 'sea' = 'aqua'
                    print("The film title is 'Aquaman (2018)'")
                else:
                    # Batman: DC comics, land-based superhero
                    print("The film title is 'Batman (2022)'")
        else:
            # No-Q3
            print("Does the superhero in the film mainly wears blue and red in action?: ")
            if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                # No-14
                print("Is the superhero part of the America's Armed Forces?: ")
                if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                    print(
                        "The film title is 'Captain America: The First Avenger (2011)'")  # Captain America: MARVEL comics, joined the Americas's Armed Forces which started his storyline as a superhero
                else:
                    print("""The film title is 'The Amazing Spider-man (2012)'
                    Wooh!! Andre Garfield right there!""")  # Spider-man: MARVEL comics, wears a blue and red colored suit
            else:
                # Black Panther: MARVEL comics
                print("The film title is 'Black Panther (2018)'")

else:
    # input() in ('romantic drama', 'Romantic Drama', 'ROMANTIC DRAMA', 'Romantic drama', 'romance'):
    print("Great! You chose Romantic Drama; Is it an LGBTQ+ based film?: ")
    if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
        # Q2
        print("Are two women involved? (i.e., women = biologically attributed sex): ")
        if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
            print("Are they students from a private school?: ")  # Q3
            if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                # Q4: Lost and Delirious: 2 in-love high-school students (sad story)
                print("The film title is 'Lost and Delirious (2001)'")
            else:
                print("Is there an age gap between the two?: ")  # Q4
                if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                    # Carol: 2 women inlove, age-gap
                    print("The film title is 'Carol (2015)'")
                else:
                    # IM&Y: 2 women inlove, romantic drama
                    input("The film title is 'Imagine Me & You (2005)'")
        else:
            print("Is the lead character in high-school?: ")
            if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                # Love, Simon: LGBTQ+ movie set in a 'high school' themed storyline
                print("The film title is 'Love, Simon (2018)'")
            else:
                # CMbYN: Not in high-school but played by a young adult actor
                print("The film title is 'Call Me by Your Name (2017)'")
    else:
        print("Is one of the protagonist sick or paralyzed?: ")  # Q2
        if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
            print("Does the character have cancer?: ")  # Q3
            if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                print("Both of them have cancer?: ")  # Q4
                if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                    # TFiOS: Both Agustus and Hazel Grace have cancer
                    print("The film title is 'The Fault in Our Starts (2014)'")
                else:
                    # AWtR: Only Jamie has cancer (&leukemia)
                    print("The film title is 'A Walk to Remember (2002)'")
            else:
                # MBY: William is paralyzed but does not have cancer
                print("The film title is 'me before you (2016)'")
        else:
            input() in ['no', 'NO', 'No', 'n', 'nO']
            print("Is the male protagonist in the MARINES? ")  # Q3
            if input() in ['yes', 'YES', 'y', 'Y', 'yES', 'Yes']:
                # PH: Luke is in Marines
                print("The film title is 'Purple Hearts (2022)'")
            else:
                # TN: Noah is in the Army
                print("The film title is 'The Notebook (2004)'")
