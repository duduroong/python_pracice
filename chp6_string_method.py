text = "X-DSPAM-Confidence:    0.8475"
colon_start = text.find(":") 
num = text[colon_start+1:]  #숫자 시작점 찾기
sol = float(num.strip())   #공백 제거 후, 소수점화
print(sol)
