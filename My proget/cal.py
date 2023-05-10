# calculation of the weight of one part

total_weight = float(input("1 удар без леяк: "))
quantity = int(input("Брой гнезда: "))
piece_weight = total_weight / quantity
print(f"Теглото на един брой детайл е {piece_weight:.5f} грама.")

# entering the number of parts that can be collected in a carton

box_detail_count = int(input("Количество в кащон бр. "))
box_weight = float(input("Тегло кашон килограми: "))
box_weight_total = (piece_weight * box_detail_count) + (box_weight * 1000)
print(f"Крайно тегло {box_weight_total:.5f} ")
weight_one_pcs = 1000 / piece_weight
print(f"Бройки в 1 кг{weight_one_pcs:.5f} бр/кг")
