import re

class PatternMatcher:
    
    def match(self, strings, pattern):
        if not isinstance(pattern, str):
            raise ValueError("El patrón debe ser un string")

        elif not all(isinstance(string, str) for string in strings): 
            raise TypeError ("Solo puede contener strings")
        
        #pattern = pattern.replace('*', '.*')
        matching_strings = []
        for string in strings:
            if re.search(pattern,string):
                matching_strings.append(string)
                
        return matching_strings


# Ejemplo de uso:

matcher = PatternMatcher()
strings = ["gato", "perro", "caballo", "gorila", "gaviota", "argdilla"]
strings_2 = ["carro", "casa", "cementerio", "papa", "mama", "oso"]
pattern = "g.*a"
pattern2 = "c.*o"
matching_strings = matcher.match(strings, pattern)
matching_strings_2 = matcher.match(strings_2, pattern2)

print(matching_strings)
print(matching_strings_2)