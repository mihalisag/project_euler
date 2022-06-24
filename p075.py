import math
import time

def primitive_triples(max_perim):

    solutions = []
    n_upper_bound = math.ceil(math.sqrt(max_perim/2))
    m_lower_bound = math.floor((math.sqrt(1+2*max_perim))/2 - 1)
   
    for n in range(1, n_upper_bound):
        m_upper_bound = math.ceil(-n/2 + (math.sqrt(n**2 + 2*max_perim))/2)
        
        for m in range(n + 1, m_upper_bound):

            if math.gcd(m, n) == 1 and not (m % 2 == 1 and n % 2 == 1):

                a = m**2 - n**2
                b = 2*n*m
                c = m**2 + n**2

                # if a + b + c >= perim and n == perim:
                #     return solutions

                triple = sorted([a, b, c])
                solutions.append(triple)
    
    return solutions

multiply_list = lambda multiplier, number_list : [multiplier * i for i in number_list]

def main():

    MAX_PERIM = 1_500_000
    primative_triples_list = primitive_triples(MAX_PERIM)
    triples_dict = {sum(triple): [triple] for triple in primative_triples_list}

    for triple in primative_triples_list:
        perimeter = sum(triple)
        max_scale_factor = math.floor(MAX_PERIM / perimeter)
        
        for scale_factor in range(1, max_scale_factor + 1):
            multiplied_triple = multiply_list(scale_factor, triple)
            multiplied_perimeter = scale_factor * perimeter

            # if perimeter == 240 or multiplied_perimeter == 240:
            #     print('test')

            if multiplied_perimeter not in triples_dict:
                triples_dict[multiplied_perimeter] = []
            
            if multiplied_triple not in triples_dict[multiplied_perimeter]:
                triples_dict[multiplied_perimeter].append(multiplied_triple)

    count = 0

    for perimeter in triples_dict:
        if len(triples_dict[perimeter]) == 1:
            count += 1

    print(count)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time() - start
    print(end)

# Without n_lower_bound: 8.776s
# With n_lower_bound: 6.597s