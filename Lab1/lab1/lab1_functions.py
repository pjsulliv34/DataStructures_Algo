from lab1.expressions import Expressions

def process_input_file(input,output,input_type,output_type):
    Processed_data = []
    with open(input,'r') as reader:
        while True:
            line = reader.readline().strip()
            line = line.replace(' ', '')
            line = line.replace('^','$')
            if line == '':
                break
        
            try:
                # print(f'Initial len {len(line)}')
                print(line,input_type,output_type)
                expression_object = Expressions(line,input_type)
                print(f'output type: {output_type}')
                if output_type == 'Postfix':
                    output_expression = expression_object.to_post_fix()
                    Processed_data.append([line,output_expression])
                elif output_type == 'Prefix':
                    output_expression = expression_object.to_pre_fix()
                    Processed_data.append([line,output_expression])
                else:
                    output_expression = expression_object.to_infix()
                    Processed_data.append([line,output_expression])
            except:
                Processed_data.append([line,'Unknown Error'])
                     

    #print(Processed_data)
    with open(output, 'w') as writer:
        index = 1
        for line in Processed_data:
            writer.write(f"Testcase {index}\n Prefix: {line[0]}\n Postfix: {line[1]}\n")
            index +=1
