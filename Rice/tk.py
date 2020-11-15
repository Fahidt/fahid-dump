
# full_order = [['Paella', 'Beef', 6],['Biryani', 'Chicken', 5], ['Paella', 'Beef', 6],['Biryani', 'Chicken', 5], ['Paella', 'Beef', 6]]
full_order = [['Paella', 'Beef', 6],['Biryani', 'Chicken', 5], ['Paella', 'Beef', 6],['Biryani', 'Chicken', 5], ['Paella', 'Beef', 6]]
# full_order = [[1,2],[1,2],[3,4],[1,2],[3,4],[1,2]]

output = []

def receipt_print():
    price = 0
    for i in full_order:
        price = price + i[2]

    header = print("-----------------Receipt------------------")
    output.append(str(header))
    for i in range((len(full_order))):
        if full_order == []:
            break
        holder = full_order[0]
        full_order.remove(full_order[0])
        c = 1
        for j in full_order:
            if holder == j:
                full_order.remove(j)
                c += 1
            else:
                pass
        body = print(f"{c} x {holder[0]} {holder[1]} £{holder[2]*c} ")
        output.append(str(body))
    bottom = print(f"------------------------------£{price}")
    output.append(str(bottom))
    
    return output

output = receipt_print()
# var = str(receipt_print())
# print(var)

