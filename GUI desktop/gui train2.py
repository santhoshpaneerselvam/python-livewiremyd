
import requests

def get_live_train_status(trainno):
    base_url="https://rappid.in/apis/train.php?train_no={}".format(trainno)
    response=requests.get(base_url) 
    data=response.json()#java script object notation
    return data



train_number="22675"
train_status=get_live_train_status(train_number)
print(train_status)
print("*****************************************************************")
print("\t\t Train Name: ",train_status["train_name"])
print("*****************************************************************")
for station_info in train_status["data"]:


    if station_info["is_current_station"]:
        print("Now Station \t\t\t\t: ",station_info["station_name"])
        print("Distance From the Starting \t: ",station_info["distance"])
        print("Timing \t\t\t\t\t\t: ",station_info["timing"])
        print("Delay \t\t\t\t\t\t: ",station_info["delay"])
        print("Platform No \t\t\t\t: ",station_info["platform"])
        print("Halt Timing \t\t\t\t: ",station_info["halt"])
        
    else:
        print("station \t\t\t\t: ",station_info["station_name"])

print("******************************************************************")
print("\t\t Message\t\t: ",train_status["message"])
print("\t\t Message updated: ",train_status["updated_time"])
print("******************************************************************")




