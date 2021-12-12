import requests
 
def main():
    ad = input("enter web address")
    response = requests.get(ad) #address
    print("Status code:",response.status_code)
    print("Header : ",response.headers)
    print("Content Type:",response.headers['content-type'])
    print("Whole page ",response.text )

if __name__ == "__main__":
    main()