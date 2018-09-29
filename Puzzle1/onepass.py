def please_conform_one_pass(caps):
    if len(caps) == 0:
        print('There is no persons')
    else:
        caps += [caps[0]]
        for i in range(1, len(caps)):
            if caps[i] != caps[i-1]:
                if caps[i] != caps[0]:
                    if caps[i] == caps[i+1]:
                        a = 0
                        print('People in positions', i, end='')
                    else:
                        a = 1
                        print('person at position', i, 'flip your cap!!')
                elif a == 0:
                    print(' though', i-1, 'flip your caps!!')
            elif len(caps) == 1:
                print('There is no person...')


cap1 = ['F', 'F', 'B', 'F', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']

please_conform_one_pass([])