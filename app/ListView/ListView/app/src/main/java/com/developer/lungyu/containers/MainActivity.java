package com.developer.lungyu.containers;

import android.content.Context;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import com.developer.lungyu.containers.containers.AbstractAdapter;
import com.developer.lungyu.containers.containers.IItem;
import com.developer.lungyu.containers.containers.ItemMessage;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private List<IItem> datasource = new ArrayList<IItem>();
    private Context context = this;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //view binding
        listView = (ListView) findViewById(R.id.listview1);

        //set resouce
        getDatasource();
        AbstractAdapter adapter = new AbstractAdapter(context,datasource);
        listView.setAdapter(adapter);
        listView.setOnItemClickListener(onItemClickListener);
    }

    private void getDatasource(){
        datasource.add(new ItemMessage("鉛筆","20"));
        datasource.add(new ItemMessage("原子筆","30"));
        datasource.add(new ItemMessage("鋼筆","10"));
        datasource.add(new ItemMessage("毛筆","1"));
        datasource.add(new ItemMessage("彩色筆","24"));
    }

    private AdapterView.OnItemClickListener onItemClickListener = new AdapterView.OnItemClickListener() {
        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
            Toast.makeText(context,"Select " + position,Toast.LENGTH_SHORT).show();
        }
    };

}
