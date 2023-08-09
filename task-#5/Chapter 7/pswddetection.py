import re

def is_strong_password(password):
  
    if len(password) < 8:
        return False
  
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False
    
  
    if not re.search(r'\d', password):
        return False
    
   
    return True


passwords = [
    '12345678',
    'Hello123',
    'AbcdefgH',
    'weak',
    'Digit456'
]

for password in passwords:
    if is_strong_password(password):
        print(f"'{password}' is a strong password.")
    else:
        print(f"'{password}' is not a strong password.")
