window.addEventListener("DOMContentLoaded", () => {
  [...document.querySelectorAll(".hidden-answer")]
  .forEach(el => el.addEventListener("click", (e) => {
      e.currentTarget.classList.toggle("hidden-answer");
      e.currentTarget.classList.toggle("shown-answer");
  }))
})
