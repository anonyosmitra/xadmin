import smtplib,sys,datetime
import poplib, imaplib,email
from email import header
xadminid = "anonyo.xadm@gmail.com"
xadminpassword = "anonyo123"
admin = "anonyos.mitra@gmail.com"
lastUpdate='Thu, 19 Jul 2018 22:04:54 +0530'
lastMail='Thu, 19 Jul 2018 22:04:54 +0530'
logFile="xadminlog.txt"
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
	f= open(logFile,"a")
	time=str( datetime.datetime.now())
	stat=move+"\t"+email+"\t"+sub+"\t"+msg+"\t"+time+"\t"+ext
	f.write("{}".format(stat))
	f.write("\n")
	f.close
def getNewMails():
	pop_conn = poplib.POP3_SSL('pop.gmail.com')
	pop_conn.user(xadminid)
	pop_conn.pass_(xadminpassword)
	#Get messages from server:
	print pop_conn.list()
	messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
	# Concat message pieces:
	messages = ["\n".join(mssg[1]) for mssg in messages]
	#Parse message intom an email object:
	messages = [parser.Parser().parsestr(mssg) for mssg in messages]
	for message in messages:
	    print message['subject']
	pop_conn.quit()
def getAllMails():
	a=None
	M = imaplib.IMAP4_SSL('imap.gmail.com')
 	M.login(xadminid,xadminpassword)
 	rv, mailboxes = M.list()
	if rv == 'OK':
   		a= process_mailbox(M)
   	M.close()
	M.logout()
def mailListener():
	a=getAllMails()
	my=[]
	for i in a:
		if i['sub']=="to port "+str(port) or if i['sub']=="Ping" or i['sub']=="update'
def process_mailbox(M):
	mails=[]
	M.select()
	rv, data = M.search(None, "ALL")
	if rv != 'OK':
		print "No messages found!"
		return
	for num in data[0].split():
		mail={'sender':None,'time':None,'sub':None,'data':None,'content-type':None,'content':None}
		rv, data = M.fetch(num, '(RFC822)')
		if rv != 'OK':
			print "ERROR getting message", num
			return
		msg = email.message_from_string(data[0][1])
		mail['data']=str(email.header.make_header(email.header.decode_header(str(msg.get_payload()[0]))))
		mail['sub']=(num, msg['Subject'])[1]
		mail['time']=msg['Date']
		date_tuple = email.utils.parsedate_tz(msg['Date'])
		mails+=[mail]
	return mails
getAllMails()
#mail("dsmitra@gmail.com","Port 0 sent","Now!")
