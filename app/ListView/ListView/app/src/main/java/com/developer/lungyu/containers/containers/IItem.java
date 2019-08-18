package com.developer.lungyu.containers.containers;

import android.view.View;
import android.view.ViewGroup;

/**
 * Created by lungyu on 2017/1/25.
 */

public interface IItem {

    void initView(int position, View view, ViewGroup parent);

    int getLayoutId();

    void release();
}
