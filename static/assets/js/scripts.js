
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
            dom: 'lBfrtip', 
            data:data.Final_result,
            columns: [
                { data: 'Nom Com' },
                { data: 'Code Iris' },
                { data: 'Rank of ScoreGlobal' },
                { data: 'Nom Iris' },
                { data: 'Population' },
                { data: 'Score Global' },
                { data: 'Acces Aux_interfaces_numeriques_intercommunalite' },
                { data: 'Access Al_information_intercommunalite' },
                { data: 'competences_administative_intercommunalite' },
                { data: 'competence_numeriques_intercommunalite' },
                { data: 'global_access_intercommunalite' },
                { data: 'global_competence_intercommunalite' }
            ],
        buttons: [
            'copyHtml5',
            'excelHtml5',
            'csvHtml5' 
        ],
        "deferLoading": 50,
        "info": false,
        recordsTotal:data.total_count,
        "deferRender": true,
            scrollY:        "500px",
            scrollX:        true,
            scrollCollapse: true,
            paging:         true,
            lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
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
                var optionText = 'ALL'; 
                var optionValue = 'ALL'; 
      
                $('#inputDepartment').append(new Option(optionText, optionValue)); 
                $(response.data.distinct_filter).each(function () {
                    $("<option />", {
                        val: this,
                        text: this
                    }).appendTo("#inputDepartment");
                });                
                $('#inputDepartment option[value="ALL"]').attr("selected",true);
                $("#inputDepartment").prop("disabled", false);
                $('#inputInterCommunalities').prop("disabled", true);
                $('#inputCommune').prop("disabled", true);  
                $('#inputInterCommunalities option[value="ALL"]').attr("selected",true);
                $('#inputCommune option[value="ALL"]').attr("selected",true);

                var datatable = $('#dataTable3').DataTable();
                datatable.clear().draw();
                datatable.rows.add(response.data.Final_result); // Add new data
                datatable.columns.adjust().draw(); // Redraw the DataTable

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
                 
                 var optionText = 'ALL'; 
                 var optionValue = 'ALL'; 
       
                 $('#inputInterCommunalities').append(new Option(optionText, optionValue)); 
                 $(response.data.distinct_filter).each(function () {
                     $("<option />", {
                         val: this,
                         text: this
                     }).appendTo("#inputInterCommunalities");
                 });
                 $('#inputDepartment option[value="ALL"]').attr("selected",true);
                 $("#inputInterCommunalities").prop("disabled", false); 
                 $("#inputCommune").prop("disabled", true);
                 $('#inputCommune option[value="ALL"]').attr("selected",true);

                 var datatable = $('#dataTable3').DataTable();
                 datatable.clear().draw();
                 datatable.rows.add(response.data.Final_result); // Add new data
                 datatable.columns.adjust().draw(); // Redraw the DataTable
 
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
                 var optionText = 'ALL'; 
                 var optionValue = 'ALL'; 
       
                 $('#inputCommune').append(new Option(optionText, optionValue)); 
                 $(response.data.distinct_filter).each(function () {
                     $("<option />", {
                         val: this,
                         text: this
                     }).appendTo("#inputCommune");
                 });
                 $('#inputDepartment option[value="ALL"]').attr("selected",true);
                 $("#inputCommune").prop("disabled", false); 


                 var datatable = $('#dataTable3').DataTable();
                 datatable.clear().draw();
                 datatable.rows.add(response.data.Final_result); // Add new data
                 datatable.columns.adjust().draw(); // Redraw the DataTable
 
 
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

                 var datatable = $('#dataTable3').DataTable();
                 datatable.clear().draw();
                 datatable.rows.add(response.data.Final_result); // Add new data
                 datatable.columns.adjust().draw(); // Redraw the DataTable
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
                 var datatable = $('#dataTable3').DataTable();
                 datatable.clear().draw();
                 datatable.rows.add(response.data.Final_result); // Add new data
                 datatable.columns.adjust().draw(); // Redraw the DataTable
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

                 var datatable = $('#dataTable3').DataTable();
                 datatable.clear().draw();
                 datatable.rows.add(response.data.Final_result); // Add new data
                 datatable.columns.adjust().draw(); // Redraw the DataTable
             },
             error: function(error){console.log(error)}
         });
     })


})(jQuery);