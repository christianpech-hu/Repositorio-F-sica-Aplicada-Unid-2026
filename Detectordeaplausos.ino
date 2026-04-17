const int sensorPin = 2;

int leds[] = {3, 4, 5, 6, 7, 9};
const int numLeds = 6;

bool estado = false;
bool modoArcade = false;

int lecturaAnterior = HIGH;

unsigned long tiempoUltimoAplauso = 0;
unsigned long tiempoPrimerAplauso = 0;

// 🔥 MÁXIMA sensibilidad
const int debounce = 80;        // MUY bajo
const int ventanaDoble = 400;   // más rápida respuesta

int contadorAplausos = 0;

// 🎮 Arcade
int ledActual = 0;
int direccion = 1;

unsigned long tiempoAnterior = 0;
const int velocidad = 60;

void setup() {
  pinMode(sensorPin, INPUT);

  for (int i = 0; i < numLeds; i++) {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
}

void loop() {
  int lectura = digitalRead(sensorPin);

  // 🔥 DETECCIÓN ULTRA SENSIBLE
  if (lectura == LOW && lecturaAnterior == HIGH) {
    unsigned long tiempoActual = millis();

    if (tiempoActual - tiempoUltimoAplauso > debounce) {

      contadorAplausos++;
      Serial.println("Aplauso MAX");

      if (contadorAplausos == 1) {
        tiempoPrimerAplauso = tiempoActual;
      }

      tiempoUltimoAplauso = tiempoActual;
    }
  }

  lecturaAnterior = lectura;

  // Evaluar aplausos
  if (contadorAplausos > 0 && millis() - tiempoPrimerAplauso > ventanaDoble) {

    if (contadorAplausos == 1) {
      modoArcade = false;
      estado = !estado;

      for (int i = 0; i < numLeds; i++) {
        digitalWrite(leds[i], estado ? HIGH : LOW);
      }
    }

    else if (contadorAplausos >= 2) {
      if (!modoArcade) {
        modoArcade = true;
        ledActual = 0;
        direccion = 1;
      } else {
        modoArcade = false;
        estado = false;

        for (int i = 0; i < numLeds; i++) {
          digitalWrite(leds[i], LOW);
        }
      }
    }

    contadorAplausos = 0;
  }

  // 🎮 ARCADE
  if (modoArcade) {
    if (millis() - tiempoAnterior > velocidad) {
      tiempoAnterior = millis();

      for (int i = 0; i < numLeds; i++) {
        digitalWrite(leds[i], LOW);
      }

      digitalWrite(leds[ledActual], HIGH);

      ledActual += direccion;

      if (ledActual == numLeds - 1 || ledActual == 0) {
        direccion = -direccion;
      }
    }
  }
}