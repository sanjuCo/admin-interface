// I write search function using jquery.
$(document).ready(function(){

    $form = $('.search-form')
    $loader = $('.loader-wrapper')
    $form.on('submit', function(e){
        /* 
        I prepopulate the value of the search 
        field with the value of the date field
        because search field is required.
        */
       
        $loader.css('display', 'block')
        $form = $(this)
        e.preventDefault();
        // Data we need
        $url = $(this).data('url')
        $formData = $(this).serialize();

        // Made a request to the correct endpoint.
        $.ajax({
            type: 'GET',
            url: $url,
            data: {
                $formData,
            },
            dataType: 'json',
            success: function(response){
                // We update necessary UI
                setTimeout(function(){
                    $loader.css('display', 'none')
                }, 1500)
                $type = $form.find("input[name='transc_type']").val();
                if($type == 'wit_transc'){
                    $con = $('#wit_tbody')
                    $con.empty()

                    if(response.wit_transc.length <= 0){
                        $con.append("<td colspan=3;'><span>404</span><br><br>The transaction you're searching for is not availalble.\n \
                            Try searching by ref code or by date.</td>")
                    }

                    $.each(response.wit_transc, function(index, obj){
                        $row = `
                            <tr>
                                <td>${obj.ref_code}</td>
                                <td>${obj.amount}</td>
                                <td>${obj.date}</td>
                            </tr> 
                        `
                        setTimeout(function(){
                            $con.append($row)
                        }, index*150);
                    });

                }else{
                    $con = $('#gen_tbody')
                    $con.empty()

                    if(response.gen_transc.length <= 0){
                        $con.append("<td colspan=5;'><span>404</span><br><br>The transaction you're searching for is not availalble.\n \
                            Try searching by ref code or by date.</td>")
                    }

                    $.each(response.gen_transc, function(index, obj){
                        $row = `
                            <tr>
                                <td>${obj.ref_code}</td>
                                <td>${obj.name}</td>
                                <td>${obj.number}</td>
                                <td>${obj.amount}</td>
                                <td>${obj.date}</td>
                            </tr> 
                        `
                        
                        setTimeout(function(){
                            $con.append($row)
                        }, index*150);
                    });
                }
                $form[0].reset();
            },
            error: function(xhr, errmsg, err){
                setTimeout(function(){
                    $loader.css('display', 'none')
                }, 1000)
                alert('Error, try again!!')
                console.log(xhr.status + ':' + xhr.responseText)
            }
        });
    });
});
