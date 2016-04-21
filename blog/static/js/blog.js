// AJAX for posting
function liked(id) {
    console.log("Funcion ajax") // sanity check
    console.log("id que del comentario que hemos guardado en el boton: "+id) // sanity check
    pk = id.split("_")[2];
    $.ajax({
        url : "/comment/"+pk+"/like", // the endpoint
        type : "POST", // http method

        // handle a successful response
        success : function(json) {
		    console.log(json); // log the returned json to the console
		    $("#val_likes_"+pk).html(json.response_text_contador);
		    console.log("success"); // another sanity check, prepend añade al principio
		},

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
// AJAX for posting
function disliked(id) {
    console.log("Funcion ajax") // sanity check
    console.log(id) // sanity check
    pk = id.split("_")[2];
    $.ajax({
        url : "/comment/"+pk+"/dislike", // the endpoint
        type : "POST", // http method

        // handle a successful response
        success : function(json) {
		    console.log(json); // log the returned json to the console
		    $("#val_dislikes_"+pk).html(json.response_text_contador);
		    console.log("success"); // another sanity check, prepend añade al principio
		},

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$('.like_btn').on('click', function(event){
    event.preventDefault();
<<<<<<< HEAD
    console.log("Liked!")  // sanity check
    like()
=======
    console.log("Start Liked!")  // sanity check
    liked(this.id)
>>>>>>> dev
});

$('.dislike_btn').on('click', function(event){
    event.preventDefault();
<<<<<<< HEAD
    console.log("Disliked!")  // sanity check
    dislike()
=======
    console.log("Start Disliked!")  // sanity check
    disliked(this.id)
>>>>>>> dev
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
