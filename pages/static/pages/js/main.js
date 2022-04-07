// let app = new Reef('#app');

var domReady = function (callback) {
  document.readyState === "interactive" || document.readyState === "complete"
    ? callback()
    : document.addEventListener("DOMContentLoaded", callback);
};

domReady(function () {
  document.querySelectorAll("a.mute").forEach(function (link) {
    console.log(link);
    link.addEventListener("click", function (event) {
      console.log(document.querySelector("a.mute"));
      event.preventDefault();
    });
  });
});
