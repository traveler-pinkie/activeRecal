#include <stdbool.h>

bool validate_pin(const char *pin) {
  int length = 0;
  while(*pin != '\0'){
    if(*pin >= '0' && *pin <= '9'){
        length++;
        pin = pin + 1;
    }else{
        return false;
    }

  }
  if(length == 4 || length == 6){
    return true;
  }else{
    return false;
  }
}
