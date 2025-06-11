python_students = []
    score_list = []
    name_result = []
    
    #Will ask the user how many students there are and input their names and scores
    for num_students in range(int(input())):
        name = input()
        score = float(input())
        #Creates a nested list in python_students
        sublist = [name, score]
        python_students.append(sublist)
    
    #Gets the score in python_students and appends them in score_list
    for scores in python_students:
        score_list.append(scores[1])
        
    #Turn score_list into a set then sorts them then turns it back into a list
    unique_scores = sorted(set(score_list))
    #Stores the second lowest score into a variable
    second_lowest_score = unique_scores[1]
    
    #Checks the scores in python_students if they are equal and appends the name in the list name_result
    for names in python_students:
        if names[1] == second_lowest_score:
            name_result.append(names[0])
    
    sorted_names_result = sorted(name_result)
    
    #Print the names with the second lowest score in alphabetical order
    for second_lowest_names in sorted_names_result:
        print(second_lowest_names)
