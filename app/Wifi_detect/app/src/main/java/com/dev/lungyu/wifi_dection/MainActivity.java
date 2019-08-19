package com.dev.lungyu.wifi_dection;

import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.net.Uri;
import android.net.wifi.ScanResult;
import android.net.wifi.WifiManager;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.SimpleAdapter;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private Context context = this;
    private WifiManager wifiManager;
    private TextView txtStatus;
    private Spinner spinnerWifis;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txtStatus = (TextView) findViewById(R.id.textView);
        spinnerWifis = (Spinner) findViewById(R.id.spinner);

        openGPS(context);
        IsEnable();
        scan();
    }

    private void IsEnable(){
        //首先取得Wi-Fi服務控制Manager
        wifiManager = (WifiManager) getSystemService(Context.WIFI_SERVICE);
        String msgStatus = null;
        if(wifiManager.isWifiEnabled()){
            msgStatus = "Wifi is Enable";
        }else {
            msgStatus = "Wifi is disable";
            //wifiManager.setWifiEnabled(true);
        }

        txtStatus.setText(msgStatus);
    }

    private void scan() {


        // Register the Receiver in some part os fragment...
        registerReceiver(new BroadcastReceiver() {
            @Override
            public void onReceive(Context context, Intent intent) {
                wifiScanReceive();
            }
        }, new IntentFilter(WifiManager.SCAN_RESULTS_AVAILABLE_ACTION));

        wifiManager.startScan();

        // Inside the receiver:





    }


    private void wifiScanReceive(){
        // the result.size() is 0 after update to Android v6.0, same code working in older devices.
        List<ScanResult> scanResultList =  wifiManager.getScanResults();

        int size = scanResultList.size();
        final List<String> dataList = new ArrayList<String>(size);
        Toast.makeText(context,"scan result :" + size,Toast.LENGTH_SHORT).show();

         for(int i = 0 ; i <size  ; i++ )
        {
            //手機目前周圍的Wi-Fi環境
            String SSID  = scanResultList.get(i).SSID ;
            int LEVEL = scanResultList.get(i).level;
            String item = String.format("%s-%d",SSID,LEVEL);
            Log.d("wifi",item);
            dataList.add(item);
        }


        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                ArrayAdapter adapter = new ArrayAdapter(context,android.R.layout.simple_spinner_item,dataList);
                adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
                spinnerWifis.setAdapter(adapter);
            }
        });
    }

    public static final void openGPS(Context context) {
        Intent GPSIntent = new Intent();
        GPSIntent.setClassName("com.android.settings",
                "com.android.settings.widget.SettingsAppWidgetProvider");
        GPSIntent.addCategory("android.intent.category.ALTERNATIVE");
        GPSIntent.setData(Uri.parse("custom:3"));
        try {
            PendingIntent.getBroadcast(context, 0, GPSIntent, 0).send();
        } catch (PendingIntent.CanceledException e) {
            e.printStackTrace();
        }
    }
}
