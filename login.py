
DB_USERS=["aziz","root"]
DB_PSWD=["1234","1111"]

def dashboard():
	print(" \n *** DashBoard  ***\n")
	
def home():
	print(" \n *** Home : ip Config ***\n")
	Hostname= input(" hostname = ")
	Host_IP = input("host ip = ")
	Host_mask=input("host submask = ")
	Gatway=input("gatway ip v4 = ")
	Confirme=input(" confirme :  y - n =")
	if Confirme=="y":
		print(" ip config",Hostname)
		open("ipconfig.conf","w").writelines(Host_IP)
		print(open("ipconfig.conf","r").readlines())
		
def change_password():
	print("\n Security : change password \n")
	HostName=input("username")
	if HostName in DB_USERS:
			last_password=input("last password : ")
			if last_password in DB_PSWD:
				new_password=input("new password : ")
				renew_password=input("repeat password")
				if new_password==renew_password :
					dashboard()
def login():
	print("\n  Login Page  \n")
	Username=input("username : ")
	Password=input("password : ")
	if (Username in DB_USERS )and Password in DB_PSWD :
		dashboard()
	else:
		print("error login")

def singup():
	titel1="create account"
	print(titel1)
	username=input("Username : ")
	password=input("password : ")
	password_repeat=input("repeat password : ")
	if password==password_repeat :
		print(" welcome",username)
		home()
	else:
		print("password Error")
		
usr=input("user")
psw=input("pss")
if usr in DB_USERS and psw in DB_PSWD[DB_USERS.index(usr)] :
	print(" it's True",DB_USERS.index(usr))
	login()
else :
	print('Error login')