def upload_file(f):
    with open("app2/static/upload/"+f.name,"wb+") as des:
        for x in f:
            des.write(x)