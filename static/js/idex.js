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

// kiyingi
document.getElementById("lupaIcon").addEventListener("click", function () {
  const headerBox = document.getElementById("headerBox");
  const input = document.getElementById("searchInput");

  if (headerBox.style.width === "35px" || headerBox.style.width === "") {
    headerBox.style.width = "500px"; // Kengaytiriladigan yangi kenglik
    input.style.display = "block"; // Inputni ko'rsatish
    this.style.display = "none"; // Lupa ikonkasini yashirish
    setTimeout(() => {
      input.style.transform = "scaleX(1)"; // Inputni ko'rsatish
      input.style.opacity = 1; // Inputni ko'rsatish
    }, 100); // 10ms kutish
  }
});

// Tashqariga bosilganda dastlabki holatga qaytish
window.addEventListener("click", function (e) {
  const headerBox = document.getElementById("headerBox");
  const input = document.getElementById("searchInput");
  const lupaIcon = document.getElementById("lupaIcon");
  const searchBack = document.getElementById("searchBack"); // Yangi element

  // Dastlabki holatda headerBox kengligi 35px va searchBack ko'rinmas
  if (headerBox.style.width === "") {
    headerBox.style.width = "35px"; // Dastlabki holat
    searchBack.style.display = "none"; // Dastlabki holatda searchBack ko'rinmaydi
  }

  if (e.target === lupaIcon) {
    // Lupa ikonkasi bosilganda
    headerBox.style.width = "600px"; // Kengaytirish
    input.style.display = "block"; // Qidiruv maydonini ko'rsatish
    searchBack.style.display = "block"; // searchBack ko'rinadi
    setTimeout(() => {
      input.style.transform = "scaleX(1)"; // Qidiruv maydonini ko'rsatish
      input.style.opacity = 1; // Qidiruv maydonini ko'rsatish
    }, 10); // 10ms - animatsiya boshlanishi uchun
    lupaIcon.style.display = "none"; // Lupa ikonkasini yashirish
  } else if (e.target === searchBack) {
    // searchBack bosilganda
    input.style.transform = "scaleX(0)"; // Qidiruv maydonini yashirish
    input.style.opacity = 0;
    setTimeout(() => {
      input.style.display = "none"; // Qidiruv maydonini ko'rinmas qilish
      headerBox.style.width = "35px"; // Dastlabki kenglikka qaytish
      lupaIcon.style.display = "block"; // Lupa ikonkasini ko'rsatish
      searchBack.style.display = "none"; // searchBackni yashirish
    }, 100); // 100ms - animatsiya davomiyligi
  }
});

// qidiruv list

const searchInput = document.getElementById("searchInput");
const searchList = document.getElementById("searchList");
const searchBack = document.getElementById("searchBack");

// Dastlabki holatda searchList ni yashirish
searchList.style.display = "none";

// Inputga harf kiritilganda
searchInput.addEventListener("input", function () {
  // Agar inputda biror narsa bo'lsa, searchList'ni ko'rsat
  if (searchInput.value.trim() !== "") {
    searchList.style.display = "block";
  } else {
    searchList.style.display = "none";
  }
});

// Tashqariga bosilganda searchList'ni yashirish
document.addEventListener("click", function (event) {
  if (!searchList.contains(event.target) && event.target !== searchInput) {
    searchList.style.display = "none"; // searchBackni ham yashirish
  }
});
