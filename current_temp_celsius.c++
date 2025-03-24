#include "Particle.h"


double current_temp;
unsigned long lastCheck=0;
// unsigned long currentTime = System.millis();

void setup() {
    Particle.variable("current_temperature_celsius", current_temp);
}

void loop() {
    unsigned long currentMillis = millis();
    
    if(currentMillis-lastCheck >1000){
        lastCheck = currentMillis;
        current_temp = random(20,31);
        
    }
 }