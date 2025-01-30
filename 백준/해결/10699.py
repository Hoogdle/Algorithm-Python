# frome : 특정 모듈 or 패키지
# import : 전체 모듈 or 패키지

# datetime.today(), 오늘 날짜
# strftime, 날짜 및 시간을 원하는 형식으로 formating


from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
print(today)
