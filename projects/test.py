 def B():
        print("1=0.5-5kg")
        print("2=5-10kg")
        print("3=10-15kg")
        print("4=>15kg")
        print("5=unsure")
        B = int(input("Weight_loss_score: "))
        weight_loss_score_lookup = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 2}
        return weight_loss_score_lookup[B]