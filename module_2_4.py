numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(0, len(numbers)-1):
    if numbers[i] == 1:
        print(numbers[i], 'i =', i, '-> checking next')
        i += 1
    else:
        for j in range(0, numbers[i]):
            if numbers[j] == 1:
                j += 1
            elif numbers[i] % numbers[j] == 0 and numbers[i] > numbers[j]:
                print(numbers[i], '- sostavnoe','tak kak numbers[i]/numbers[j]=',numbers[i] / numbers[j])
                not_primes.append(numbers[i])
                break
            elif numbers[i] / numbers[j] == 1 and numbers[i] == numbers[j]:
                print(numbers[i], 'prostoe', 'tak kak numbers[i]/numbers[j]=',numbers[i] / numbers[j])
                primes.append(numbers[i])
                break
            #print(numbers[i] / numbers[j])
print('primes: ', primes)
print('not primes: ', not_primes)
