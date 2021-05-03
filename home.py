import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
from flask import Flask, render_template 
import os
import math

def kidney_properties(sample): 
    df = pd.read_csv (r'Kidney_Sample_Annotations.txt',sep="\t")
    vals=""
    for i in range(len(df)-1):
        print(df['SegmentDisplayName'][i],sample) 
        if(df['SegmentDisplayName'][i]==sample):
            vals=[df['disease_status'][i],df['pathology'][i],df['region'][i],df['AOINucleiCount'][i],df['RoiReportX'][i],df['RoiReportY'][i]]
            print(vals)
    return vals

def kidney_probe(sample):
    #https://www.spandidos-publications.com/10.3892/mmr.2017.7666
    main_target=["VEGFA","ACTN4","COL1A2","IGF1","HLA‑DPA1","NPHS1","NPHS2","WT1"]
    main_target_index=[4690,8245,3498,3381,16487,9316,15288,9117]
    df = pd.read_csv (r'Kidney_Raw_BioProbeCountMatrix.txt',sep="\t")
    vals=[]
    for i in main_target_index:
        vals.append(df[sample][i])
    print(vals)
    df = pd.DataFrame({'x': main_target, 'y': vals}) # creating a sample dataframe
    data = [
        go.Bar(
            name='BioProbe Count',
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]
    bar_plot= json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return bar_plot

def kidney_target(sample):
    #https://www.spandidos-publications.com/10.3892/mmr.2017.7666
    main_target=["VEGFA","ACTN4","COL1A2","IGF1","HLA‑DPA1","NPHS1","NPHS2","WT1"]
    main_target_index=[11312,14271,10301,10195,5384,15193,4325,15041]
    df = pd.read_csv (r'Kidney_Q3Norm_TargetCountMatrix.txt',sep="\t")
    vals=[]
    for i in main_target_index:
        vals.append(df[sample][i])
    print(vals)
    df = pd.DataFrame({'x': main_target, 'y': vals}) # creating a sample dataframe
    data = [
        go.Bar(
            name='Target Count',
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]
    bar_plot= json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return bar_plot
app = Flask(__name__,static_url_path='/static')
  
def get_file(path,addn):
    paths=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file.endswith(".png")):
                tmp=os.path.join(root,file)
                head, tail = os.path.split(tmp)
                tail=tail.replace(".png","")
                tail=addn+tail
                tmp=tmp.replace("/home/aniket/Desktop/Projects/nanostring","")
                paths.append([tmp,tail])
    print(paths)
    return paths
 
@app.route('/')
def index():
    paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/head_imgs","main/")
    return render_template('index.html', paths=paths )

@app.route("/main/img_det/<section>")
def detail(section):
    print(section)
    paths=[]
    names=section.split("-") 
    samplename=""
    if(len(names)==2):
        samplename=names[0]+" | "+names[1]+" | Geometric Segment"
    elif(len(names)==3):
        samplename=names[0]+" | "+names[1]+" | "+names[2]
    if "disease1B" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/d1b","img_det/") 
    elif "disease2B" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/d2b","img_det/")
    elif "disease3" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/d3","img_det/")
    elif "disease4" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/d4","img_det/")
    elif "normal2B" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/n2b","img_det/")
    elif "normal3" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/n3","img_det/")
    elif "normal4" in section: 
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/n4","img_det/")
    main_path=[]
    bar_plot1="{}"
    bar_plot2="{}"
    try:
        bar_plot1=kidney_target(samplename) 
    except:
        print("err")
    try:
        bar_plot2=kidney_probe(samplename)
    except:
        print("err")
    data_prop=kidney_properties(samplename)
    print(1,data_prop)
    for i in paths:
        if (section in i[0]):
            main_path.append(i)
            break
    return render_template('detail.html', section=section, paths=main_path, plot1=bar_plot1, plot2=bar_plot2 ,status=data_prop[0],patho=data_prop[1],region=data_prop[2],cnt=data_prop[3])

@app.route("/main/<section>")
def data(section):
    print(section)
    paths=None
    if "disease1B" in section: 
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/d1b","img_det/") 
    elif "disease2B" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/d2b","img_det/")
    elif "disease3" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/d3","img_det/")
    elif "disease4" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/d4","img_det/")
    elif "normal2B" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/n2b","img_det/")
    elif "normal3" in section:
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/n3","img_det/")
    elif "normal4" in section: 
        paths=get_file("/home/aniket/Desktop/Projects/nanostring/static/crp_imgs/n4","img_det/")
    print(paths)
    return render_template('display.html', section=section, paths=paths )




if __name__ == '__main__':
    app.run(debug=True)