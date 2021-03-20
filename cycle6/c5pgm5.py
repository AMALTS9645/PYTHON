f = open("C:/Users/student.MCALAB/Desktop/20mca011/PYTHON/cycle5/details.csv", 'a')
import json
    thisdict = {
        "brand":"ford",
        "model":"mustang",
        "year":"1964"
                }
result =json.dumps(thisdict)
f.write(result)
f.close()
f = open("C:/Users/student.MCALAB/Desktop/20mca011/PYTHON/cycle5/details.csv", 'r')
print(f.read())
