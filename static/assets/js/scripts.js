
(function($) {
    "use strict";

    /*================================
    Preloader
    ==================================*/

    var preloader = $('#preloader');
    $(window).on('load', function() {
        setTimeout(function() {
            preloader.fadeOut('slow', function() { $(this).remove(); });
        }, 300)
    });
 
    /*================================
    stickey Header
    ==================================*/
    $(window).on('scroll', function() {
        var scroll = $(window).scrollTop(),
            mainHeader = $('#sticky-header'),
            mainHeaderHeight = mainHeader.innerHeight();

        // console.log(mainHeader.innerHeight());
        if (scroll > 1) {
            $("#sticky-header").addClass("sticky-menu");
        } else {
            $("#sticky-header").removeClass("sticky-menu");
        }
    });

    
    /*================================
    datatable active
    ==================================*/
     
    if ($('#dataTable3').length) {
        $('#dataTable3').DataTable( {
            dom: 'Bfrtip',
        buttons: [
            'copyHtml5',
            'excelHtml5',
            'csvHtml5' 
        ],
            scrollY:        "500px",
            scrollX:        true,
            scrollCollapse: true,
            paging:         true,
            fixedColumns:   {
                leftColumns: 4,
                heightMatch: 'none'
            }
        } ); 
    } 

    
    /*================================
    Fullscreen Page
    ==================================*/

    if ($('#full-view').length) {

        var requestFullscreen = function(ele) {
            if (ele.requestFullscreen) {
                ele.requestFullscreen();
            } else if (ele.webkitRequestFullscreen) {
                ele.webkitRequestFullscreen();
            } else if (ele.mozRequestFullScreen) {
                ele.mozRequestFullScreen();
            } else if (ele.msRequestFullscreen) {
                ele.msRequestFullscreen();
            } else {
                console.log('Fullscreen API is not supported.');
            }
        };

        var exitFullscreen = function() {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen();
            } else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            } else if (document.msExitFullscreen) {
                document.msExitFullscreen();
            } else {
                console.log('Fullscreen API is not supported.');
            }
        };

        var fsDocButton = document.getElementById('full-view');
        var fsExitDocButton = document.getElementById('full-view-exit');

        fsDocButton.addEventListener('click', function(e) {
            e.preventDefault();
            requestFullscreen(document.documentElement);
            $('body').addClass('expanded');
        });

        fsExitDocButton.addEventListener('click', function(e) {
            e.preventDefault();
            exitFullscreen();
            $('body').removeClass('expanded');
        });
    }

    $('#inputRegion').change(function(){
       var posturl="/index_get_data";
       //var posturl = {{ url_for("stuff") }};
        var val = {
                    region: $(this).val(),
                    change : "region",
                    donnees_infra_communales : $("#inputDonnes").val(),
                    Choix_de_Point_Reference : $("#inputChoice").val()};
    
        $.ajax({
            type: 'POST',
            url: posturl, 
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(val),
            success: function(response){ 
                console.log(response.data); 
                $("#inputDepartment").html("");
                $(response.data.distinct_filter).each(function () {
                    $("<option />", {
                        val: this,
                        text: this
                    }).appendTo("#inputDepartment");
                });
                var optionText = 'All'; 
                var optionValue = 'All'; 
      
                $('#inputDepartment').append(new Option(optionText, optionValue)); 


            },
            error: function(error){console.log(error)}
        });
    })

    $('#inputDepartment').change(function(){
        var posturl="/index_get_data";
        //var posturl = {{ url_for("stuff") }};
         var val = {
                     region: $("#inputRegion").val(),
                     department : $(this).val(),
                     change : "department",
                     donnees_infra_communales : $("#inputDonnes").val(),
                     Choix_de_Point_Reference : $("#inputChoice").val()};
     
         $.ajax({
             type: 'POST',
             url: posturl, 
             dataType: 'json',
             contentType: 'application/json',
             data: JSON.stringify(val),
             success: function(response){ 
                 console.log(response.data); 
                 $("#inputInterCommunalities").html("");
                 $(response.data.distinct_filter).each(function () {
                     $("<option />", {
                         val: this,
                         text: this
                     }).appendTo("#inputInterCommunalities");
                 });
                 var optionText = 'All'; 
                 var optionValue = 'All'; 
       
                 $('#inputInterCommunalities').append(new Option(optionText, optionValue)); 
 
 
             },
             error: function(error){console.log(error)}
         });
     })
     
     $('#inputInterCommunalities').change(function(){
        var posturl="/index_get_data";
        //var posturl = {{ url_for("stuff") }};
         var val = {
                     region: $("#inputRegion").val(),
                     department : $("#inputDepartment").val(),
                     intercommunalities : $(this).val(),
                     change : "intercommunalities",
                     donnees_infra_communales : $("#inputDonnes").val(),
                     Choix_de_Point_Reference : $("#inputChoice").val()};
     
         $.ajax({
             type: 'POST',
             url: posturl, 
             dataType: 'json',
             contentType: 'application/json',
             data: JSON.stringify(val),
             success: function(response){ 
                 console.log(response.data); 
                 $("#inputCommune").html("");
                 $(response.data.distinct_filter).each(function () {
                     $("<option />", {
                         val: this,
                         text: this
                     }).appendTo("#inputCommune");
                 });
                 var optionText = 'All'; 
                 var optionValue = 'All'; 
       
                 $('#inputCommune').append(new Option(optionText, optionValue)); 
 
 
             },
             error: function(error){console.log(error)}
         });
     })

     $('#inputCommune').change(function(){
        var posturl="/index_get_data";
        //var posturl = {{ url_for("stuff") }};
         var val = {
                     region: $("#inputRegion").val(),
                     department : $("#inputDepartment").val(),
                     intercommunalities : $("#inputInterCommunalities").val(), 
                     change : "commune",
                     commune : $(this).val(),
                     donnees_infra_communales : $("#inputDonnes").val(),
                     Choix_de_Point_Reference : $("#inputChoice").val()};
     
         $.ajax({
             type: 'POST',
             url: posturl, 
             dataType: 'json',
             contentType: 'application/json',
             data: JSON.stringify(val),
             success: function(response){ 
                 console.log(response.data); 
             },
             error: function(error){console.log(error)}
         });
     })

     $('#inputChoice').change(function(){
        var posturl="/index_get_data";
        //var posturl = {{ url_for("stuff") }};
         var val = {
                     region: $("#inputRegion").val(),
                     department : $("#inputDepartment").val(),
                     intercommunalities : $("#inputInterCommunalities").val(), 
                     change : "Choix_de_Point_Reference",
                     commune : $("#inputCommune").val(),
                     donnees_infra_communales : $("#inputDonnes").val(),
                     Choix_de_Point_Reference : $(this).val()};
     
         $.ajax({
             type: 'POST',
             url: posturl, 
             dataType: 'json',
             contentType: 'application/json',
             data: JSON.stringify(val),
             success: function(response){ 
                 console.log(response.data); 
             },
             error: function(error){console.log(error)}
         });
     })

     $('#inputDonnes').change(function(){
        var posturl="/index_get_data";
        //var posturl = {{ url_for("stuff") }};
         var val = {
                     region: $("#inputRegion").val(),
                     department : $("#inputDepartment").val(),
                     intercommunalities : $("#inputInterCommunalities").val(), 
                     change : "donnees_infra_communales",
                     commune : $("#inputCommune").val(),
                     donnees_infra_communales : $(this).val(),
                     Choix_de_Point_Reference : $("#inputChoice").val()};
     
         $.ajax({
             type: 'POST',
             url: posturl, 
             dataType: 'json',
             contentType: 'application/json',
             data: JSON.stringify(val),
             success: function(response){ 
                 console.log(response.data); 
             },
             error: function(error){console.log(error)}
         });
     })


})(jQuery);