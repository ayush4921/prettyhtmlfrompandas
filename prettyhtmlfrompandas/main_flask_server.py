def makehtml(df,name):
    import os
    from flask import Flask, flash, request, redirect, url_for, render_template
    import pandas as pd

    
    f = open(os.path.join(os.getcwdb(),'static','style.css'), "w")
    f.write(

        '''
        /*	
            Side Navigation Menu V2, RWD
            ===================
            Author: @heyPablete

        */

        @charset "UTF-8";
        @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);
        
        body {
        font-family: 'Open Sans', sans-serif;
        font-weight: 300;
        line-height: 1.42em;
        color:#A7A1AE;
        background-color:#1F2739;
        }
        
        h1 {
        font-size:3em; 
        font-weight: 300;
        line-height:1em;
        text-align: center;
        color: #4DC3FA;
        }
        
        h2 {
        font-size:1em; 
        font-weight: 300;
        text-align: center;
        display: block;
        line-height:1em;
        padding-bottom: 2em;
        color: #FB667A;
        }
        
        h2 a {
        font-weight: 700;
        text-transform: uppercase;
        color: #FB667A;
        text-decoration: none;
        }
        
        .blue { color: #185875; }
        .yellow { color: #FFF842; }
        
        .container th h1 {
            font-weight: bold;
            font-size: 1em;
        text-align: left;
        color: #185875;
        }
        
        .container td {
            font-weight: normal;
            font-size: 1em;
        -webkit-box-shadow: 0 2px 2px -2px #0E1119;
            -moz-box-shadow: 0 2px 2px -2px #0E1119;
                box-shadow: 0 2px 2px -2px #0E1119;
        }
        
        .container {
            text-align: left;
            overflow: hidden;
            width: 80%;
            margin: 0 auto;
        display: table;
        padding: 0 0 8em 0;
        }
        
        .container td, .container th {
            padding-bottom: 2%;
            padding-top: 2%;
        padding-left:2%;  
        }
        
        /* Background-color of the odd rows */
        .container tr:nth-child(odd) {
            background-color: #323C50;
        }
        
        /* Background-color of the even rows */
        .container tr:nth-child(even) {
            background-color: #2C3446;
        }
        
        .container th {
            background-color: #1F2739;
        }
        
        .container td:first-child { color: #FB667A; }
        
        .container tr:hover {
            background-color: #464A52;
        -webkit-box-shadow: 0 6px 6px -6px #0E1119;
            -moz-box-shadow: 0 6px 6px -6px #0E1119;
                box-shadow: 0 6px 6px -6px #0E1119;
        }
        
        .container td:hover {
        background-color: #FFF842;
        color: #403E10;
        font-weight: bold;
        
        box-shadow: #7F7C21 -1px 1px, #7F7C21 -2px 2px, #7F7C21 -3px 3px, #7F7C21 -4px 4px, #7F7C21 -5px 5px, #7F7C21 -6px 6px;
        transform: translate3d(6px, -6px, 0);
        
        transition-delay: 0s;
            transition-duration: 0.4s;
            transition-property: all;
        transition-timing-function: line;
        }
        
        @media (max-width: 800px) {
        .container td:nth-child(4),
        .container th:nth-child(4) { display: none; }
        }


        '''
    )
    f.close()

    
    f = open(os.path.join(os.getcwdb(),'templates','hello.html'), "w")
    f.write(

        '''
        
            <!DOCTYPE html>
            <html lang="en" >
            <head>
            <meta charset="UTF-8">
            <title>{{name}}</title>
            <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css'><link rel="stylesheet" href="..\static\css\style.css">

            </head>
            <h1>{{name}}</h1>
            <body>
            <!-- partial:index.partial.html -->
            <div class="container">
                <div class="header_wrap">
                    <div class="num_rows">
                    
                            <div class="form-group"> 	<!--		Show Numbers Of Rows 		-->
                                <select class  ="form-control" name="state" id="maxRows" style="width: 20%;>
                                    
                                    
                                    <option value="10">10</option>
                                    <option value="15">15</option>
                                    <option value="20">20</option>
                                    <option value="50">50</option>
                                    <option value="70">70</option>
                                    <option value="100">100</option>
                        <option value="5000">Show ALL Rows</option>
                                    </select>
                                
                            </div>
                    </div>
                    <div class="tb_search">
            <input type="text" id="search_input_all" onkeyup="FilterkeyWord_all_table()" placeholder="Search.." class="form-control" style="width: 20%;">
            <br>
                    </div>
                </div>
            
            {% for table in tables %}
            {{titles[loop.index]}}
            {{ table|safe }}
            {% endfor %}




            <style>
                .alert {
                padding: 20px;
                background-color: #f44336;
                color: white;
                opacity: 1;
                transition: opacity 0.6s;
                margin-bottom: 15px;
                }
                
                .alert.success {background-color: #4CAF50;}
                .alert.info {background-color: #2196F3;}
                .alert.warning {background-color: #ff9800;}
                
                .closebtn {
                margin-left: 15px;
                color: white;
                font-weight: bold;
                float: right;
                font-size: 22px;
                line-height: 20px;
                cursor: pointer;
                transition: 0.3s;
                }
                
                .closebtn:hover {
                color: black;
                }
                </style>
                </head>
                <body>
                
                
                
                <script>
                var close = document.getElementsByClassName("closebtn");
                var i;
                
                for (i = 0; i < close.length; i++) {
                close[i].onclick = function(){
                    var div = this.parentElement;
                    div.style.opacity = "0";
                    setTimeout(function(){ div.style.display = "none"; }, 600);
                }
                }
                </script>

            <!--		Start Pagination -->
                        <div class='pagination-container'>
                            <nav>
                            <ul class="pagination">
                            <!--	Here the JS Function Will Add the Rows -->
                            </ul>
                            </nav>
                        </div>
                <div class="rows_count">Showing 11 to 20 of 91 entries</div>
                <br>
                
            </div> <!-- 		End of Container -->



            <!--  Developed By Yasser Mas -->
            <!-- partial -->
            <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.2/jquery.min.js'></script>
            <script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js'></script><script  src="..\static\js\script.js"></script>

            </body>
            </html>



        '''
    )
    f.close()
    app = Flask(__name__)
    
    @app.route('/', methods=['GET', 'POST'])
    def hello_world():
        df=df
        name=name
        return render_template("hello.html",df=df,tables=[df.to_html(index=False,classes="table table-class",table_id="table-id",border=0)], titles=df.columns.values,name=name)    
    if __name__ == '__main__':
        app.run(debug=True)



