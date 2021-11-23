filename = input("Please enter HTML file name here: ")
#here we create dictionary which will hold our tags.
dict = {"<html>":"</html>","<br>":"0","<hr>":"0","<body>":"</body>","<pre":"</pre>","<style>":"</style>","<title>":"</title>","<head>":"</head>","<table>":"</table","<thead>":"</thead>","<tr>":"</tr","<td>":"</td","<tbody>":"</tbody>","<ul>":"</ul>","<li>":"</li>","<strong>":"</strong>"}
#here we create a list to append aour tages
list_1=[]
#here goes our list which will hold the file strings
list_2= []
#here we create a list to append tags that have properties 
list_3=[]
#here goes a list with tags which we expect to have no attributes
list=["<html>","</html>","<br>","<hr>","<style>","</style>","<body>","</body>","<title>","</title>","<head>","</head>"]
#our function to open, read and create a list of strings from a file 
def read_folder(filename):
    file = open(filename)
    search=file.read()
    searchlist = search.split() 
    list_2.extend(searchlist)
read_folder(filename) 
# to check wether we have <!doctype html>
if list_2[0] != "<!DOCTYPE":
        print("YOR HTML FILE DOES NOT HAVE <!DOCTYPE html> PLEAS INSERT IN, otherwise:")
#here we iterate through the lists of the file and append all the open tags plus can lead to error if <html> or any first open tag is missing       
for i in list_2:
    if i in dict.keys():
        list_1.append(i)
        # since both <br> and <hr> does not have closing tags we can make sure they are valid using the following
        if i.strip("<>") == 'br':
            list_1.remove(i)
        elif i.strip("<>") == 'hr':
            list_1.remove(i)
    
    else:
        #for the case our tag starts from closed tag it will give us tag missing
        if i in dict.values():
            if len(list_1)==0:
                print("YOUR HTML TAG IS INCOMPLETE")
                break
        #here we append closed tags one by one then delete both the closed tag with its open one, so we use 
        if i in dict.values():
            list_1.append(i)
            # num_1 is used to refer to the index of lastly enterd open tag of our closed tag
            #num_2 is used for deleting both open tag and closed tag that are at the end index
            index_1 = -2
            index_2 = -1
            if dict[list_1[index_1]]==i:
                list_1.pop(index_2)
                list_1.pop(index_2)
#here we remove tags that we can check using the upper methode
for i in list:
    if i in list_2:
        list_2.remove(i)
# here we iterate through the list until we find tags using the following conditionals
for i in list_2:
    if i[0]=="<" and i[1] == 'i':
        continue
    elif i[0] == "<" and (i[1] != "/" and i[1] != "!"):
        list_3.append(i)
    elif i[0] == "<" and i[1] == "/":
        list_3.append(i)
        # here we use the indexs to comper letters of the tags and see if the tag is closed so we use [0][1] to refer to the second element of the first list and [-1][2] for the 3rd element of the last list 
        index_1 = 0
        index_2 = 1
        index_3 = -1
        index_4 = 2
        if list_3[index_1][index_2]==list_3[-index_3][index_4]:
            list_3.pop(index_1)
            list_3.pop(index_1)
            
# finally the condition we need to see if the html file is valid      
if len(list_1) == 0 and len(list_3) ==0:
    print("YOUR HTML TAG IS VALID")
# if the html file is not valid   
else:
    print("YOUR HTML TAG IS INCOMPLETEe")




















                