#include <Servo.h>


#define trigPin 13  //Trig Ultrasons (sortie)
#define echoPin 12  //Echo Ultrasons (entrée)


Servo Servobase;
Servo Servobase2;
Servo Servoseg1;
Servo Servoseg2;
Servo Servoseg3;
Servo Servorot;


int pos;
int positionaatteindre = 0;
int posbase = 0;
int posrot = 0;
int posseg1 = 0;
int posseg2 = 0;
int posseg3 = 0;
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
long duration, distance;



void setup()

{
    pinMode(trigPin, OUTPUT);  //Trig est une sortie
    pinMode(echoPin, INPUT);   //Echo est le retour, en entrée
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
    while ( cardispo < 4 )
    {
      cardispo = Serial.available();
    }
    char choseLue = Serial.read();
    char choseLue2 = Serial.read();
    char choseLue3 = Serial.read();
    char choseLue4 = Serial.read();
    positionaatteindre = (choseLue2 - 48)*100 + (choseLue3 - 48)*10 + (choseLue4 - 48);
	if (choseLue - 48 == 1)
	{
		positionaatteindre = -positionaatteindre;
	}
    Serial.println(positionaatteindre); 
    // Capteur ultrason
    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10); //Trig déclenché 10ms sur HIGH
    digitalWrite(trigPin, LOW);
    // Calcul de l'écho
    duration = pulseIn(echoPin, HIGH);
    // Distance proportionnelle à la durée de sortie
    distance = duration*340/(2*10000);  //Vitesse du son théorique
    Serial.println("ultrason");
    Serial.println(distance);
    anglerot = positionaatteindre;
       
       
       
       
    // angle pour la base
    Serial.println("base"); 
    cardispo = Serial.available();
    while ( cardispo < 4 )
    {
      cardispo = Serial.available();
    }
    choseLue = Serial.read();
    choseLue2 = Serial.read();
    choseLue3 = Serial.read();
    choseLue4 = Serial.read();
    positionaatteindre = (choseLue2 - 48)*100 + (choseLue3 - 48)*10 + (choseLue4 - 48);
	if (choseLue - 48 == 1)
	{
		positionaatteindre = -positionaatteindre;
	}
    Serial.println(positionaatteindre); 
    anglebase = positionaatteindre;
        

    // angle pour 1er segment
        Serial.println("seg1"); 
    cardispo = Serial.available();
    while ( cardispo < 4 )
    {
      cardispo = Serial.available();
    }
    choseLue = Serial.read();
    choseLue2 = Serial.read();
	choseLue3 = Serial.read();
	choseLue4 = Serial.read();
    positionaatteindre = (choseLue2 - 48)*100 + (choseLue3 - 48)*10 + (choseLue4 - 48);
	if (choseLue - 48 == 1)
	{
		positionaatteindre = -positionaatteindre;
	}
    Serial.println(positionaatteindre); 
    angleseg1 = positionaatteindre;
    

    // angle pour 2eme segment
        Serial.println("seg2"); 
    cardispo = Serial.available();
    while ( cardispo < 4 )
    {
      cardispo = Serial.available();
    }
    choseLue = Serial.read();
    choseLue2 = Serial.read();
	choseLue3 = Serial.read();
	choseLue4 = Serial.read();
    positionaatteindre = (choseLue2 - 48)*100 + (choseLue3 - 48)*10 + (choseLue4 - 48);
	if (choseLue - 48 == 1)
	{
		positionaatteindre = -positionaatteindre;
	}
    Serial.println(positionaatteindre); 
    angleseg2 = positionaatteindre;
    

    // angle pour troisieme segment
        Serial.println("seg3"); 
    cardispo = Serial.available();
    while ( cardispo < 4 )
    {
      cardispo = Serial.available();
    }
    choseLue = Serial.read();
    choseLue2 = Serial.read();
	choseLue3 = Serial.read();
	choseLue4 = Serial.read();
    positionaatteindre = (choseLue2 - 48)*100 + (choseLue3 - 48)*10 + (choseLue4 - 48);
	if (choseLue - 48 == 1)
	{
	positionaatteindre = -positionaatteindre;
	}
    Serial.println(positionaatteindre); 
    angleseg3 = positionaatteindre;
    

    

    //############################################################# DEPLACEMENT DU BRAS ############################################"

    

    // rotation primaire
    if (posrot < anglerot)
    {
      for(pos = posrot; pos <= anglerot; pos += 1)  
        {                                  
          Servorot.write(inirot + pos);        
          delay(15);                    
        } 
    }
    else
    {
     for(pos = posrot; pos >= anglerot; pos-=1)    
      {                                
        Servorot.write(inirot + pos);    
        delay(15);     
      } 
    }
    posrot = anglerot;
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

    if (posseg1 < angleseg1)
    {
      for(pos = posseg1; pos <= angleseg1; pos += 1)  
        {                                  
         Servoseg1.write(iniseg1 + pos);        
          delay(15);                    
        } 
    }
    else
    {
      for(pos = posseg1; pos >= angleseg1; pos-=1)    
      {                                
        Servoseg1.write(iniseg1 + pos);    
        delay(15);     
      } 
    }
    posseg1 = angleseg1;
    delay(500);
   

    //segment 2
    if (posseg2 < angleseg2)
    {
      for(pos = posseg2; pos <= angleseg2; pos += 1)  
        {                                  
          Servoseg2.write(iniseg2 + pos);        
          delay(15);                    
        } 
    }
    else
    {
      for(pos = posseg2; pos >= angleseg2; pos-=1)    
      {                                
        Servoseg2.write(iniseg2 + pos);    
        delay(15);     
      } 
    }
    posseg2 = angleseg2;
    delay(500);
    

    // seg3
    if (posseg3 < angleseg3)
    {
      for(pos = posseg3; pos <= angleseg3; pos += 1)  
        {                                  
          Servoseg3.write(iniseg3 + pos);        
          delay(15);                    
        } 
    }
    else
    {
      for(pos = posseg3; pos >= angleseg3; pos-=1)    
      {                                
        Servoseg3.write(iniseg3 + pos);    
        delay(15);     
      } 
    }
    posseg3 = angleseg3;
    delay(500);
   
}
