import random
import operator

def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)

    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print(f'คำถาม: {num_1} {operation} {num_2}')
    return answer

def ask_question():
    answer = float(random_problem())
    guess = float(input('กรุณากรอกคำตอบของคุณ: '))
    return guess == answer

def game():
    score = 0
    while True:
        if ask_question() == True:
            score += 1
            print('ถูกต้อง!')
        else:
            print('ไม่ถูกต้อง')
            break
    print(f'======== เกมจบแล้ว ========\nคะแนนของคุณคือ {score}\nพยายามต่อไป!')
    
game()