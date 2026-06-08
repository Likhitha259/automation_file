import csv
path=r'C:\Users\Admin\PycharmProjects\framework_m21\utilities\data_.csv'
def get_login_cred():
    with open(path,'r') as file:
        actual_data=[]
        datas=csv.DictReader(file)  #reads the data in the form dict
        for data in datas:
            username_=data['username']
            password_=data['password']
            actual_data.append((username_,password_))
        return actual_data
