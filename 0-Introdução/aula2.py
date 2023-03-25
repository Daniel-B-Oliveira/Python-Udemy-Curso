# \r\n -> CRFL 
# \n -> LF (Windows mais recente)

print(12, 34, sep='-', end='\n')
print(12, 34, sep='-', end='\r\n')
print(56, 78, sep='-', end='##')
