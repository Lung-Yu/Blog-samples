package com.developer.lungyu.ocr_sample;

import android.graphics.Bitmap;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.googlecode.tesseract.android.TessBaseAPI;

public class MainActivity extends AppCompatActivity {


    static final String TESSBASE_PATH = "/storage/emulated/0/download/tesseract/";
    static final String DEFAULT_LANGUAGE = "eng";
    static final String CHINESE_LANGUAGE = "chi_tra";


    ImageView imgSrc;
    TextView txtResult;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        imgSrc = (ImageView) findViewById(R.id.imageView);
        txtResult = (TextView) findViewById(R.id.textView1);
    }
    public void run(View v){
        String ocrResult = ocrWithEnglish();
        txtResult.setText(ocrResult);
    }
    public String ocrWithEnglish() {
        String resString = "";

        imgSrc.setDrawingCacheEnabled(true);
        final Bitmap bitmap = imgSrc.getDrawingCache();
        final TessBaseAPI ocrApi = new TessBaseAPI();

        ocrApi.init(TESSBASE_PATH, CHINESE_LANGUAGE);
        ocrApi.setPageSegMode(TessBaseAPI.PageSegMode.PSM_SINGLE_LINE);

        ocrApi.setImage(bitmap);
        resString = ocrApi.getUTF8Text();

        ocrApi.clear();
        ocrApi.end();
        return  resString;
    }
}
