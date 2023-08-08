const location = "Washington";
const format = "json";

const requestBody = JSON.stringify([{ city: location, output_format: format }]);

console.log(requestBody);
fetch("http://localhost:8080/getCurrentWeather", {
  method: "POST",
  body: requestBody,
})
  .then((resp) => resp.json())
  .then((data) => console.log(data))
  .catch((err) => console.log(err));
