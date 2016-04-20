$('.like').on('click', function(event){
    event.preventDefault();
    console.log("Liked!")  // sanity check
    like()
});

$('.dislike').on('click', function(event){
    event.preventDefault();
    console.log("Disliked!")  // sanity check
    dislike()
});

function like() {
    console.log("like is working!") // sanity check
    $.ajax({
    	url : 'comment_like', // the endpoint
    	type : 'GET', // http method
    	data : { like : $('#vlike').val() },

    	// handle a successful response
        success : function(json) {
            console.log(json.like); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }


    });
};

function dislike() {
    console.log("dislike is working!") // sanity check
    console.log($('#vdislike').val())
};
