import smtplib,sys,datetime
import poplib
from email import parser

xadminid = "anonyo.xadm@gmail.com"
xadminpassword = "anonyo123"
admin = "anonyos.mitra@gmail.com"
port=0
def mailAdmin(msg):
	stmp = 'Subject: {}\n\n{}'.format("Port "+str(port)+" sent",msg)
	mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
	mailServer.starttls()
	mailServer.login(xadminid , xadminpassword)
	mailServer.sendmail(xadminid, admin , stmp)
	mailServer.quit()
	log("sent","anonyos.mitra@gmail.com","Port "+str(port)+" sent",msg)
	return(True)
def mail(to,sub,msg):
	stmp = 'Subject: {}\n\n{}'.format(sub,msg)
	mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
	mailServer.starttls()
	mailServer.login(xadminid , xadminpassword)
	mailServer.sendmail(xadminid, to , stmp)
	mailServer.quit()
	log("sent",to,sub,msg)
	return(True)
def log(move,email,sub,msg,ext=""):
	f= open("log.txt","a")
	time=str( datetime.datetime.now())
	stat=move+"\t"+email+"\t"+sub+"\t"+msg+"\t"+time+"\t"+ext
	f.write("{}".format(stat))
	f.write("\n")
	f.close
def checkMail():
	pop_conn = poplib.POP3_SSL('pop.gmail.com')
	pop_conn.user(xadminid)
	pop_conn.pass_(xadminpassword)
	#Get messages from server:
	messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
	# Concat message pieces:
	messages = ["\n".join(mssg[1]) for mssg in messages]
	#Parse message intom an email object:
	messages = [parser.Parser().parsestr(mssg) for mssg in messages]
	for message in messages:
	    print message['subject']
	pop_conn.quit()
checkMail()
#mail("dsmitra@gmail.com","Port 0 sent","Now!")
