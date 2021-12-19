
function deleteSaved(restaurantId) {
  fetch("/delete-saved", {
    method: "POST",
    body: JSON.stringify(restaurantId),
  }).then((_res) => {
    window.location.href = "/";
  });
}
