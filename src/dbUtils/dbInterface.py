from pymongo import MongoClient

class dbInterface:
  def __init__(self, credentials):
    # Read DBCredential file
    with open(credentials) as f:
      content = f.read().splitlines()
    client = MongoClient(content[3], int(content[2]))
    database = client[content[4]]
    self.profiles = database[content[5]]
    self.maleData = database[content[6]]
    self.femaleData = database[content[7]]
    self.accounts = database[content[8]]

  def getAccounts(self):
    return self.accounts.find()
 
  def writeAccount(self, screenName, gender):
    self.account.insert({"_id":screenName, "gender": gender})

  def deleteAccount(self,screenName):
    self.account.remove({"_id":screenName})

  def writeProfile(self, user, tweets):
    data = user.__dict__
    data['_id'] = user.screenName
    data['tweets'] = map(lambda x:x.__dict__, tweets)
  
    self.profiles.insert(data)
  
  def getProfile(self, screenName):
    return self.profiles.find({"_id": screenName})
  
  def existsProfile(self, screenName):
    return self.profiles.find({"_id": screenName}).count()
  
  def getProfiles(self):
    return (self.profiles).find()

  def deleteAll(self,screenName):
    self.maleData.remove({"_id": screenName})
    self.femaleData.remove({"_id": screenName})
    self.profiles.remove({"_id": screenName})

  def writeData(self,data):
    if(data["gender"] == "M"): 
      self.maleData.insert(data)
    else:
      self.femaleData.insert(data)