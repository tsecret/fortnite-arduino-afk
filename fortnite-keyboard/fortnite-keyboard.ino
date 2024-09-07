#include <Keyboard.h>

void setup() {
  Keyboard.begin();
}

void loop() {
  jumpAround();
  afk();

  emote();
  afk();

  hold('w');
  hold('s');
  hold('a');
  hold('d');
  afk();
}

void press(char button){
  Keyboard.press(button);
  delay(100);
  Keyboard.release(button);
}

void hold(char button){
  Keyboard.press(button);
  delay(random(2000, 5000));
  Keyboard.release(button);
}

void jumpAround(){
  for (int i=1; i <= random(2, 5); i++){
    press(' ');
    delay(random(500, 1000));
  }
}

void emote(){
  press('b');
}

void afk(){
  delay(random(10000, 120000));
}