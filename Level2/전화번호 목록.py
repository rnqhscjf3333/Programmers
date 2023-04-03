#전화번호 목록
def solution(phone_book):
    
    phone_book.sort()
    #print(phone_book)
    
    for i in range(len(phone_book)-1):
        if(len(phone_book[i+1])>=len(phone_book[i])):
            if(phone_book[i+1][0:len(phone_book[i])]==phone_book[i]):
                return False
    
    return True