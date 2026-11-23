"""Fetch validated SELAE frequency snapshots using Python standard library."""
import urllib.request,re,json,concurrent.futures,html,pathlib,datetime
ROOT=pathlib.Path(__file__).resolve().parent
G=['bonoloto','la-primitiva','euromillones']
def parse_stats(g,s):
 rows=[]
 for tr in re.findall(r'<tr\b[^>]*>([\s\S]*?)</tr>',s):
  c=re.findall(r'<td[^>]*>\s*(\d+)\s*</td>',tr)
  if len(c)==4: rows.append(list(map(int,c)))
 date=re.search(r'actualizaci.n:\s*(\d{2}/\d{2}/\d{4})',html.unescape(s)).group(1)
 total=int(re.search(r'inicio la venta de este juego,\s*(\d+)',s).group(1))
 maximum,picked=(50,5) if g=='euromillones' else (49,6)
 if sorted(r[0] for r in rows)!=list(range(1,maximum+1)):raise ValueError('Incomplete or duplicate number rows')
 if sum(r[1] for r in rows)!=total*picked:raise ValueError('Historical total mismatch')
 if any(r[1]>total for r in rows):raise ValueError('Invalid counts')
 annual=[sum(r[i] for r in rows) for i in (2,3)]
 if any(n%picked for n in annual):raise ValueError('Annual total mismatch')
 labels=list(dict.fromkeys(int(x) for x in re.findall(r'<th\b[^>]*>\s*(20\d{2})\s*</(?:a|th)>',s)))[-2:]
 if len(labels)!=2:labels=[int(date[-4:])-1,int(date[-4:])]
 return dict(rows=sorted(rows),date=date,total=total,years=[n//picked for n in annual],yearLabels=labels)
def get(g):
 with urllib.request.urlopen('https://www.loteriasyapuestas.es/es/'+g+'/estadisticas',timeout=40) as r:s=r.read().decode()
 d=parse_stats(g,s)
 print(g,d['total'],d['date'])
 return g,d
def main():
 target=ROOT/'stats.json'
 old=json.loads(target.read_text()) if target.exists() else {}
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:d=dict(pool.map(get,G))
 for g in G:
  if g in old and datetime.datetime.strptime(d[g]['date'],'%d/%m/%Y')<datetime.datetime.strptime(old[g]['date'],'%d/%m/%Y'):raise ValueError('Source date went backwards')
 d['_meta']={'source':'SELAE','fetchedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 tmp=target.with_suffix('.tmp');tmp.write_text(json.dumps(d,ensure_ascii=False),encoding='utf-8');tmp.replace(target)
if __name__=='__main__':main()
