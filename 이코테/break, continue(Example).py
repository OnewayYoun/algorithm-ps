l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [100, 200, 300]

for i in l1:
    for j in l2:
        for k in l3:
            print(i, j, k)
            if i == 2 and j == 20 and k == 200:
                print('1st break')
                break
        else:
            print('1st')
            continue
        print('2nd break')
        break
    else:
        print('2nd')
        continue
    print('3rd break')
    break
