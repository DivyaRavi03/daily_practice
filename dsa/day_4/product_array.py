def product_array(items):
    product = 0
    answer = []
    diff = 0
    for i in range(len(items)):
       diff = len(items) - i
       if diff:
           for k in range(0,diff):
               product = 1 * items[k]
               answer.append(product)
       for j in range(i+1, len(items)):
           product = product * items[j]
           answer.append(product)
    return answer
        

        

        
