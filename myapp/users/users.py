from bson.objectid import ObjectId
from flask_login import UserMixin
from passlib.apps import custom_app_context as pwd_context

from ..app import mongo,login_manager



class LoggedUser(UserMixin):
	
	def __init__(self,userid,user_record):
		self.userid = userid
		self.user_record = user_record
		
	def get_id(self):		# needed by flask-login
		return self.userid



def register_user(username,password):
	
	# search in db for this username
	user_record = mongo.db.users.find_one({'username':username})
	
	if user_record:		# username found(?)
		return None	# should never happen!
		
	# create a hash from the supplied passwd
	pwhash = pwd_context.encrypt(password)
	# insert user record into database
	user_record = {'username':username,'pwhash':pwhash}
	result = mongo.db.users.insert_one(user_record)
	oid = result.inserted_id	# the objectid of newly created record
	
	# return logged-user object
	user_record.update({'_id':oid})
	return LoggedUser(str(oid),user_record)
	

def validate_user(username,password):
	
	# search in db for this username
	user_record = mongo.db.users.find_one({'username':username})
	
	if user_record and pwd_context.verify(password,user_record['pwhash']):	# user found and verified
		return LoggedUser(str(user_record['_id']),user_record)
	
	# else, username not found or incorrect credentials
	return None
		
	
def exists_username(username):
		
	# search in db for this username
	user_record = mongo.db.users.find_one({'username':username})
	
	return bool(user_record)
	
		

@login_manager.user_loader	
def load_user(userid):

	# userid is a hex sting encoded mongo objectid
	oid = ObjectId(userid)
	
	# search in db for this objectid
	user_record = mongo.db.users.find_one({'_id':oid})
	
	if user_record:		# if a user by this id was found
		return LoggedUser(userid,user_record)		
		
	# user not found
	return None


	

