// Adding and deletion modals.
$(document).ready(function(){
    let add_prod = $('#add-prod');
    let del_prod = $('#del-prod');
    let add_item = $('#add-item');
    let del_item = $('#del-item');
    let add_prod_modal = $('#add-prod-modal');
    let add_item_modal = $('#add-item-modal');
    let del_prod_modal = $('#del-prod-modal');
    let del_item_modal = $('#del-item-modal');


    // Product modals
    add_prod.on('click', function(){
        if(add_prod_modal.css('display') === 'none'){
            add_prod_modal.css('display', 'flex');
        }else{
            add_prod_modal.css('display', 'none');
        }
    });
    $(document).on('click', function(e){
        if($(e.target).closest('#add-prod-modal').length === 0  && $(e.target).closest('#add-prod').length === 0){
            add_prod_modal.css('display', 'none');
        }
    });
    del_prod.on('click', function(){
        if(del_prod_modal.css('display') === 'none'){
            del_prod_modal.css('display', 'flex');
        }else{
            del_prod_modal.css('display', 'none');
        }
    });
    $(document).on('click', function(e){
        if($(e.target).closest('#del-prod-modal').length === 0 && $(e.target).closest('#del-prod').length === 0){
            del_prod_modal.css('display', 'none');
        }
    });


    // Item modals 
    add_item.on('click', function(){
        if(add_item_modal.css('display') === 'none'){
            add_item_modal.css('display', 'flex');
        }else{
            add_item_modal.css('display', 'none');
        }
    });
    $(document).on('click', function(e){
        if($(e.target).closest('#add-item-modal').length === 0  && $(e.target).closest('#add-item').length === 0){
            add_item_modal.css('display', 'none')
        }
    });
    del_item.on('click', function(){
        if(del_item_modal.css('display') === 'none'){
            del_item_modal.css('display', 'flex');
        }else{
            del_item_modal.css('display', 'none');
        }
    });
    $(document).on('click', function(e){
        if($(e.target).closest('#del-item-modal').length === 0 && $(e.target).closest('#del-item').length === 0){
            del_item_modal.css('display', 'none');
        }
    });
});

// Item images logic
$(document).ready(function(){
    let img1 = $('#img1')
    let img2 = $('#img2')
    let img3 = $('#img3')
    let img_input1 = $('#id_f1')
    let img_input2 = $('#id_f2')
    let img_input3 = $('#id_f3')

    img1.on('click', function(){
        img_input1.click();
    });
    img_input1.on('change', function(e){
        let image = e.target.files[0]
        if(image){
            let url = URL.createObjectURL(image)
            img1.empty().append(`<img src=${url} alt="First Item image.">`);
        }
    });
    

    img2.on('click', function(){
        img_input2.click();
    });
    img_input2.on('change', function(e){
        let image = e.target.files[0]
        if(image){
            let url = URL.createObjectURL(image)
            img2.empty().append(`<img src=${url} alt="First Item image.">`);
        }
    });


    img3.on('click', function(){
        img_input3.click();
    });
    img_input3.on('change', function(e){
        let image = e.target.files[0]
        if(image){
            let url = URL.createObjectURL(image)
            img3.empty().append(`<img src=${url} alt="First Item image.">`);
        }
    });
});