text = "X-DSPAM-Confidence:    0.8475"
st = '0'
start_from = text.find(st)
num = text[start_from:start_from+6]
flt = float(num)
print(flt)
