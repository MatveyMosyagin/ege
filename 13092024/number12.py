for one in range(1, 100):
    for two in range(1, 100):
        for three in range(1, 100):
            a = '0' + one * '1' + two * '2' + three * '3'
            while '01' in a or '02' in a or '03' in a:
                a = a.replace('01', '2302', 1)
                a = a.replace('02', '10', 1)
                a = a.replace('03', '201', 1)
            if a.count('1') == 40 and a.count('2') == 10 and a.count('3') == 8:
                print(one)
