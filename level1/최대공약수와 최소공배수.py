// https://programmers.co.kr/learn/courses/30/lessons/12940

# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.

def solution(n, m):
    answer = []
    
    gr_co = 1 # 최대 공약수
    le_co = 1 # 최소 공배수
    
    while True:
        
        stack = 0 # 더 나눌수 있는지 확인
        for i in range(2,min(n,m)+1):
            if n % i == 0 and m % i == 0:
                gr_co *= i
                le_co *= i
                n //= i
                m //= i
                stack += 1
                break
        
        if stack == 0:
            break
         
    le_co = le_co * n * m
        
    answer.append(gr_co)
    answer.append(le_co)    
        
    return answer
