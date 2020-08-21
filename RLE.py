# Run Length Encoding

def RLE(s):
    count=1
    out=[]
    for i in range(1,len(s)):
      if s[i] != s[i-1]:
        out.append(s[i-1]+str(count))
        count = 1
      else:
        count+=1
      if i == len(s)-1:
        if count > 1:
          out.append(s[i-1]+str(count))
        else:
          out.append(s[i]+'1')

    return ''.join(out)
