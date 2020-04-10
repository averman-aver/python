subj = {}
with open('6_task_file.txt') as f:
    #lines = f.readlines()
    for line in f:  # оказалось, что можно так, без .readlines
        words = ' '.join(line.split())
        subject, lecture, practice, labs = words.split()

        a = []
        for i in range(len(lecture)):  # путем формирования списка удаляются символы "не цифры"
            try:
                a.append(int(lecture[i]))
            except ValueError as err:
                continue
        aa = ''  # если соответствующее значение пустое, принудительно записывается 0, чтобы не было конфликта с int
        for j in range(len(a)):
            aa = aa + str(a[j])
        if aa == '':
            aa = '0'
        lecture = int(aa)

        b = []
        for i in range(len(practice)):
            try:
                b.append(int(practice[i]))
            except ValueError as err:
                continue
        bb = ''
        for j in range(len(b)):
            bb = bb + str(b[j])
        if bb == '':
            bb = '0'
        practice = int(bb)

        c = []
        for i in range(len(labs)):
            try:
                c.append(int(labs[i]))
            except ValueError as err:
                continue
        cc = ''
        for j in range(len(c)):
            cc = cc + str(c[j])
        if cc == '':
            cc = '0'
        labs = int(cc)

        subj[subject] = lecture + practice + labs  # ключу "предмет" присваивается значение "сумма учебных часов"
    print(subj)



