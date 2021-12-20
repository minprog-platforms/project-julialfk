function deleteSaved(restaurantId) {
// takes the restaurant id and redirects the id to the delete-saved page
  var delete_url = window.location.pathname.replace("/saved", "/delete-saved")

  fetch(delete_url, {
    method: "POST",
    body: JSON.stringify(restaurantId),
    success: function(response) {
      window.location.href = response.redirect;
    }
  })
}
