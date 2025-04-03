diff = int(input())
customer = list(input())
customer.reverse()

m = w = 0
while customer:
    first_customer = customer[-1]
    if first_customer == "M" and abs(w - (m+1)) <= diff:
        m += 1
        customer.pop()
    elif first_customer == "W" and abs(w+1 - m) <= diff:
        w += 1
        customer.pop()
    else:
        if len(customer) < 2:
            break
        second_customer = customer[-2]
        if second_customer == "M" and abs(w - (m+1)) <= diff:
            m += 1
            customer.pop(-2)
        elif second_customer == "W" and abs(w+1 - m) <= diff:
            w += 1
            customer.pop(-2)
        else:
            break
print(w+m)
