#!/usr/bin/env python3
"""Native Repo Lens client. No repository clones, model keys or timed polling."""
import json, queue, re, sys, threading, uuid, urllib.parse, urllib.request, urllib.error, webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import ttk

OWNER='One-Wave-Universe'
BRANCH='feature/repo-lens-deepseek-jetson-20261003'
REPOS=('Builds','One-Wave-Science','Bridge-Comand','Mythos-and-Stories')
ACTORS=('GPT','GEMINI','DEEPSEEK','CLAUDE','GROK')
DEFAULT_ID='council-independent-jetson-pieces-20261003-01'
INSTRUCTIONS=('AGENTS.md','AI_CANONICAL_START_HERE.md','AI_FOREMAN_WORK_REGISTER.md','BRIDGE_COMMAND_START_HERE.md','ENGINE_EVIDENCE_PIPELINES.md','README.md')
SETTINGS=Path.home()/'.config/repo-lens/settings.json'

def get(url):
    u=urllib.parse.urlsplit(url)
    if u.scheme!='https' or u.hostname not in ('api.github.com','raw.githubusercontent.com') or u.username or u.password:raise ValueError('Unregistered source')
    request=urllib.request.Request(url,headers={'User-Agent':'OneWave-RepoLens-Native/0.1'})
    try:
        with urllib.request.urlopen(request,timeout=30) as response:
            final=urllib.parse.urlsplit(response.url)
            if final.scheme!='https' or final.hostname!=u.hostname:raise ValueError('Unexpected source redirect')
            raw=response.read(8*1024*1024+1)
            if len(raw)>8*1024*1024:raise ValueError('Source exceeds limit; nothing truncated')
            return raw.decode('utf-8')
    except urllib.error.HTTPError as error:
        raise ValueError('No result or source at this path yet' if error.code==404 else f'GitHub HTTP {error.code}; request stopped') from None

def api(path):return json.loads(get('https://api.github.com/repos/'+OWNER+'/'+path))

def reference(repo):
    if repo not in REPOS:raise ValueError('Unknown repository')
    branch=api(repo)['default_branch'];url=repo+'/commits/'+urllib.parse.quote(branch,safe='')
    head=api(url);sha=head['sha'];tree=api(repo+'/git/trees/'+head['commit']['tree']['sha']+'?recursive=1')
    if tree.get('truncated'):raise ValueError('Full manifest unavailable; request stopped')
    if any(n['type']=='commit' for n in tree['tree']):raise ValueError('Submodule requires separate full reference')
    files=[n for n in tree['tree'] if n['type']=='blob'];paths={n['path'] for n in files}
    instructions=[{'path':p,'content':get('https://raw.githubusercontent.com/'+OWNER+'/'+repo+'/'+sha+'/'+p)} for p in INSTRUCTIONS if p in paths]
    if api(url)['sha']!=sha:raise ValueError('Repository changed; start a new reference')
    return {'repository':OWNER+'/'+repo,'branch':branch,'commit':sha,'file_count':len(files),'manifest':files,'instructions':instructions,'coverage':'Bootstrap manifest and instructions only. Backend must read all source pieces before a completed model answer.'}

def packet(repo,question,actors,cycles,metadata,refs):
    question=question.strip()
    if repo not in REPOS or not 1<=len(question)<=8000:raise ValueError('Choose a repository and a question of 1–8000 characters')
    if not actors or len(set(actors))!=len(actors) or any(a not in ACTORS for a in actors):raise ValueError('Choose valid AI slots')
    if not 1<=cycles<=6:raise ValueError('Cycles must be 1–6')
    queries=[{'url':'https://opendata.cern.ch/api/records/?q=CMS&size=1','purpose':'Read CERN source metadata and preserve provenance.'},{'url':'https://gwosc.org/api/v2/runs','purpose':'Read GWOSC observing-run metadata and preserve provenance.'}] if metadata else []
    return {'id':'native-'+str(uuid.uuid4()),'repository':OWNER+'/'+repo,'question':question,'actors':actors,'workflow':'answer_then_council','lead_actor':actors[0],'reference_mode':'indexed','internal_dialogue':True,'max_model_calls':128,'metadata_queries':queries,'lens_reference':[{k:r[k] for k in ('repository','branch','commit')} for r in refs]}

def prepare(repo,question,actors,cycles,metadata):
    # Validate before any source request, then establish fresh references.
    packet(repo,question,actors,cycles,metadata,[])
    refs=[reference(r) for r in dict.fromkeys((repo,'Builds','One-Wave-Science','Bridge-Comand'))]
    p=packet(repo,question,actors,cycles,metadata,refs)
    query=urllib.parse.urlencode({'filename':'repo-lens/requests/'+p['id']+'.json','value':json.dumps(p,indent=2),'message':'Repo Lens native: '+p['id']})
    return {'packet':p,'context':refs,'submission_url':'https://github.com/'+OWNER+'/Builds/new/'+BRANCH+'?'+query}

def result(id):
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,80}',id):raise ValueError('Invalid request ID')
    x=json.loads(get('https://raw.githubusercontent.com/'+OWNER+'/Builds/'+BRANCH+'/repo-lens/results/'+id+'.json'))
    if x.get('id')!=id or x.get('schema') not in {'repo-lens/v1','repo-lens/v2'}:raise ValueError('Receipt identity mismatch')
    return x

def latest_result():
    pointer=json.loads(get('https://raw.githubusercontent.com/'+OWNER+'/Builds/'+BRANCH+'/repo-lens/council-current.json'))
    if pointer.get('schema')!='repo-lens/council-current-v1':raise ValueError('Council pointer identity mismatch')
    return result(pointer.get('id',''))

def display(x):
    lines=[x['id'],x['status'],'']
    for actor,v in x.get('actors',{}).items():
        line=f"{actor}: {v.get('display_status',v.get('status'))} · {v.get('cycles',0)} cycles"
        if 'segments_total' in v:line+=f" · {v.get('segments_read',0)}/{v['segments_total']} pieces"
        if v.get('activity'):line+=' · '+v['activity']
        lines.extend([line,v.get('error','')])
    for t in x.get('turns',[]):
        r=t.get('reference',{})
        lines.extend(['',f"{t['actor']} · cycle {t['cycle']} · {t['status']}",t.get('answer',''),f"{r.get('repository')} @ {r.get('commit')}",f"{r.get('file_count',0)} files · {t.get('segments_read',0)} pieces read",r.get('coverage','')])
        if t.get('peer_cycles_seen'):lines.append('Actual peers read: '+', '.join(f"{p['actor']} {p['cycle']}" for p in t['peer_cycles_seen']))
        for source in t.get('metadata_sources',[]):lines.append(f"{source['provider']} · {source['bytes']} bytes · SHA-256 {source['sha256']}")
    if x.get('consensus'):lines.extend(['','Council decision: '+x['consensus']['status'],'Missing votes: '+', '.join(x['consensus'].get('missing_votes',[]))])
    lines.extend(['',x.get('stop_reason','Only real completed receipts count.')]);return '\n'.join(lines)

class App:
    def __init__(self,root):
        self.root=root;self.events=queue.Queue();self.busy=False;self.evidence={};self.submission='';self.run_url=''
        root.title('Repo Lens');root.geometry('1100x800');root.minsize(720,600)
        style=ttk.Style(root);style.theme_use('clam')
        style.configure('.',background='#142128',foreground='#e9f1ed',fieldbackground='#203039')
        style.configure('TButton',padding=8);root.configure(background='#142128')
        try:settings=json.loads(SETTINGS.read_text())
        except (OSError,ValueError):settings={}
        frame=ttk.Frame(root,padding=20);frame.pack(fill='both',expand=True)
        ttk.Label(frame,text='REPO LENS · Linux desktop',font=('sans',21,'bold')).pack(anchor='w')
        ttk.Label(frame,text='Ask one AI · it references GitHub, then hands its answer to the council').pack(anchor='w',pady=10)
        tabs=ttk.Notebook(frame);tabs.pack(fill='both',expand=True)
        form=ttk.Frame(tabs,padding=16);output=ttk.Frame(tabs,padding=16);proof=ttk.Frame(tabs,padding=16)
        tabs.add(form,text='Question');tabs.add(output,text='Results');tabs.add(proof,text='Source and metadata')
        self.repo=tk.StringVar(value=settings.get('repo','Builds'));ttk.Label(form,text='Repository · full backend scan').pack(anchor='w')
        ttk.Combobox(form,textvariable=self.repo,values=REPOS,state='readonly').pack(fill='x',pady=8)
        self.question=tk.Text(form,height=7,wrap='word',background='#203039',foreground='#ffffff',insertbackground='white');self.question.pack(fill='both',expand=True);self.question.insert('1.0',settings.get('question',''))
        ttk.Label(form,text='Ask this AI first').pack(anchor='w',pady=(12,0))
        self.lead=tk.StringVar(value=settings.get('lead','GPT'));ttk.Combobox(form,textvariable=self.lead,values=ACTORS,state='readonly').pack(fill='x',pady=8)
        self.slots={actor:tk.BooleanVar(value=True) for actor in ACTORS}
        self.cycles=tk.StringVar(value='1');self.metadata=tk.BooleanVar(value=False)
        ttk.Label(form,text='The lead answers first. Council members review when finished.\nMetadata is available when needed. Limited members park; no timers.').pack(anchor='w',pady=8)
        self.prepare_button=ttk.Button(form,text='Reference and prepare',command=self.prepare);self.prepare_button.pack(fill='x',pady=12)
        ttk.Button(form,text='Submit prepared question on GitHub',command=lambda:self.open(self.submission)).pack(fill='x')
        ttk.Label(form,text='Questions and answers are public. GitHub opens its signed-in commit screen.\nPreparing alone does not start a run. Claude has no shell or filesystem tools through this app.').pack(anchor='w',pady=10)
        self.id=tk.StringVar(value=settings.get('request',DEFAULT_ID));ttk.Entry(output,textvariable=self.id).pack(fill='x')
        self.read_button=ttk.Button(output,text='Read latest council once',command=self.read);self.read_button.pack(fill='x',pady=8)
        ttk.Button(output,text='Open execution on GitHub',command=lambda:self.open(self.run_url)).pack(fill='x',pady=4)
        self.text=self.readonly(output);self.proof=self.readonly(proof)
        self.notice=tk.StringVar(value='Ready. Every network action is explicit; no scheduled polling.');ttk.Label(frame,textvariable=self.notice,wraplength=1000).pack(fill='x',pady=(12,0))
        root.bind('<<TaskComplete>>',self.done);root.protocol('WM_DELETE_WINDOW',self.close);self.tabs=tabs
    def readonly(self,parent):
        frame=ttk.Frame(parent);frame.pack(fill='both',expand=True)
        text=tk.Text(frame,wrap='word',background='#102027',foreground='#f0f5f2',state='disabled');text.pack(side='left',fill='both',expand=True)
        bar=ttk.Scrollbar(frame,command=text.yview);bar.pack(side='right',fill='y');text.configure(yscrollcommand=bar.set);return text
    def set_text(self,widget,text):widget.configure(state='normal');widget.delete('1.0','end');widget.insert('1.0',text);widget.configure(state='disabled')
    def task(self,kind,fn):
        if self.busy:return
        self.busy=True;self.prepare_button.state(['disabled']);self.read_button.state(['disabled']);self.notice.set('Reading current GitHub reference…' if kind=='prepare' else 'Reading one receipt…')
        def work():
            try:self.events.put((kind,fn(),None))
            except Exception as e:self.events.put((kind,None,str(e)))
            try:self.root.event_generate('<<TaskComplete>>',when='tail')
            except (RuntimeError,tk.TclError):pass
        threading.Thread(target=work,daemon=True).start()
    def done(self,event):
        try:kind,x,error=self.events.get_nowait()
        except queue.Empty:return
        self.busy=False;self.prepare_button.state(['!disabled']);self.read_button.state(['!disabled'])
        if error:self.notice.set(error);return
        self.evidence=x;self.set_text(self.proof,json.dumps(x,indent=2,ensure_ascii=False))
        if kind=='prepare':self.id.set(x['packet']['id']);self.submission=x['submission_url'];self.notice.set('Reference complete for preparation. Submit on GitHub to start the full scan.')
        else:self.id.set(x['id']);self.run_url=x.get('run_url','');self.set_text(self.text,display(x));self.tabs.select(1);self.notice.set('Receipt read. No automatic polling.')
    def prepare(self):
        try:n=int(self.cycles.get())
        except ValueError:self.notice.set('Cycles must be 1–6');return
        args=(self.repo.get(),self.question.get('1.0','end'),[self.lead.get()]+[a for a in ACTORS if a!=self.lead.get()],1,False);self.task('prepare',lambda:prepare(*args))
    def read(self):self.task('read',latest_result)
    def open(self,url):
        if not url:self.notice.set('No prepared submission or execution link yet.');return
        if not url.startswith('https://github.com/One-Wave-Universe/'):self.notice.set('Unregistered link');return
        webbrowser.open(url)
    def close(self):
        settings={'repo':self.repo.get(),'lead':self.lead.get(),'question':self.question.get('1.0','end').strip(),'request':self.id.get(),'cycles':self.cycles.get(),'metadata':self.metadata.get(),'actors':{a:v.get() for a,v in self.slots.items()}}
        try:SETTINGS.parent.mkdir(parents=True,exist_ok=True);SETTINGS.write_text(json.dumps(settings));SETTINGS.chmod(0o600)
        except OSError:pass
        self.root.destroy()

if __name__=='__main__':
    root=tk.Tk();app=App(root)
    if '--smoke' in sys.argv:root.update();root.destroy();print('NATIVE_LINUX_UI_OK')
    else:root.mainloop()
