#include <Servo.h>

Servo Servobase;
Servo Servobase2;
Servo Servoseg1;
Servo Servoseg2;
Servo Servoseg3;
Servo Servorot;



int pos;
int positionaatteindre = 0;
int posbase = 0;
int cardispo;
int anglerot;
int anglebase;
int angleseg1;
int angleseg2;
int angleseg3;

int inirot = 90;
int inibase = 90;
int iniseg1 = 90;
int iniseg2 = 0;
int iniseg3 = 90;




void setup()
{
    Serial.begin(9600);
    Servobase.attach(8);
    Servobase2.attach(9);
    Servorot.attach(7);
    Servoseg1.attach(2);
    Servoseg2.attach(3);
    Servoseg3.attach(4);
    Servobase.write(inibase);
    Servobase2.write(inibase);
    Servorot.write(inirot);
    Servoseg1.write(iniseg1);
    Servoseg2.write(iniseg2);
    Servoseg3.write(iniseg3);
    
    
    
}

void loop()
{
    // #####################################  COLLECTE D INFO #######################################################################"
    
    // angle pour la rotation
    Serial.println("rot"); 
    cardispo = Serial.available();
    while ( cardispo < 2 )
    {
      cardispo = Serial.available();
    }
    char choseLue = Serial.read();
    char choseLue2 = Serial.read();
    positionaatteindre = (choseLue - 48)*10 + (choseLue2 - 48);
    Serial.println(positionaatteindre); 
    anglerot = positionaatteindre;
    
    
    // angle pour la base
    Serial.println("base"); 
    cardispo = Serial.available();
    while ( cardispo < 2 )
    {
      cardispo = Serial.available();
    }
    choseLue = Serial.read();
    choseLue2 = Serial.read();
    positionaatteindre = (choseLue - 48)*10 + (choseLue2 - 48);
    Serial.println(positionaatteindre); 
    anglebase = positionaatteindre;
    
    
    // angle pour 1er segment
        Serial.println("seg1"); 
    cardispo = Serial.available();
    while ( cardispo < 2 )
    {
      cardispo = Serial.available();
    }
    choseLue = Serial.read();
    choseLue2 = Serial.read();
    positionaatteindre = (choseLue - 48)*10 + (choseLue2 - 48);
    Serial.println(positionaatteindre); 
    angleseg1 = positionaatteindre;
    
    // angle pour 2eme segment
        Serial.println("seg2"); 
    cardispo = Serial.available();
    while ( cardispo < 2 )
    {
      cardispo = Serial.available();
    }
    choseLue = Serial.read();
    choseLue2 = Serial.read();
    positionaatteindre = (choseLue - 48)*10 + (choseLue2 - 48);
    Serial.println(positionaatteindre); 
    angleseg2 = positionaatteindre;
    
    // angle pour troisieme segment
        Serial.println("seg3"); 
    cardispo = Serial.available();
    while ( cardispo < 2 )
    {
      cardispo = Serial.available();
    }
    choseLue = Serial.read();
    choseLue2 = Serial.read();
    positionaatteindre = (choseLue - 48)*10 + (choseLue2 - 48);
    Serial.println(positionaatteindre); 
    angleseg3 = positionaatteindre;
    
    
    //############################################################# DEPLACEMENT DU BRAS ############################################"
    
    // rotation primaire
    Servorot.write(inirot + anglerot);
    delay(500);
    
    // deplacement de la base
    if (posbase < anglebase)
    {
      for(pos = posbase; pos <= anglebase; pos += 1)  
        {                                  
          Servobase.write(inibase + pos);
          Servobase2.write(inibase - pos);          
          delay(15);                    
        } 
    }
    else
    {
      for(pos = posbase; pos >= anglebase; pos-=1)    
      {                                
        Servobase.write(inibase + pos);
        Servobase2.write(inibase - pos);    
        delay(15);     
      } 
    }
    posbase = anglebase;
    delay(500);
    
    
    // segment 1
    Servoseg1.write(iniseg1 - angleseg1);
    delay(500);
    
    //segment 2
    Servoseg2.write(iniseg2 + angleseg2);
    delay(500);
    
    // seg3
    Servoseg3.write(iniseg3 - angleseg3);
    delay(500);
    
}
