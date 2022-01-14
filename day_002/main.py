print("Bienvenido al calculador de propinas!!")
#inputs
total = input("¿Cuál es el total a pagar? ")
tip = input("¿Qué porcentaje de propina le gustaría dar? ")
number_of_people = input("¿En cuántas personas se dividirá la cuenta? ")

#parse
total_in_float = float(total)
tip_in_int = int(tip)
number_of_people_in_int  = int(number_of_people)

#calculation
pay = total_in_float * (tip_in_int/100 + 1) / number_of_people_in_int
pay_round = "{:.2f}".format(pay)

#menssage
result = f"Cada uno debe pagar ${pay_round}"
print(result)