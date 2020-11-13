def makehtml(df,name):
    import os
    from flask import Flask, flash, request, redirect, url_for, render_template
    import pandas as pd

    app = Flask(__name__)
    
    @app.route('/', methods=['GET', 'POST'])
    def hello_world():
        df=df
        name=name
        return render_template("hello.html",df=df,tables=[df.to_html(index=False,classes="table table-class",table_id="table-id",border=0)], titles=df.columns.values,name=name)    
    if __name__ == '__main__':
        app.run(debug=True)

