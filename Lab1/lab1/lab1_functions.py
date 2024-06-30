
from lab1.expressions import Expressions

def process_input_file(input,output):
    Processed_data = []
    with open(input,'r') as reader:
        while True:
            line = reader.readline().strip()
            line = line.replace(' ', '')
            line = line.replace('^','$')
            if line == '':
                break
            #print(f"Working on {line}")
            
            try:
                # print(f'Initial len {len(line)}')
                Prefix_object = Expressions(line,'Prefix')
                post_fix = Prefix_object.to_post_fix()
                #print(f'{post_fix}, postifx')
                Processed_data.append([line,post_fix])

                
            except:
                print(f"Line not working: {line}")
                print(post_fix)
                Processed_data.append([line,'Unknown Error'])

    #print(Processed_data)
    with open(output, 'w') as writer:
        index = 1
        for line in Processed_data:
            writer.write(f"Testcase {index}\n Prefix: {line[0]}\n Postfix: {line[1]}\n")
            index +=1


# loc_ = r"C:\Users\pjsul\OneDrive\Desktop\Masters AI Courses\Data Structures\Labs\Lab1_submission\resources\Required Input.txt"
# output = r"C:\Users\pjsul\OneDrive\Desktop\Masters AI Courses\Data Structures\Labs\Lab1_submission\resources\output.txt"

# process_input_file(loc_,output)