numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(0, len(numbers)):
    if numbers[i] == 1:
        print('numbers[i] = ', numbers[i], '; (i = ', i, '), "1" - не простое и не составное')
        i += 1
    else:
        for j in range(2, numbers[-1]):
            if numbers[i] % j == 0 and numbers[i] > j:
                print(numbers[i], '- составное, так как numbers[i]/j = ', numbers[i], '/', j, '= ',numbers[i]/j)
                not_primes.append(numbers[i])
                break
            elif numbers[i] / j == 1:
                print(numbers[i], '- простое, так как numbers[i]/j = ', numbers[i], '/', j, '= ', numbers[i]/j)
                primes.append(numbers[i])
                #break
print('primes: ', primes)
print('not primes: ', not_primes)
