def read_students(file_path):    
    students = {}     
    with open(file_path, 'r') as file:         
        for line in file:             
            name, unit, mark, weight = line.strip().split(', ')             
            mark = int(mark)             
            weight = int(weight)                          
            if name not in students:                 
                students[name] = []             
                students[name].append((mark, weight))     
                return students 
def calculate_weighted_grade(students):     
    results = []     
    for name, grades in students.items():         
        total_weighted_marks = 0         
        total_weight = 0         
        for mark, weight in grades:            
            total_weighted_marks += mark * (weight / 100)             
            total_weight += weight         
            if total_weight == 100:            
                results.append((name, total_weighted_marks))         
            else:             
                print(f"Error: Weights for {name} do not add up to 100.")     
                return results 
def write_results(file_path, results):     
    with open(file_path, 'w') as file:         
        for name, mark in results:             
            grade = 'Pass' if mark >= 50 else 'Fail'             
            file.write(f"{name}, {mark:.2f}, {grade}\n") 
input_file = 'students.txt' 
output_file = 'results.txt' 
students = read_students(input_file) 
results = calculate_weighted_grade(students) 
write_results(output_file, results) 
print("Results have been written to", output_file)