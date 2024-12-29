function submitForm() {
    const formData = {
      age: document.getElementById("age").value,
      sex: document.getElementById("sex").value,
      chestPain: document.getElementById("chestPain").value,
      bp: document.getElementById("bp").value,
      cholesterol: document.getElementById("cholesterol").value,
      fbs: document.getElementById("fbs").value,
      ekg: document.getElementById("ekg").value,
      maxHr: document.getElementById("maxHr").value,
      exerciseAngina: document.getElementById("exerciseAngina").value,
      stDepression: document.getElementById("stDepression").value,
      slope: document.getElementById("slope").value,
      vessels: document.getElementById("vessels").value,
      thallium: document.getElementById("thallium").value,
    };
  
    fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        const resultElement = document.getElementById("result");
        resultElement.innerHTML = data.prediction
          ? "The person has Heart Disease."
          : "The person does not have Heart Disease.";
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  