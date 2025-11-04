const selected = document.getElementById("select-selected");
const optionsContainer = document.getElementById("select-items");

selected.addEventListener("click", () => {
  optionsContainer.classList.toggle("show"); // 'show' klassini qo'shish yoki olib tashlash
});

const options = optionsContainer.querySelectorAll("div");
options.forEach((option) => {
  option.addEventListener("click", () => {
    selected.innerText = option.innerText;
    optionsContainer.classList.remove("show"); // Tanlangan variantdan so'ng yopish
  });
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

  // Agar bosilgan joy searchInput yoki headerBox bo'lmasa
  if (
    !headerBox.contains(e.target) &&
    !input.contains(e.target) &&
    e.target !== lupaIcon
  ) {
    input.style.transform = "scaleX(0)"; // Inputni yashirish
    input.style.opacity = 0; // Inputni yashirish
    setTimeout(() => {
      input.style.display = "none"; // Inputni ko'rinmas qilish
      headerBox.style.width = "35px"; // Qaytadan dastlabki kenglik
      lupaIcon.style.display = "block"; // Lupa ikonkasini ko'rsatish
    }, 100); // 300ms - animatsiya davomiyligi
  }
});

// qidiruv list
function toggleSearchList() {
  const searchInput = document.getElementById("searchInput");
  const searchList = document.getElementById("searchList");

  // Agar inputda biror narsa bo'lsa, searchList'ni ko'rsat
  if (searchInput.value.trim() !== "") {
    searchList.style.display = "block";
  } else {
    searchList.style.display = "none";
  }
}
