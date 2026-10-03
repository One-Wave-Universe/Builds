package com.onewave.repolens;

import org.json.*;
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

final class LensClient {
    static final String OWNER="One-Wave-Universe", BRANCH="feature/repo-lens-deepseek-jetson-20261003";
    static final String[] REPOS={"Builds","One-Wave-Science","Bridge-Comand","Mythos-and-Stories"};
    static final String[] ACTORS={"GPT","GEMINI","DEEPSEEK","CLAUDE","GROK"};
    static final String DEFAULT_ID="council-independent-jetson-pieces-20261003-01";
    static final String[] INSTRUCTIONS={"AGENTS.md","AI_CANONICAL_START_HERE.md","AI_FOREMAN_WORK_REGISTER.md","BRIDGE_COMMAND_START_HERE.md","ENGINE_EVIDENCE_PIPELINES.md","README.md"};
    static String get(String url) throws Exception {
        URL u=new URL(url);
        if (!u.getProtocol().equals("https") || !(u.getHost().equals("api.github.com") || u.getHost().equals("raw.githubusercontent.com"))) throw new IOException("Unregistered source");
        HttpURLConnection c=(HttpURLConnection)u.openConnection();
        c.setInstanceFollowRedirects(false); c.setConnectTimeout(20000); c.setReadTimeout(30000);
        c.setRequestProperty("User-Agent","OneWave-RepoLens-Native/0.1");
        try {
            int status=c.getResponseCode();
            if(status==404)throw new IOException("No result or source at this path yet");
            if(status!=200)throw new IOException("GitHub HTTP "+status+"; request stopped");
            try(InputStream in=c.getInputStream(); ByteArrayOutputStream out=new ByteArrayOutputStream()) {
                byte[] b=new byte[8192]; int n;
                while((n=in.read(b))!=-1) { if(out.size()+n>8*1024*1024)throw new IOException("Source exceeds read limit; nothing truncated"); out.write(b,0,n); }
                return out.toString(StandardCharsets.UTF_8.name());
            }
        } finally { c.disconnect(); }
    }
    static JSONObject api(String path) throws Exception {return new JSONObject(get("https://api.github.com/repos/"+OWNER+"/"+path));}
    static String encode(String s) throws Exception {return URLEncoder.encode(s,StandardCharsets.UTF_8.name());}
    static JSONObject reference(String repo) throws Exception {
        if(!Arrays.asList(REPOS).contains(repo))throw new IOException("Unknown repository");
        String branch=api(repo).getString("default_branch");
        JSONObject head=api(repo+"/commits/"+encode(branch)); String sha=head.getString("sha");
        JSONObject tree=api(repo+"/git/trees/"+head.getJSONObject("commit").getJSONObject("tree").getString("sha")+"?recursive=1");
        if(tree.optBoolean("truncated"))throw new IOException("Full manifest unavailable; request stopped");
        JSONArray blobs=new JSONArray(), instructions=new JSONArray(); Set<String> paths=new HashSet<>();
        JSONArray nodes=tree.getJSONArray("tree");
        for(int i=0;i<nodes.length();i++) {JSONObject node=nodes.getJSONObject(i);
            if(node.optString("type").equals("commit"))throw new IOException("Submodule requires separate complete reference");
            if(node.optString("type").equals("blob")){blobs.put(node);paths.add(node.getString("path"));}
        }
        for(String path:INSTRUCTIONS)if(paths.contains(path))instructions.put(new JSONObject().put("path",path).put("content",get("https://raw.githubusercontent.com/"+OWNER+"/"+repo+"/"+sha+"/"+path)));
        if(!api(repo+"/commits/"+encode(branch)).getString("sha").equals(sha))throw new IOException("Repository changed; start a new reference");
        return new JSONObject().put("repository",OWNER+"/"+repo).put("branch",branch).put("commit",sha).put("file_count",blobs.length()).put("manifest",blobs).put("instructions",instructions).put("coverage","Bootstrap manifest and instructions only. Backend must read all source pieces before a completed model answer.");
    }
    static JSONObject prepare(String repo,String question,List<String> actors,int cycles,boolean metadata) throws Exception {
        question=question.trim();
        if(question.isEmpty()||question.length()>8000)throw new IOException("Question must be 1–8000 characters");
        if(actors.isEmpty()||!Arrays.asList(ACTORS).containsAll(actors)||new HashSet<>(actors).size()!=actors.size())throw new IOException("Choose valid AI slots");
        if(cycles<1||cycles>6)throw new IOException("Cycles must be 1–6");
        JSONArray refs=new JSONArray(), context=new JSONArray();
        for(String name:new LinkedHashSet<>(Arrays.asList(repo,"Bridge-Comand"))) {
            JSONObject r=reference(name);context.put(r);
            refs.put(new JSONObject().put("repository",r.getString("repository")).put("branch",r.getString("branch")).put("commit",r.getString("commit")));
        }
        String id="native-"+UUID.randomUUID();
        JSONArray queries=new JSONArray();
        if(metadata){queries.put(new JSONObject().put("url","https://opendata.cern.ch/api/records/?q=CMS&size=1").put("purpose","Read CERN source metadata and preserve provenance."));queries.put(new JSONObject().put("url","https://gwosc.org/api/v2/runs").put("purpose","Read GWOSC observing-run metadata and preserve provenance."));}
        JSONObject packet=new JSONObject().put("id",id).put("repository",OWNER+"/"+repo).put("question",question).put("actors",new JSONArray(actors)).put("cycles",cycles).put("max_model_calls",256).put("metadata_queries",queries).put("lens_reference",refs);
        String url="https://github.com/"+OWNER+"/Builds/new/"+BRANCH+"?filename="+encode("repo-lens/requests/"+id+".json")+"&value="+encode(packet.toString(2))+"&message="+encode("Repo Lens native: "+id);
        return new JSONObject().put("packet",packet).put("context",context).put("submission_url",url);
    }
    static JSONObject result(String id) throws Exception {
        if(!id.matches("[A-Za-z0-9_-]{1,80}"))throw new IOException("Invalid request ID");
        JSONObject x=new JSONObject(get("https://raw.githubusercontent.com/"+OWNER+"/Builds/"+BRANCH+"/repo-lens/results/"+id+".json"));
        if(!x.optString("id").equals(id)||!x.optString("schema").equals("repo-lens/v1"))throw new IOException("Receipt identity mismatch");
        return x;
    }
    static String display(JSONObject x) throws Exception {
        StringBuilder s=new StringBuilder(x.getString("id")+"\n"+x.getString("status")+"\n\n");
        JSONObject slots=x.optJSONObject("actors");
        if(slots!=null)for(String a:ACTORS){JSONObject v=slots.optJSONObject(a);if(v!=null){s.append(a).append(": ").append(v.optString("status")).append(" · ").append(v.optInt("cycles")).append(" cycles");if(v.has("segments_total"))s.append(" · ").append(v.optInt("segments_read")).append('/').append(v.optInt("segments_total")).append(" pieces");if(v.has("error"))s.append("\n").append(v.getString("error"));s.append("\n");}}
        JSONArray turns=x.optJSONArray("turns");
        if(turns!=null)for(int i=0;i<turns.length();i++){JSONObject t=turns.getJSONObject(i);s.append("\n").append(t.optString("actor")).append(" · cycle ").append(t.optInt("cycle")).append(" · ").append(t.optString("status")).append("\n").append(t.optString("answer")).append("\n");JSONObject r=t.optJSONObject("reference");if(r!=null)s.append(r.optString("repository")).append(" @ ").append(r.optString("commit")).append("\n").append(r.optInt("file_count")).append(" files · ").append(t.optInt("segments_read")).append(" pieces read\n").append(r.optString("coverage")).append("\n");}
        s.append("\n").append(x.optString("stop_reason","Only real completed receipts count."));return s.toString();
    }
}
