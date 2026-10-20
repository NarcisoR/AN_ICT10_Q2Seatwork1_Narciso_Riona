from pyscript import document, display
my_list= ["Pauline Chu Tan", "Mika Genove", "Val Garcia",]

def show_list():
    output = document.getElementById("output")
    output.innerHTML = ""
    for item in my_list:
        display(item, target="output")
        
def append_value(e):
    firstname=document.getElementById("firstname").value.strip()
    lastname=document.getElementById("lastname").value.strip()
    message= document.getElementById("message")

    if firstname and lastname:
        my_list.append(firstname + " " + lastname)
        message.innerHTML= "Data Added Successfully"
        show_list()
    else:
        message.innerHTML="Please add a Member"
    document.getElementById("firstname").value=""
    document.getElementById("lastname").value=""

def delete_value(e):
    firstname=document.getElementById("firstname").value.strip()
    lastname=document.getElementById("lastname").value.strip()
    message= document.getElementById("message")
    
    if firstname and lastname:
        value = firstname + " " + lastname
        if value in my_list:
            my_list.remove(value)
            message.innerHTML= "Data Deleted!"
            show_list()
    else:
        message.innerHTML= "Member not found or available in the list"
    
    document.getElementById("firstname").value= ""
    document.getElementById("lastname").value= ""
show_list()