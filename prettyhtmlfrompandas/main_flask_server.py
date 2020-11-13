
class makehtml:
    def __init__(self,df,name):
        from flask import Flask, flash, request, redirect, url_for, render_template
        import pandas as pd
        app = Flask(__name__)

        @app.route('/', methods=['GET', 'POST'])
        def hello_world():
            print(2)
            return render_template("hello.html",df=df,tables=[df.to_html(index=False,classes="table table-class",table_id="table-id",border=0)], titles=df.columns.values,name=name)    
        
        app.run()
    
    @staticmethod
    def makefiles():
        import os
        


        path=os.getcwd()
        

        jsfile='''
                
                getPagination('#table-id');
                    $('#maxRows').trigger('change');
                    function getPagination (table){

                        $('#maxRows').on('change',function(){
                            $('.pagination').html('');						// reset pagination div
                            var trnum = 0 ;									// reset tr counter 
                            var maxRows = parseInt($(this).val());			// get Max Rows from select option
                        
                            var totalRows = $(table+' tbody tr').length;		// numbers of rows 
                            $(table+' tr:gt(0)').each(function(){			// each TR in  table and not the header
                                trnum++;									// Start Counter 
                                if (trnum > maxRows ){						// if tr number gt maxRows
                                    
                                    $(this).hide();							// fade it out 
                                }if (trnum <= maxRows ){$(this).show();}// else fade in Important in case if it ..
                            });											//  was fade out to fade it in 
                            if (totalRows > maxRows){						// if tr total rows gt max rows option
                                var pagenum = Math.ceil(totalRows/maxRows);	// ceil total(rows/maxrows) to get ..  
                                                                            //	numbers of pages 
                                for (var i = 1; i <= pagenum ;){			// for each page append pagination li 
                                $('.pagination').append('<li data-page="'+i+'">\
                                                    <span>'+ i++ +'<span class="sr-only">(current)</span></span>\
                                                    </li>').show();
                                }											// end for i 
                    
                        
                            } 												// end if row count > max rows
                            $('.pagination li:first-child').addClass('active'); // add active class to the first li 
                        
                        
                        //SHOWING ROWS NUMBER OUT OF TOTAL DEFAULT
                    showig_rows_count(maxRows, 1, totalRows);
                        //SHOWING ROWS NUMBER OUT OF TOTAL DEFAULT

                        $('.pagination li').on('click',function(e){		// on click each page
                        e.preventDefault();
                                var pageNum = $(this).attr('data-page');	// get it's number
                                var trIndex = 0 ;							// reset tr counter
                                $('.pagination li').removeClass('active');	// remove active class from all li 
                                $(this).addClass('active');					// add active class to the clicked 
                        
                        
                        //SHOWING ROWS NUMBER OUT OF TOTAL
                    showig_rows_count(maxRows, pageNum, totalRows);
                        //SHOWING ROWS NUMBER OUT OF TOTAL
                        
                        
                        
                                $(table+' tr:gt(0)').each(function(){		// each tr in table not the header
                                    trIndex++;								// tr index counter 
                                    // if tr index gt maxRows*pageNum or lt maxRows*pageNum-maxRows fade if out
                                    if (trIndex > (maxRows*pageNum) || trIndex <= ((maxRows*pageNum)-maxRows)){
                                        $(this).hide();		
                                    }else {$(this).show();} 				//else fade in 
                                }); 										// end of for each tr in table
                                    });										// end of on click pagination list
                        });
                                                            // end of on select change 
                        
                                                // END OF PAGINATION 
                    
                    }	


                            

                // SI SETTING
                $(function(){
                    // Just to append id number for each row  
                default_index();
                                    
                });

                //ROWS SHOWING FUNCTION
                function showig_rows_count(maxRows, pageNum, totalRows) {
                //Default rows showing
                        var end_index = maxRows*pageNum;
                        var start_index = ((maxRows*pageNum)- maxRows) + parseFloat(1);
                        var string = 'Showing '+ start_index + ' to ' + end_index +' of ' + totalRows + ' entries';               
                        $('.rows_count').html(string);
                }

                // CREATING INDEX
                function default_index() {
                $('table tr:eq(0)').prepend('<th> ID </th>')

                                    var id = 0;

                                    $('table tr:gt(0)').each(function(){	
                                        id++
                                        $(this).prepend('<td>'+id+'</td>');
                                    });
                }

                // All Table search script
                function FilterkeyWord_all_table() {
                
                // Count td if you want to search on all table instead of specific column

                var count = $('.table').children('tbody').children('tr:first-child').children('td').length; 

                        // Declare variables
                var input, filter, table, tr, td, i;
                input = document.getElementById("search_input_all");
                var input_value =     document.getElementById("search_input_all").value;
                        filter = input.value.toLowerCase();
                if(input_value !=''){
                        table = document.getElementById("table-id");
                        tr = table.getElementsByTagName("tr");

                        // Loop through all table rows, and hide those who don't match the search query
                        for (i = 1; i < tr.length; i++) {
                        
                        var flag = 0;
                        
                        for(j = 0; j < count; j++){
                            td = tr[i].getElementsByTagName("td")[j];
                            if (td) {
                            
                                var td_text = td.innerHTML;  
                                if (td.innerHTML.toLowerCase().indexOf(filter) > -1) {
                                //var td_text = td.innerHTML;  
                                //td.innerHTML = 'shaban';
                                flag = 1;
                                } else {
                                //DO NOTHING
                                }
                            }
                            }
                        if(flag==1){
                                    tr[i].style.display = "";
                        }else {
                            tr[i].style.display = "none";
                        }
                        }
                    }else {
                    //RESET TABLE
                    $('#maxRows').trigger('change');
                    }
                }

                '''
        try:
            os.makedirs(os.path.join(f'{path}','static','js'))
            path2=os.path.join(f'{path}','static','js','script.js')
            with open(path2, 'w') as f:
                f.write(jsfile)
        except:
            print(2)
        
        cssfile='''
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
        try:
            os.makedirs(os.path.join(f'{path}','static','css'))

            path1=os.path.join(f'{path}','static','css','style.css')
            with open(path1, 'w') as f:
                f.write(cssfile)
        except:
            print(2)


        htmlfile='''
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
        try:
            os.makedirs(os.path.join(f'{path}','templates'))
            path3=os.path.join(f'{path}','templates','hello.html')
            with open(path3, 'w') as f:
                f.write(htmlfile)
        except:
            pass
        


