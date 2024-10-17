def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n == 1:
            ben_wins += 1
            continue
        
        primes = sieve_of_eratosthenes(n)
        primes_set = set(primes)
        current_player = "Maria"
        
        while primes_set:
            prime = min(primes_set)
            multiples = set(range(prime, n + 1, prime))
            primes_set -= multiples
            
            if not primes_set:
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            
            current_player = "Ben" if current_player == "Maria" else "Maria"
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None