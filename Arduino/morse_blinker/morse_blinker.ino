
String myString = "sleep";
int string_len = 5;
char lettersArray [5];
int leter_delay = 1000;

void dot(){
  digitalWrite(A7,HIGH);
  delay(200);
  digitalWrite(A7,LOW);
  delay(200);
  }

void dash(){
  digitalWrite(A7,HIGH);
  delay(600);
  digitalWrite(A7,LOW);
  delay(200);
}

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(A7, OUTPUT);
  myString.toCharArray(lettersArray, myString.length() + 1);
}

// the loop function runs over and over again forever
void loop() {
  morse_out();
  delay(2000);
}

void morse_out(){
    for (int i = 0; i < string_len; i++){
      Serial.print(lettersArray[i]);
      switch (lettersArray[i]) {
        case 'a':
          dot();
          dash();
          delay(leter_delay);
          break;
        case 'b':
          dash();
          dot();
          dot();
          dot();
          delay(leter_delay);
          break;
        case 'c':
          dash();
          dot();
          dash();
          dot();
          delay(leter_delay);
          break;
        case 'd':
          dash();
          dot();
          dot();
          delay(leter_delay);
          break;
        case 'e':
          dot();
          delay(leter_delay);
          break;
        case 'f':
          dot();
          dot();
          dash();
          dot();
          delay(leter_delay);
          break;
        case 'g':
          dash();
          dash();
          dot();
          delay(leter_delay);
          break;
        case 'h':
          dot();
          dot();
          dot();
          dot();
          delay(leter_delay);
          break;
        case 'i':
          dot();
          dot();
          delay(leter_delay);
          break;
        case 'j':
          dot();
          dash();
          dash();
          dash();
          delay(leter_delay);
          break;
        case 'k':
          dash();
          dot();
          dash();
          delay(leter_delay);
          break;
        case 'l':
          dot();
          dash();
          dot();
          dot();
          delay(leter_delay);
          break;
        case 'm':
          dash();
          dash();
          delay(leter_delay);
          break;
        case 'n':
          dash();
          dot();
          delay(leter_delay);
          break;
        case 'o':
          dash();
          dash();
          dash();
          delay(leter_delay);
          break;
        case 'p':
          dot();
          dash();
          dash();
          dot();
          delay(leter_delay);
          break;
        case 'q':
          dash();
          dash();
          dot();
          dash();
          delay(leter_delay);
          break;
        case 'r':
          dot();
          dash();
          dot();
          delay(leter_delay);
          break;
        case 's':
          dot();
          dot();
          dot();
          delay(leter_delay);
          break;
        case 't':
          dash();
          delay(leter_delay);
          break;
        case 'u':
          dot();
          dot();
          dash();
          delay(leter_delay);
          break;
        case 'v':
          dot();
          dot();
          dot();
          dash();
          delay(leter_delay);
          break;
        case 'w':
          dot();
          dash();
          dash();
          delay(leter_delay);
          break;
        case 'x':
          dash();
          dot();
          dot();
          dash();
          delay(leter_delay);
          break;
        case 'y':
          dash();
          dot();
          dash();
          dash();
          delay(leter_delay);
          break;
        case 'z':
          dash();
          dash();
          dot();
          dot();
          delay(leter_delay);
          break;
        case ' ':
          delay(leter_delay);
          delay(leter_delay);
          break;
        case '?':
          dot();
          dot();
          dash();
          dash();
          dot();
          dot();
          delay(leter_delay);
          break;
        default:
          // Handle any other cases if needed
          break;
      } 
    Serial.println(" ");
    }
}
