import pikepdf, re, sys
src, dst = sys.argv[1], sys.argv[2]
pdf=pikepdf.open(src)
removed=[]
for pno,page in enumerate(pdf.pages,1):
    xo=page.Resources.get('/XObject',{})
    overlay=set()
    for name,obj in xo.items():
        if obj.get('/Subtype')=='/Form':
            bbox=[float(v) for v in obj.get('/BBox',[])]
            if not re.match(r'^/Fm\d+$',str(name)) and bbox==[0,0,612,792]:
                overlay.add(str(name))
    if isinstance(page.Contents,pikepdf.Array):
        content=b''.join(c.read_bytes() for c in page.Contents)
    else:
        content=page.Contents.read_bytes()
    txt=content.decode('latin-1'); n0=len(txt)
    for name in overlay:
        pat=re.compile(r'\s*q\s+1(?:\.0+)?\s+0(?:\.0+)?\s+0(?:\.0+)?\s+1(?:\.0+)?\s+0(?:\.0+)?\s+0(?:\.0+)?\s+cm\s+'+re.escape(name)+r'\s+Do\s+Q\s*')
        txt,k=pat.subn('\n',txt)
        if k!=1: print('WARN page',pno,name,'matches',k)
    for name in overlay: del xo[name]
    page.Contents=pdf.make_stream(txt.encode('latin-1'))
    removed.append((pno,sorted(overlay),n0-len(txt)))
pdf.save(dst)
for r in removed[:4]+removed[-2:]: print(r)
print('pages with overlays:',sum(1 for r in removed if r[1]), 'of', len(removed))
