// spoof serial messages for CAN-less serial testing

#define SER_BAUD 115200

void setup()
{
    Serial.begin(SER_BAUD);
    Serial.println("Program Start");
    delay(5);
}


void loop()
{
    const char canId[] = "90";  
  
    const char *msgs[6];
    msgs[0] = "01\t55\t40\t35\t60\t00\t00\t22";
    msgs[1] = "01\t65\t40\t3A\t61\t01\t01\t11";
    msgs[2] = "01\t75\t41\t3F\t62\t02\t0A\t32";
    msgs[3] = "01\t85\t41\t40\t63\t03\t00\tBE";
    msgs[4] = "01\t95\t45\t45\t64\t04\t00\tA1";
    msgs[5] = "01\tA5\t45\t4A\t65\t05\t00\tA2";

    for(int i = 0; i<6; i++)    // print the data
    {
        Serial.print("0x");
        Serial.println(canId);
        Serial.println(msgs[i]);
    }
    Serial.println();
    
    delay(500);
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
