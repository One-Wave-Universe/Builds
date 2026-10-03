package com.onewave.repolens;

import android.app.*;
import android.os.*;
import android.content.*;
import android.net.Uri;
import android.graphics.Color;
import android.view.*;
import android.widget.*;
import org.json.*;
import java.util.*;
import java.util.concurrent.*;

public class MainActivity extends Activity {
    private final ExecutorService network=Executors.newSingleThreadExecutor();
    private LinearLayout page; private Spinner repository,lead; private EditText question,requestId,cycles;
    private TextView notice,result; private CheckBox metadata; private final Map<String,CheckBox> slots=new LinkedHashMap<>();
    private JSONObject evidence; private String submission="",runUrl=""; private Button prepare,read;
    private SharedPreferences prefs;
    private int dp(int v){return (int)(v*getResources().getDisplayMetrics().density);}
    private void label(String text){TextView v=new TextView(this);v.setText(text);v.setTextColor(Color.rgb(168,233,180));v.setTextSize(17);v.setPadding(0,dp(18),0,dp(6));page.addView(v);}
    private EditText edit(String hint){EditText v=new EditText(this);v.setHint(hint);v.setTextColor(Color.WHITE);v.setHintTextColor(Color.LTGRAY);page.addView(v);return v;}
    private Button button(String text,Runnable task){Button b=new Button(this);b.setText(text);b.setOnClickListener(v->task.run());page.addView(b);return b;}
    private void open(String url){try{if(!url.startsWith("https://github.com/One-Wave-Universe/"))throw new IllegalArgumentException("Unregistered link");startActivity(new Intent(Intent.ACTION_VIEW,Uri.parse(url)));}catch(Exception e){notice.setText("Could not open GitHub: "+e.getMessage());}}
    @Override public void onCreate(Bundle state){super.onCreate(state);prefs=getSharedPreferences("lens",MODE_PRIVATE);
        ScrollView scroll=new ScrollView(this);page=new LinearLayout(this);page.setOrientation(LinearLayout.VERTICAL);page.setPadding(dp(20),dp(30),dp(20),dp(32));page.setBackgroundColor(Color.rgb(16,27,34));scroll.addView(page);setContentView(scroll);
        label("REPO LENS · native Android");TextView intro=new TextView(this);intro.setText("Ask one AI. It references GitHub and uses metadata when needed, then hands its answer to the council. Each member finishes its own review. Limited members park. No timers.");intro.setTextColor(Color.LTGRAY);page.addView(intro);
        label("Repository");repository=new Spinner(this);repository.setAdapter(new ArrayAdapter<>(this,android.R.layout.simple_spinner_dropdown_item,LensClient.REPOS));repository.setSelection(prefs.getInt("repo",0));page.addView(repository);
        label("Question");question=edit("What should the AIs verify?");question.setMinLines(3);question.setGravity(Gravity.TOP);question.setText(prefs.getString("question",""));
        label("Ask this AI first");lead=new Spinner(this);lead.setAdapter(new ArrayAdapter<>(this,android.R.layout.simple_spinner_dropdown_item,LensClient.ACTORS));page.addView(lead);
        for(String actor:LensClient.ACTORS){CheckBox box=new CheckBox(this);box.setChecked(true);slots.put(actor,box);}
        cycles=new EditText(this);cycles.setText("1");metadata=new CheckBox(this);metadata.setChecked(false);
        notice=new TextView(this);notice.setTextColor(Color.LTGRAY);notice.setPadding(0,dp(10),0,dp(10));page.addView(notice);
        prepare=button("Reference and prepare",()->prepare());button("Submit prepared question on GitHub",()->{if(submission.isEmpty())notice.setText("Prepare a question first.");else open(submission);});
        TextView privacy=new TextView(this);privacy.setText("Questions and answers are public in Builds. GitHub opens its signed-in commit screen; preparing alone does not start a run.");privacy.setTextColor(Color.LTGRAY);page.addView(privacy);
        label("Verified results");requestId=edit("Request ID");requestId.setSingleLine(true);requestId.setText(prefs.getString("request",LensClient.DEFAULT_ID));
        read=button("Read latest council once",()->read());button("Inspect source and metadata receipt",()->{if(evidence==null){notice.setText("Read or prepare a request first.");return;}try{new AlertDialog.Builder(this).setTitle("Source / metadata evidence").setMessage(evidence.toString(2)).setPositiveButton("Close",null).show();}catch(Exception e){notice.setText(e.getMessage());}});button("Open execution on GitHub",()->{if(runUrl.isEmpty())notice.setText("No execution link in the last result.");else open(runUrl);});
        result=new TextView(this);result.setTextColor(Color.WHITE);result.setTextSize(15);result.setTextIsSelectable(true);result.setPadding(0,dp(16),0,0);page.addView(result);
    }
    private void busy(boolean value){prepare.setEnabled(!value);read.setEnabled(!value);}
    private void prepare(){String repo=repository.getSelectedItem().toString(),q=question.getText().toString();List<String> selected=new ArrayList<>();String first=lead.getSelectedItem().toString();selected.add(first);for(String actor:LensClient.ACTORS)if(!actor.equals(first))selected.add(actor);int n;try{n=Integer.parseInt(cycles.getText().toString());}catch(Exception e){notice.setText("Cycles must be 1–6");return;}boolean md=metadata.isChecked();busy(true);notice.setText("Reading current GitHub manifest and instructions…");network.execute(()->{try{JSONObject p=LensClient.prepare(repo,q,selected,n,md);runOnUiThread(()->{try{evidence=p;submission=p.getString("submission_url");requestId.setText(p.getJSONObject("packet").getString("id"));notice.setText("Reference complete for preparation. Submit on GitHub to start the full scan.");}catch(Exception e){notice.setText(e.getMessage());}busy(false);});}catch(Exception e){runOnUiThread(()->{notice.setText(e.getMessage());busy(false);});}});}
    private void read(){String id=requestId.getText().toString().trim();busy(true);notice.setText("Reading one current receipt…");network.execute(()->{try{JSONObject x=LensClient.latestResult();String text=LensClient.display(x);runOnUiThread(()->{evidence=x;requestId.setText(x.optString("id"));runUrl=x.optString("run_url","");result.setText(text);notice.setText("Receipt read. No automatic polling.");busy(false);});}catch(Exception e){runOnUiThread(()->{notice.setText(e.getMessage());busy(false);});}});}
    @Override protected void onPause(){super.onPause();SharedPreferences.Editor e=prefs.edit().putInt("repo",repository.getSelectedItemPosition()).putString("question",question.getText().toString()).putString("request",requestId.getText().toString()).putString("cycles",cycles.getText().toString()).putBoolean("metadata",metadata.isChecked());for(Map.Entry<String,CheckBox> s:slots.entrySet())e.putBoolean(s.getKey(),s.getValue().isChecked());e.apply();}
    @Override protected void onDestroy(){network.shutdownNow();super.onDestroy();}
}
