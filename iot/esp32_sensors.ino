#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";
const char* serverURL = "http://YOUR_PC_IP:5000/predict";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    float temperature = 28.5;
    float humidity = 65.0;
    float moisture = 42.0;
    float ph = 6.7;

    String json = "{";
    json += "\"temperature\":" + String(temperature) + ",";
    json += "\"humidity\":" + String(humidity) + ",";
    json += "\"moisture\":" + String(moisture) + ",";
    json += "\"ph\":" + String(ph);
    json += "}";

    http.begin(serverURL);
    http.addHeader("Content-Type", "application/json");
    http.POST(json);
    http.end();
  }

  delay(10000);
}
