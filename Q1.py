# ask_question naam ka Ek function likhiye jo yeh text ko "ek baar" print kare.
#  Fir iss function ko 5 baar call kar ke yeh text 5 baar print karvao.

# def ask_question():
#     print("ek baar")

# ask_question()
# ask_question()
# ask_question()
# ask_question()
# ask_question()

# Fir while loop ka use kar ke iss function ko 100 baar call karne ka code likho.
#  Dono parts ka code ek hi file mein likh ke upload karo!
def ask_question():
    print("ek baar")

i=0
while i<100:
    print(i+1),ask_question()
    i=i+1