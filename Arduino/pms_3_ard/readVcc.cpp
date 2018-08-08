
#include "Arduino.h"
#define VCC_CALIBRATION 1088050L        //  1100 mv * 1023 this value is obtained by real measurment in the lab
                                        //  vcc = (1100 * 1023) / result;

long readVcc() {
  long result;
  long vcc;
  
  ADMUX = _BV(REFS0) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);

  delay(2);                                        // Wait for Vref to settle
  ADCSRA |= _BV(ADSC);                             // Convert
  while (bit_is_set(ADCSRA,ADSC));
  result = ADCL;
  result |= ADCH<<8;
  vcc = VCC_CALIBRATION / result;                  
  return vcc;
}

