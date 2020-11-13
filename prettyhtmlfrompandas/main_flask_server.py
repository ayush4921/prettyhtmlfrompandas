import os
from flask import Flask, flash, request, redirect, url_for, render_template
import pandas as pd


def makehtml(df,name):

    app = Flask(__name__)



    @app.route('/', methods=['GET', 'POST'])
    def hello_world():
        name='Ayush'

            

        
            

        return render_template("hello.html",df=df,tables=[df.to_html(index=False,classes="table table-class",table_id="table-id",border=0)], titles=df.columns.values,name=name)
    
        

        
        #return render_template("index.html",abc=abc,list123=list123,drawer1=drawer1,drawer2=drawer2,drawer3=drawer3,lenth=lenth,len_drawer1=len_drawer1,len_drawer2=len_drawer2,len_drawer3=len_drawer3)
        #return render_template("hello.html",tables=[df.to_html(classes="table table-striped table-class",table_id="table-id",border=0)], titles=df.columns.values)


        
            

    


    if __name__ == '__main__':
        app.run(debug=True)