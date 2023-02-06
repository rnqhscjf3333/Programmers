#시저 암호
def solution(s, n):
    answer = ''
    
    for i in s:
        if(i==" "):
            answer+=" "
        else:
            if(ord(i)+n>122):
                answer+=chr(ord(i)+n-122+96)
            elif(ord(i)<91 and ord(i)+n>90):
                answer+=chr(ord(i)+n-90+64)
            else:
                answer+=chr(ord(i)+n)

    return answer