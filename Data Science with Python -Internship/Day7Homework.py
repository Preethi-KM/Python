def Facttorial(num):
    fact=1;
    for i in range(1,num+1):
        fact=fact*i;
    return fact;
print(Facttorial(5))




def Fibo(num):
    a,b=0,1
    for _ in range(num):
        print(a)
        a,b=b,a+b
Fibo(6)    


emails = [
    "amit.kumar@gmail.com",
    "ravi.singh@yahoo.com",
    "suresh.patel@outlook.com",
    "vikram.rao@gmail.com",
    "manoj.sharma@mail.com",
    "rajesh.nair@gmail.com",
    "karan.mehta@yahoo.com",
    "pradeep.joshi@mail.com",
    "deepak.verma@gmail.com",
    "nikhil.desai@company.com"
]


gmail_emails = [e for e in emails if e.endswith("@gmail.com")]
print("Gmail emails:", gmail_emails)
yahoo_emails = [e for e in emails if e.endswith("@yahoo.com")]
print("Yahoo emails:", yahoo_emails)
company_emails = [e for e in emails if "company" in e]
print("Company emails:", company_emails)
r_emails = [e for e in emails if e.startswith("r")]
print("Emails starting with 'r':", r_emails)
import random
three_emails = random.sample(emails, 3)
print("Any 3 random emails:", three_emails)