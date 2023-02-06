#개인정보 수집 유효기간
import datetime
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):
    answer = []
    term = {}
    for i in terms:
        term[i.split()[0]]=int(i.split()[1])
        
    a=0
    for i in privacies:
        a+=1
        if(datetime.datetime.strptime(today,'%Y.%m.%d')>=datetime.datetime.strptime(i.split()[0],'%Y.%m.%d')+relativedelta(months=term[i.split()[1]])):
            answer.append(a)
        
    return answer

solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
