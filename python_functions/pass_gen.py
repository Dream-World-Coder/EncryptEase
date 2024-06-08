import random
import string

class Password_Maker:
  def __init__(self, length:int, sequence):
    self.length = length
    self.seq = str(sequence)
    
  def generate_password(self):
    remaining_length = self.length - len(self.seq)
    
    if remaining_length < 0:
      return print('Bruh wtf ? :|')
    
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