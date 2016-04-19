$('.like').on('click', function(event){
    event.preventDefault();
    console.log("Liked!")  // sanity check
});

$('.dislike').on('click', function(event){
    event.preventDefault();
    console.log("Disliked!")  // sanity check
});
