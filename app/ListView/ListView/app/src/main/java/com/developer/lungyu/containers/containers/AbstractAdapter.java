package com.developer.lungyu.containers.containers;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;

import java.util.List;

/**
 * Created by lungyu on 2017/1/25.
 */

public class AbstractAdapter extends BaseAdapter {
    private Context context;
    private LayoutInflater inflater;
    private List<IItem> items;
    private int count = 0;

    public AbstractAdapter(Context context, List<IItem> datasource){
        this.context = context;
        inflater = ((LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE));
        this.items = datasource;
    }

    @Override
    public int getCount() {
        if (items != null)
            return items.size();
        return 0;
    }

    @Override
    public Object getItem(int position) {
        return items.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = inflater.inflate(
                    items.get(position).getLayoutId(), null);
        }

        IItem item =  items.get(position);
        item.initView(position, convertView, parent);
        return convertView;
    }
}
