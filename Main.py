from User import User


john = User("jhon")
mary = User("Mary")
luciano = User("Luciano")



john.hacer_deposito(1500).hacer_deposito(300).hacer_deposito(200).hacer_retiro(600).mostrar_balance_usuario()

mary.hacer_deposito(400).hacer_deposito(500).mostrar_balance_usuario()



luciano.hacer_deposito(400).hacer_retiro(50).hacer_retiro(150).hacer_retiro(199).mostrar_balance_usuario()




# #Bonus

john.transfer_dinero(luciano, 400).mostrar_balance_usuario()

luciano.mostrar_balance_usuario()




