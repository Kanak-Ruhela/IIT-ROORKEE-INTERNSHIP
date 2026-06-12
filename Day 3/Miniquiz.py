def quiz_game():
    score = 0

    print('1. Which planet is known as the Red Planet?')
    print('A) Venus ' ,'B) Mars' ,'C) Jupiter', 'D) Saturn')
    ans = input('Enter your answer').upper()
    if ans == "B":
        print("Correct answer")
        score += 1
    else:
        print ('Incorrect answer')
        print('Correct answer','B')

    print('2. If a bag contains 3 red marbles, 4 blue marbles, and 5 green marbles, what is the probability of picking a blue marble?')
    print('A) 1/4 B) 1/3 C) 4/5 D) 1/2')
    ans = input('Enter your answer').upper()
    if ans == "B":
        print("Correct answer")
        score += 1
    else:
        print ('Incorrect answer')
        print('Correct answer','B')

    print('3. What is the next number in the pattern: 2, 6, 12, 20, 30, ...')
    print('A) 36 B) 40 C) 42 D) 50')
    ans = input('Enter your answer').upper()
    if ans == "B":
        print("Correct answer")
        score += 1
    else:
        print ('Incorrect answer')
        print('Correct answer','C')

    print('4. What is the area of a triangle with a base of \(6\text{ cm}\) and a height of \(8\text{ cm}\)')
    print('A) \(14\text{ cm}^2\) B) \(24\text{ cm}^2\) C) \(48\text{ cm}^2\) D) \(96\text{ cm}^2\)')
    ans = input('Enter your answer').upper() 
    if ans == "B":
        print("Correct answer")
        score += 1
    else:
        print ('Incorrect answer')
        print('Correct answer','B')

    print('5. How many bones does an adult human have?')
    print('A) 106 B) 206 C) 306 D) 406')
    ans = input('Enter your answer').upper()
    if ans == "B":
        print("Correct answer")
        score += 1
    else:
        print ('Incorrect answer')
        print('Correct answer','B')
    print('\nyour score =', score ,'/ 5')
quiz_game()

