#!/usr/bin/env python3
import random


def play_game(secret):
    print("Myslím si číslo od '1' do '20'.")
    tip = None
    counter = 5

    while counter > 0 and tip != secret:
        tip = int(input("Tvoj tip: "))

        if secret > tip:
            print('Hmm... Moje číslo je väčšie ako tvoje. Skús znova!')
            counter -= 1

        elif secret < tip:
            print('Hmm... Moje číslo je menšie ako tvoje. Skús znova!')
            counter -= 1

        else:
            print('Ta ty si genius.')
            break

    else:
        print(f'Ani 5 pokusov ti nestacilo, hanbi sa! Moje cislo je: {secret}')


if __name__ == '__main__':

    play_again = "ano"

    while play_again in ('a', 'ano', 'y', 'yes'):
        play_game(random.randint(1, 20))
        play_again = input('Chceš si zahrať znova? "ano" či "nie"').lower().strip()

    print('Nezavislač už toľko!')
    print('Good bye.')
