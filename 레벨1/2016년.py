#2016년 날짜 요일
import datetime

def solution(a, b):
    s_day=datetime.datetime(2016,a,b,0,0,0)
    return s_day.strftime('%a').upper()