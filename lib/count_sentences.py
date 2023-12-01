#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value_input=''):
        self.value_input = value_input
        
    def get_value(self):
        return self.value_input

    def set_value(self, new_input):
        if isinstance(new_input, str):
            self.value_input = new_input
        else:
            print("The value must be a string.")
        
    def is_sentence(self):
        return self.value_input.endswith('.')
    
    def is_question(self):
        return self.value_input.endswith('?')
    
    def is_exclamation(self):
        return self.value_input.endswith('!')
    
    def count_sentences(self):
        sentence_ending_pattern = r"[.?!]\s"
        # Split the string based on the regex pattern.
        sentences = re.split(sentence_ending_pattern, self.value)
        # Remove any empty strings from the list.
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)
    
    value = property(get_value, set_value)





my_str = MyString()
my_str.value = "This is a string! It has three sentences. Right?"
print(my_str.count_sentences())
print(my_str.is_exclamation())  
my_str.set_value(29)