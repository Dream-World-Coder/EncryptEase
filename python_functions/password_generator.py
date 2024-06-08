'''
  generate random password of 8 to 12 char
  abc - small alpha / lowercase => $a / $l
  ABC - big alpha / uppercase => $A / $u
  123 - numeric => $n
  !@# - ascii => $#
  
  a list containing 8 to 12 such characters , and will use random.choice on that list
  every group ($a, $A, ...) will have min 2 places and max 4
  
'''

import random
import string


class Password_Maker:
  def __init__(self, length:int, sequence):
    self.length = length
    self.seq = str(sequence)
    
  def generate_password(self):
    remaining_length = self.length - len(self.seq)
    # k_value = remaining_length
    
    lowercaseStr = string.ascii_lowercase
    uppercaseStr = string.ascii_uppercase
    strNumStr = string.digits
    punctuationCharStr = '!@#$%&*?-_'
    total_Strings = lowercaseStr + uppercaseStr + strNumStr + punctuationCharStr
    
    grp_length = remaining_length // 4
    
    lowers_list = random.choices(lowercaseStr, k=grp_length)
    uppers_list = random.choices(uppercaseStr, k= grp_length)
    digits_list = random.choices(strNumStr, k= grp_length)
    punctuations_list = random.choices(punctuationCharStr, k= grp_length)
    
    pro_password_list = lowers_list + uppers_list + digits_list + punctuations_list
    
    if len(pro_password_list) < remaining_length:
      diff = remaining_length - len(pro_password_list)
      extras = random.choices(total_Strings, k=diff)
      pro_password_list += extras
    
    random.shuffle(pro_password_list)
    random.shuffle(pro_password_list)
    random.shuffle(pro_password_list)
    
    password = self.seq + ''.join(pro_password_list)
    
    return password

  
Password_Generator = Password_Maker(length= 8, sequence='')
password = Password_Generator.generate_password()
print(f'password = {password}')