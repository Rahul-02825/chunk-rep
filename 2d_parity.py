def app(data):
    length=len(data)
    j=1
    zeros=""
    while(1):
        if(length<=8*j):
            zeros+=(8*j-length)*"0"
            zeros+=data
            break
        else:
            j+=1
    print(zeros)
    return zeros

def make_parity(raw_data,parity):
    string=""
    for i in raw_data:
        c=i.count("1")
        if(parity.lower()=="even"):
            if(c%2==0):
                string+="0"
            else:
                string+="1"
        else:
            if(c%2==0):
                string+="1"
            else:
                string+="0"
    return string

def add_col(data):
    lis=[]
    for i in range (len(data[0])):
        li=""
        for j in range(len(data)):
            li+=data[j][i]
        lis.append(li)
    return lis
    
def row_append(data,final):
    final_l=[]
    j=0
    for i in data:
        i+=final[j]
        j+=1
        final_l.append(i)
    return final_l

def print_col_form(final_data):
    s=""
    col_form=add_col(final_data)
    for i in col_form:
        s+=i
    return s
    

def twodim(data,parity):
    col_data=add_col(data)
    data.append(make_parity(col_data,parity))
    final=make_parity(data,parity)
    final_data=row_append(data,final)
    s=""
    for i in final_data:
        s+=i
    print("The final data printed in row form is:",s)
    print("The final data printed in col form is:",print_col_form(final_data))
    err=print_col_form(final_data)
    return s,err
    #main
parity=input("Give the parity to be done:")
n=int(input("Enter the number of data to be stored:"))
data=[]
for i in range(n):
    data1=[]
    data.append(app(input("Enter the data:")))
s1,err1=twodim(data,parity)

#error
parit=input("Give the parity to be done:")
nm=int(input("Enter the number of data to be stored:"))
datas=[]
for i in range(n):
    data1s=[]
    datas.append(app(input("Enter the error data:")))
s,err=twodim(datas,parity)

if(s1==s and err==err1):
    print("No error occured")
else:
    print("A error has occured")


