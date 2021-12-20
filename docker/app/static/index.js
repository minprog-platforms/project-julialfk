function deleteSaved(restaurantId) {
// takes the restaurant id and redirects the id to the delete-saved page
  fetch("{{ url_for('views.delete_saved') }}", {
    method: "POST",
    body: JSON.stringify(restaurantId),
  }).then((_res) => {
    window.location.href = "{{ url_for('views.saved') }}";
  });
}
