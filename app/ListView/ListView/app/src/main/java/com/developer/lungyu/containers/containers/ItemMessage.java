package com.developer.lungyu.containers.containers;

import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.developer.lungyu.containers.R;

/**
 * Created by lungyu on 2017/1/25.
 */

public class ItemMessage implements IItem {

    private String title;
    private String detail;
    public ItemMessage(String title,String detail){
        this.title = title;
        this.detail = detail;
    }


    @Override
    public void initView(int position, View view, ViewGroup parent) {
        TextView txtTitle = (TextView) view.findViewById(R.id.txtTitle);
        TextView txtDetail = (TextView) view.findViewById(R.id.txtDetail);

        txtTitle.setText(title);
        txtDetail.setText(detail);
    }

    @Override
    public int getLayoutId() {
        return R.layout.item_view;
    }

    @Override
    public void release() {

    }
}
