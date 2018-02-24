'''
정규식, 문자열을 다루는 모듈
'''
import re

def find_number_in_string(regex):
    '''
    문자열 안에서 정규식을 이용해 숫자를 찾는 함수
    '''
    return int(re.findall('\d+', regex)[0])
