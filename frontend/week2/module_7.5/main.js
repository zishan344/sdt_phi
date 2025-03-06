let count = 0;
document.getElementById("card_counter").innerText = count;
function displayLoading() {
  const search_loading = document.getElementById("search_loading");
  search_loading.innerHTML = `
    <div class="loading text-center">
      <p>Loading...</p>
    </div>
  `;
}

function hideLoading() {
  const search_loading = document.getElementById("search_loading");
  search_loading.innerHTML = "";
}

function searchProduct() {
  const search = document.getElementById("search-input").value;

  if (!search.trim()) return;
  displayLoading();
  fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${search}`)
    .then((res) => res.json())
    .then((data) => {
      hideLoading();
      displayMeal(data.meals);
    });
}
function displayMeal(meals) {
  const search_loading = document.getElementById("search_loading");
  const card_box = document.getElementById("card_box");
  search_loading.innerHTML = "";
  card_box.innerHTML = "";
  if (!meals || meals.length == 0) {
    const searchDiv = document.createElement("div");
    searchDiv.innerHTML = `
     <div class="text-center">
        <h2>Items Not Found</h2>
      </div>
    `;
    search_loading.appendChild(searchDiv);
    return;
  }
  meals.forEach((meal) => {
    const div = document.createElement("div");
    div.classList.add("col-4");
    div.classList.add("px-2");
    div.classList.add("my-2");
    div.innerHTML = `
              <div class="card ">
                <img
                  src=${meal?.strMealThumb}
                  class="card-img-top h-50 w-100"
                  alt="..." />
                <div class="card-body">
                  <h5 class="card-title">Name: ${meal?.strMeal}</h5>
                  <h5 class="fs-6">Category: ${meal?.strCategory}</h5>
                  <p class="card-text">
                    ${meal?.strInstructions.slice(0, 15)}...
                  </p>
                  <div class="text-center">
                    <button onClick="handleDetails('${
                      meal.idMeal
                    }')" type="button" class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#exampleModal"> Details</button>
                  </div>
                </div>
              </div>
     `;
    card_box.appendChild(div);
  });
}
function addToCard(name, img) {
  if (count == 7) return alert("You can't add more then 7 items");
  count += 1;
  document.getElementById("card_counter").innerText = count;
  const table_body = document.getElementById("table_body");
  const table_row = document.createElement("tr");
  table_row.innerHTML = `
                <th scope="row">${count}</th>
                <td>
                  <div style="width: 50px; height: 50px">
                    <img
                      class="w-100 h-100 rounded-circle"
                      src="${img}"
                      alt="" />
                  </div>
                </td>
                <td>${name}</td>            
  `;
  table_body.appendChild(table_row);
  console.log("add cart");
}
function handleDetails(id) {
  fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then((res) => res.json())
    .then((data) => displayDetails(data.meals[0]));
}
function displayDetails(item) {
  const detailsBox = document.getElementById("details_box");
  detailsBox.innerHTML = `
    <div style="width: 30rem;"  class="card p-0">
      <img src="${
        item.strMealThumb
      }" style="height:280px" class="card-img-top rounded" alt="${
    item.strMeal
  }" />
      <div class="card-body">
        <h5 class="card-title text-center">${item.strMeal}</h5>
        <p><strong>Category:</strong> ${item.strCategory}</p>
        <p><strong>Tag:</strong> ${item.strTags || "N/A"}</p>
        <p>${item.strInstructions.slice(0, 200)}</p>
        <div class="text-center">
          <button class="btn btn-outline-secondary" onclick="closeDetails()">Close</button>
        </div>
      </div>
    </div>
  `;
}

function closeDetails() {
  const detailsBox = document.getElementById("details_box");
  detailsBox.innerHTML = "";
}
