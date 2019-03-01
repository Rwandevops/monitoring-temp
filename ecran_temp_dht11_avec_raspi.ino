/* ILI9225 Driver */
/* https://github.com/Nkawu/TFT_22_ILI9225 */


// Include application, user and local libraries
#include "SPI.h"
#include "TFT_22_ILI9225.h"
#include <dht.h>
#include <Wire.h>

dht DHT;

#define TFT_RST 8
#define TFT_RS  9
#define TFT_CS  10  // SS
#define TFT_SDI 11  // MOSI
#define TFT_CLK 13  // SCK
#define TFT_LED 3   // 0 if wired to +5V directly

#define DHT11_PIN 7

#define SLAVE_ADDRESS 0x12


/*
Hardware hookup

LCD Pin                 Arduino Pin
-------                 -----------
 1  Vcc                 Vcc
 2  Gnd                 Gnd
 3  Gnd                 Gnd or N/C
 4                      N/C
 5                      N/C
 6  LED (backlight)     D3
 7  CLK                 D13 (SCK)
 8  SDI                 D11 (MOSI)
 9  RS                  D9
10  RST                 D8
11  CS                  D10
*/

// Use hardware SPI (faster - on Uno: 13-SCK, 12-MISO, 11-MOSI)
TFT_22_ILI9225 tft = TFT_22_ILI9225(TFT_RST, TFT_RS, TFT_CS, TFT_LED);
// Use software SPI (slower)
//TFT_22_ILI9225 tft = TFT_22_ILI9225(TFT_RST, TFT_RS, TFT_CS, TFT_SDI, TFT_CLK, TFT_LED);

// Variables and constants
uint16_t x, y;
boolean flag = false;
int dataReceived = 0;

// Setup
void setup() {
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  tft.begin();
  Serial.begin(9600);
}

// Loop
void loop() {
    
// lecture du DHT11
  int chk = DHT.read11(DHT11_PIN);
// affichage de la température sur le port série
  Serial.println(DHT.temperature);
  int temp = DHT.temperature;
// conversion de chk en chaine de caractères
  String Temp=String(temp);

// écriture sur l'écran ILI9225
  tft.setFont(Terminal12x16); // définition de la police
  tft.setBackgroundColor(COLOR_BLACK); // définition du fond d'écran
  
  tft.drawText(40, 30, "Bonjour,", COLOR_YELLOW); 
  tft.drawText(40, 80, "il fait", COLOR_YELLOW);
  tft.drawText(30, 130, Temp, COLOR_GREEN);
  tft.drawText(80, 130, "degres", COLOR_GREEN);

  delay(900);
}
 void receiveData(int byteCount){
   while(Wire.available()) {
       dataReceived = Wire.read();
       Serial.print("Temperature : ");
       Serial.println(dataReceived);
   }
}

void sendData(){
   int temp = DHT.temperature;
   Wire.write(temp);
}
