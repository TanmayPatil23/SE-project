from datetime import date
import re

class Validation():
   def __init__(self, type, minLength, maxLength):
      self.type = type
      self.minLength = minLength
      self.maxLength = maxLength

class Validation_Tool():
   def __init__(self):
      self.validation = {}
      self.validation['first_name'] = Validation(type = 'string', minLength = 2, maxLength = 50)
      self.validation['middle_name'] = Validation(type = 'string', minLength = 2, maxLength = 50)
      self.validation['last_name'] = Validation(type = 'string', minLength = 2, maxLength = 50)
      self.validation['dob'] = Validation(type = 'date', minLength = 10, maxLength=10)
      self.validation['mobile'] = Validation(type = 'integer', minLength=10, maxLength =10)
      self.validation['email'] = Validation(type = 'string', minLength=5, maxLength=50)
      self.validation['age'] = Validation(type= 'integer', minLength=1, maxLength=3)
      self.validation['gender'] = Validation(type='string', minLength=4, maxLength=6)
      self.validation['city'] = Validation(type='string', minLength = 2, maxLength = 50)
      self.validation['state'] = Validation(type='string', minLength = 2, maxLength = 50)
      self.validation['pin'] = Validation(type='integer', minLength = 6, maxLength = 6)
      self.validation['aadhar'] = Validation(type='integer', minLength = 12, maxLength = 12)
      self.validation['blood_grp'] = Validation(type='string', minLength = 2, maxLength = 3)
      self.validation['dose_num'] = Validation(type='integer', minLength = 1, maxLength = 1)
      self.validation['prev_id'] = Validation(type='integer', minLength = 12, maxLength = 12)
      self.validation['prev_date'] = Validation(type='date', minLength = 10, maxLength = 10)
      self.validation['vaccine_name'] = Validation(type='string', minLength=7, maxLength=10)
      self.validation['preferred_date'] = Validation(type='date', minLength=10, maxLength=10)

      self.testcase = {}
      self.testcase['first_name'] = 'pass'
      self.testcase['middle_name'] = 'pass'
      self.testcase['last_name'] = 'pass'
      self.testcase['dob'] = 'pass'
      self.testcase['mobile'] = 'pass'
      self.testcase['email'] = 'pass'
      self.testcase['age'] = 'pass'
      self.testcase['gender'] = 'pass'
      self.testcase['city'] = 'pass'
      self.testcase['state'] = 'pass'
      self.testcase['pin'] = 'pass'
      self.testcase['aadhar'] = 'pass'
      self.testcase['blood_grp'] = 'pass'
      self.testcase['dose_num'] = 'pass'
      self.testcase['prev_id'] = 'pass'
      self.testcase['prev_date'] = 'pass'
      self.testcase['vaccine_name'] = 'pass'
      self.testcase['preferred_date'] = 'pass'

   def validate_date(self, Date):
      format = "%d-%m-%Y"
      res = 'pass'
      try:
         res = bool(datetime.strptime(Date, format))
         if res:
            split_data = record['dob'].split('/')
            dd, mm, yyyy = split_data[0], split_data[1], split_data[2]
            if (date.today() - date(int(yyyy), int(mm), int(dd))).days < 0:
               res = False
      except:
         res = False
      return res

   def calculate_age(self, Date):
      today = date.today()
      age = today.year - Date.year - ((today.month, today.day) < (Date.month, Date.day))
      print(age)
      return age
   
   def validate_email(self, email):
      regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
      if(re.fullmatch(regex, email)):
         return 'pass'
      return False
   
   def validate(self, record):
      pairs = record[1:-1].split(',')
      record = {}
      for pair in pairs:
         split_pair = pair.split(':')
         key, value = split_pair[0].strip().replace("'", ''), split_pair[1].strip().replace("'", '')
         record[key] = value
      for field in record:
         data = record[field].strip()
         type = self.validation[field].type
         minLength = self.validation[field].minLength
         maxLength = self.validation[field].maxLength
         if len(data) == 0 or len(data) < minLength or len(data) > maxLength:
            self.testcase[field] = 'fail'
            continue
         elif type == 'date':
            if field == 'prev_date' and record['dose_num'] == '1':
               self.testcase[field] = 'pass'
               continue
            self.testcase[field] = self.validate_date(date)
            continue
         elif type == 'integer':
            for digit in data:
               if ord(digit) < 48 or ord(digit) > 57:
                  self.testcase[field] = 'fail'
                  break
            continue
         if field == 'email':
            self.testcase[field] = self.validate_email(data)
            continue
         elif field == 'age':
            if self.testcase['dob'] == 'fail':
               self.testcase[field] = 'fail'
               continue
            split_data = record['dob'].split('/')
            dd, mm, yyyy = split_data[0], split_data[1], split_data[2]
            age = self.calculate_age(date(int(yyyy), int(mm), int(dd)))
            if int(data) != age:
               self.testcase[field] = 'fail'
            continue
         elif field == 'gender':
            if data.lower() not in ['male', 'female', 'other']:
               self.testcase[field] = 'fail'
            continue
         elif field == 'blood_grp':
            data = data.lower()
            if data not in ['a+', 'a-', 'b+', 'b-', 'ab+', 'ab-', 'o+', 'o-']:
               self.testcase[field] = 'fail'
            continue
         elif field == 'dose_num':
            if data not in ['1', '2']:
               self.testcase[field] = 'fail'
            continue
         elif field == 'prev_id':
            if record['dose_num'] == '1':
               self.testcase[field] = 'pass'
               continue
            if self.testcase['aadhar'] == 'fail':
               self.testcase[field] = 'fail'
               continue
            if record['aadhar'] != data:
               self.testcase[field] = 'fail'
            continue
         elif field == 'vaccine_name':
            if data.lower() not in ['covaxin', 'covishield', 'sputnik']:
               self.testcase[field] = 'fail'
            continue
      return record
         
if __name__ == '__main__':
   tool = Validation_Tool()




