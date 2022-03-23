





def create_dictionary(filename):
    """creates a dictionary for each word w as a key
       Input: filename is a string
    """
    
    file = open(filename, 'r')
    full_file = file.read().split()
    file.close()
    my_dict = {'$' : []}

    for i in range(len(full_file)):
        if '.' in full_file[i-1]: 
            my_dict['$'] += [full_file[i]]
        if '!' in full_file[i-1]:
            my_dict['$'] += [full_file[i]]
        if '?' in full_file[i-1]:
            my_dict['$'] += [full_file[i]]
        if full_file[i] not in my_dict:
            if not '.' in full_file[i]:
                my_dict[full_file[i]] = [full_file[i+1]]
            if not '!' in full_file[i]:
                my_dict[full_file[i]] = [full_file[i+1]]
            if not '?' in full_file[i]:
                my_dict[full_file[i]] = [full_file[i+1]]
        elif full_file[i] in my_dict:
            if not '.' in full_file[i]:
                my_dict[full_file[i]] = [full_file[i+1]]
            if not '!' in full_file[i]:
                my_dict[full_file[i]] = [full_file[i+1]]
            if not '?' in full_file[i]:
                my_dict[full_file[i]] = [full_file[i+1]]

    return my_dict


def generate_text(word_dict, num_words):
    '''returns a Markov generated text'''
    
    text = ''
    nextw = random.choice(word_dict['$'])
    num += -1
    text = nextw + text

    while num_words > 0:
        if '.' in text.split()[-1]: 
            nextw = random.choice(word_dict['$'])
        if '!' in text.split()[-1]:
            nextw = random.choice(word_dict['$'])
        if '?' in text.split()[-1]:
            nextw = random.choice(word_dict['$'])
        elif word_dict[text.split()[-1]] == []:
            nextw = random.choice(word_dict['$'])
        else:
            nextw = random.choice(word_dict[text.split()[-1]])
            
        text = text + ' ' + nextw
        num -= 1
        
    print(text)
        
