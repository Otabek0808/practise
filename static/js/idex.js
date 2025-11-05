const languageSelector = document.getElementById("languageSelector");

// Uslublarni qo'shish
languageSelector.style.padding = "10px";
languageSelector.style.borderRadius = "5px";
languageSelector.style.cursor = "pointer";
languageSelector.style.transition = "0.3s ease"; // O'zgarish animatsiyasi
languageSelector.style.zIndex = "99";
languageSelector.style.border = "none";
languageSelector.style.boxSizing = "border-box";
languageSelector.style.boxShadow = "0 0 5px rgba(255, 255, 255, 0.7)";
languageSelector.style.backdropFilter = "blur(30px)";

// Focus va blur hodisalari
languageSelector.addEventListener("focus", function () {
  this.style.backgroundColor = "rgba(255, 255, 255, 0.1)"; // Tanlanganda fon rangi
  this.style.color = "white"; // Tanlanganda matn rangi
  this.style.transition = "background-color 0.3s ease"; // Animatsiya
});

languageSelector.addEventListener("blur", function () {
  // Qaytish fon rangi
  this.style.color = "withe"; // Qaytish matn rangi
  this.style.transition = "background-color 0.3s ease"; // Animatsiya
});

// Hover hodisasi
languageSelector.addEventListener("mouseover", function () {
  this.style.boxShadow = "0 0 10px rgba(255, 255, 255, 0.7)"; // Hoverda soyali effekt
});

languageSelector.addEventListener("mouseout", function () {
  this.style.boxShadow = "0 0 5px rgba(255, 255, 255, 0.7)"; // Hoverdan chiqganda qaytish
});

window.addEventListener("click", (e) => {
  if (!selected.contains(e.target)) {
    optionsContainer.classList.remove("show"); // Tashqaridan bosilganda yopish
  }
});

// qidiruv Hajm

// qidiruv list

const searchInput = document.getElementById("searchInput");
const searchList = document.getElementById("searchList");

// Dastlabki holatda searchList ni yashirish
searchList.style.display = "none";

// Inputga harf kiritilganda
searchInput.addEventListener("input", function () {
  // Agar inputda biror narsa bo'lsa, searchList'ni ko'rsat
  if (searchInput.value.trim() !== "") {
    searchList.style.display = "block";
  } else {
    searchList.style.display = "none"; // Bo'sh bo'lsa, yashirish
  }
});

// Enter tugmasi bosilganda searchList'ni ko'rsatish
searchInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    if (searchInput.value.trim() !== "") {
      searchList.style.display = "block"; // Enter bosilganda ko'rsatish
    }
  }
});

// Tashqariga bosilganda searchList'ni yashirish
document.addEventListener("click", function (event) {
  if (!searchList.contains(event.target) && event.target !== searchInput) {
    searchList.style.display = "none"; // Tashqariga bosilganda yashirish
  }
});
document.addEventListener("click", function (event) {
  const isClickInside =
    searchList.contains(event.target) || event.target === searchInput;

  if (!isClickInside) {
    searchList.style.display = "none"; // Tashqariga bosilganda yashirish
  }
});

// ekran tusi seach displey block
const overlay = document.createElement("div");
overlay.style.position = "fixed";
overlay.style.top = "0";
overlay.style.left = "0";
overlay.style.width = "100%";
overlay.style.height = "100%";
overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
overlay.style.display = "none"; // Dastlab yashirin
overlay.style.zIndex = "999"; // Yuqori qatlamda ko'rsatish
document.body.appendChild(overlay);

searchInput.addEventListener("input", function () {
  if (searchList.style.display === "block") {
    overlay.style.display = "block"; // Overlay ko'rsatiladi
  } else {
    overlay.style.display = "none"; // Overlay yashirin
  }
});

searchList.addEventListener("click", function () {
  searchList.style.display = "block"; // Ro'yxat ko'rsatiladi
  overlay.style.display = "block"; // Overlay ko'rsatiladi
});

document.addEventListener("click", function (event) {
  const isClickInside =
    searchList.contains(event.target) || event.target === searchInput;

  if (!isClickInside) {
    searchList.style.display = "none"; // Tashqariga bosilganda yashirish
    overlay.style.display = "none"; // Overlay'ni yashirish
  }
});
