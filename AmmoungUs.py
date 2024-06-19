from logic import *
import termcolor

ksi = Symbol('ksi')
deji = Symbol('deji')
simon =  Symbol('symon')

ammoundUsPlayers = [ksi, deji, simon]

cafiteria = Symbol('cafiteria')
navigation = Symbol('navigation')
cams = Symbol('cams')

places = [cafiteria, navigation, cams]

bomber = Symbol('bomber')
imposter = Symbol('imposter')
wereWolf = Symbol('wareWolf')

killers = [bomber, imposter, wereWolf]

symbols = ammoundUsPlayers + places + killers

def checkKnowladgeBase(knowladge):
    for symbol in symbols:
        if model_check(knowladge, symbol):
            termcolor.cprint(f'{symbol}: Killer', 'green')
        elif not model_check(knowladge, Not(symbol)):
            print(f'{symbol}: Maybe')
    
knowladge = And(
    Or(ksi, deji, simon),
    Or(cafiteria, cams, navigation),
    Or(bomber, imposter, wereWolf)
)

knowladge.add(And(
    Not(ksi), Not(cafiteria), Not(wereWolf)
)) #wereWolf isnt activated

knowladge.add(Or(
    Not(deji), Not(cams), Not(bomber)
))

knowladge.add(Not(ksi))
knowladge.add(Not(cams))
knowladge.add(Not(deji))

checkKnowladgeBase(knowladge)
