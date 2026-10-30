import sys,subprocess,re,html
pdf=sys.argv[1]
out=subprocess.run(['pdftotext','-bbox-layout',pdf,'-'],capture_output=True,text=True).stdout
pages=out.split('<page ')[1:]
for pi,pg in enumerate(pages,1):
    lines=[]
    for lm in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>',pg,re.S):
        x0,y0,x1,y1=map(float,lm.groups()[:4]); words=re.findall(r'>([^<]*)</word>',lm.group(5))
        lines.append((x0,y0,x1,y1,' '.join(html.unescape(w) for w in words)))
    hits=set()
    for i in range(len(lines)):
        a=lines[i]
        for j in range(i+1,len(lines)):
            b=lines[j]
            ox=min(a[2],b[2])-max(a[0],b[0]); oy=min(a[3],b[3])-max(a[1],b[1])
            ha=a[3]-a[1]; hb=b[3]-b[1]
            sa,sb=a[4].strip(),b[4].strip()
            if sa in sb or sb in sa or set(sa.split())&set(sb.split()): continue
            if ox>3 and oy>0.45*min(ha,hb):
                hits.add((round(a[1]),a[4][:50],b[4][:50]))
    for h in sorted(hits): print(f's.{pi} y={h[0]}: {h[1]!r} <> {h[2]!r}')
