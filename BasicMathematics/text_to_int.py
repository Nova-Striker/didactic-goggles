def texttoint(st):
    units = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,
        "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
        "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19}

    tens ={"twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60,
      "seventy":70, "eighty":80, "ninety":90}

    scales = {"hundred":100, "thousand":1000, "million":1000000, "billion":1000000000, "trillion":1000000000000}
    st1=st.lower().split()
    num=0
    for i in range(-1,-(len(st1)+1),-1):
        if st1[i+1] not in scales.keys():
            if st1[i] in units.keys():
                num+=units[st1[i]]
            elif st1[i] in tens.keys():
                num+=tens[st1[i]]
            elif st1[i] in scales.keys():
                if st1[i-1] in units.keys():
                    num+=(units[st1[i-1]]*scales[st1[i]])
                elif st1[i-1] in tens.keys():
                    num+=(tens[st1[i-1]]*scales[st1[i]])
                elif (i-1)<(-(len(st1))):
                    num+=scales[st1[i]]
    return num
while True:
    st=input("Enter number in text:")
    print(texttoint(st))
