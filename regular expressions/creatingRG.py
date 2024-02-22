from greenery import fsm, lego
import sys
import re
A, B, C = range(3)
a , b  = '0', '1'
machine = fsm.fsm(
    alphabet={a,b},
    states={A,B,C},
    initial=A, # Записываем без {}
    finals={A},
    map = {
        A : {b: B, a: A},
        B : {b: A, a: C},
        C : {a: B, b: C},
    }, 
)  
res = lego.from_fsm(machine) # Получаем готовое регулярное выражение 

