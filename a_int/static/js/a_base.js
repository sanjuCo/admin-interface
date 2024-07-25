 //I control the profile modal
 $(document).ready(function(){
    let modal = $('.profile-modal');
    let profile = $('#profile');

    profile.on('click', function(e){
        e.preventDefault();
        if(modal.css('display') === 'none'){
            modal.css('display', 'flex');
        }else{
            modal.css('display', 'none');
        }
    })
    $(document).on('click', function(e) {
        if ($(e.target).closest(modal).length === 0 && $(e.target).closest(profile).length === 0) {
            modal.css('display', 'none');
        }
    });
})


// I control the withdrawing form
$(document).ready(function(){
    let w_modal = $('.withdraw-modal');
    let withdraw = $('.withdraw');
    withdraw.on('click', function(e){
        e.preventDefault();
        if(w_modal.css('display') === 'none'){
            w_modal.css('display', 'flex');
        }else{
            w_modal.css('display', 'none');
        }
    });
    $(document).on('click', function(e){
        if ($(e.target).closest('.withdraw-modal').length === 0 && $(e.target).closest('.withdraw').length === 0) {
            w_modal.css('display', 'none');
        }
    })
});

// Feedback form
$(document).ready(function(){
    let feedback = $('.feedback')
    let feedback_form = $('#feedback-form')

    feedback.on('click', function(e){
        e.preventDefault();
        if(feedback_form.css('display') === 'none'){
            feedback_form.css('display', 'flex');
        }else{
            feedback_form.css('display', 'none');
        }
    });
    $(document).on('click', function(e){
        if($(e.target).closest('#feedback-form').length === 0 && $(e.target).closest('.feedback').length === 0){
            feedback_form.css('display', 'none');
        }
    });
});