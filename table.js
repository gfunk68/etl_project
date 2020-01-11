// JavaScript Document
$(document).ready(function() {
    
    //use ajax .get to retrieve the table html and return to the table div
     $.get("data.html", function(data, status){
         //assign the table html to div
         $('#tableDiv').html(data);
         //add the bootstrap classes to the table item
         $('table').each(function(i){
             $(this).addClass('table',i);
             $(this).addClass('table-striped',i);
             $(this).addClass('table-responsive',i);
         }); 
     });
 });