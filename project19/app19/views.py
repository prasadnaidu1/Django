from django.shortcuts import render
def showindex(request):
    return render(request,"index.html")
def validate(request):
    uname = request.POST.get("t1")
    upass = request.POST.get("t2")

    from firebase import firebase as fab
    fr = fab.FirebaseApplication("https://loginpage-9f66f.firebaseio.com/login",None)
    d1 = fr.get("login/",None)
    if d1["username"]==uname and d1["password"]==upass:
        return render(request,"weelcome.html")
    else:
        print("invalid user")
        d2={"message":"invalid user"}
        return render(request,"index.html",d2)
