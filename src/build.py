import json
R=1.2
dur=[4.0,2.5,4.0,1.833,2.667]
names=["Field","Drift","Fusion","Engine","Core"]
lingers=[0.0,0.0,0.25,0.0,0.35]
w=[round(d*R,3) for d in dur]; total=sum(w)
c=[0]; 
for x in w: c.append(c[-1]+x)
segs="\n".join(f'''    <div data-sc-segment data-sc-w="{w[i]}" data-sc-linger="{lingers[i]}" data-sc-waypoint="{names[i]}">
      <img src="assets/p{i+1}.webp" alt="" decoding="async">
      <video data-sc-src="assets/leg{i+1}.mp4" data-sc-src-mobile="assets/leg{i+1}-m.mp4" muted playsinline preload="none"></video>
    </div>''' for i in range(5))
mapitems="\n".join(f'    <li><a href="#top" data-go="{round(c[i]+(0 if i==0 else 0.25),2)}" data-leg="{i}" aria-current="{str(i==0).lower()}"><span>{names[i]}</span><i></i></a></li>' for i in range(5))
lat={0:[("2.75×","avg LTV/CAC lift",58,30),("$15M","paid spend managed in-house",70,62)],
     1:[("84%","pick between bad options",60,24),("34%","of failures: no product demand",71,64)],
     2:[("Investor goals × founder execution","one plan",57,20),("One field","two sides",70,72)],
     3:[("Go / No-Go","in 2 to 3 weeks",62,26),("5 stages","one operating system",72,66)],
     4:[("Base fee + %","of incremental revenue",60,24),("60 min","free growth audit call",70,66)]}
latent="\n".join(f'  <p data-leg="{k}" style="left:{x}%;top:{y}%">{a}<small>{b}</small></p>' for k,v in lat.items() for a,b,x,y in v)
win={"who":"0.17 0.27 0.2 0.2","split":"0.27 0.42 0.2 0.2","fusion":"0.50 0.665 0.25 0.2","think":"0.665 0.735 0.2 0.2",
     "method":"0.735 0.82 0.2 0.2","team":"0.82 0.875 0.2 0.2","cases":"0.875 0.925 0.2 0.2","engage":"0.925 0.97 0.2 0.2","finale":"0.97 1 0.5 0"}
s=open('src/page.tpl.html').read()
s=s.replace('{{SEGMENTS}}',segs).replace('{{MAPITEMS}}',mapitems).replace('{{LATENT}}',latent).replace('{{FINALE_T}}',str(round(total+0.3,2)))
for k,v in win.items(): s=s.replace('{{'+k+'}}',v)
assert '{{' not in s, s[s.index('{{'):s.index('{{')+30]
open('page.html','w').write(s)
open('index.html','w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'+s+'</body></html>')
print('total',total,'bounds',[round(x/total,3) for x in c])
