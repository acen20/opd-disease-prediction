var symptoms = document.querySelectorAll(".btn-symptom");
var count = 1;

symptoms.forEach((symptom) => {
  symptom.addEventListener("click", () => {
    symptom.classList.toggle("check");
    var ip = symptom.children[0];
    ip.value = Number(ip.value) ? "0" : "1";
    console.log(ip.value);
    if (ip.value) count += 1;
    else {
      count -= 1;
    }
  });
});

var search = () => {
  var element = document.querySelector("#searchBox");
  var query = element.value.toLowerCase();
  if (query.length > 0) {
    symptoms.forEach((symptom) => {
      if (symptom.children[1].innerHTML.toLowerCase().includes(query)) {
        symptom.classList.add("display");
      } else {
        symptom.classList.remove("display");
      }
    });
  } else {
    clear();
  }
};

var clear = () => {
  symptoms.forEach((symptom) => {
    symptom.classList.remove("display");
  });
};

var predict = () => {
  if (count) {
    var symptoms = document.querySelector("#symptoms-form");
    symptoms.submit();
  } else {
    alert("you didn't select any symptom");
  }
};
