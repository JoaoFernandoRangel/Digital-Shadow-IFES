/*
      Programa para Leitura do sensor de Aceleração e Giroscópio MPU-6050
      Leitura feita via baramento I2C, impressão na Serial para ser vizualizada com o Serial Plotter do Arduino IDE

      Componentes:
        - Arduino (Qualquer placa);
        - Sensor MPU-6050 (Placa GY-521)

      Versão 1.0 - Versão inicial com leitura do sensor e impressão na serial - 07/Jan/2021

 *    * Criado por Cleber Borges - FunBots - @cleber.funbots  *     *

      Instagram: https://www.instagram.com/cleber.funbots/
      Facebook: https://www.facebook.com/cleber.funbots
      YouTube: https://www.youtube.com/channel/UCKs2l5weIqgJQxiLj0A6Atw
      Telegram: https://t.me/cleberfunbots

*/

// Inclusão das Bibliotecas
#include<Wire.h>
char begin = "<";
char end = ">";
// Endereco I2C do sensor MPU-6050
const int MPU = 0x68;

// Variaveis para armazenar valores do sensor
float AccX, AccY, AccZ, Temp, GyrX, GyrY, GyrZ;

//Teste zerar
float zeroX, zeroY, zeroZ; int k = 1;

void setup() {
  // Inicializa Serial
  Serial.begin(9600);

  // Inicializa o MPU-6050
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);

  // Configura Giroscópio para fundo de escala desejado
  /*
    Wire.write(0b00000000); // fundo de escala em +/-250°/s
    Wire.write(0b00001000); // fundo de escala em +/-500°/s
    Wire.write(0b00010000); // fundo de escala em +/-1000°/s
    Wire.write(0b00011000); // fundo de escala em +/-2000°/s
  */
  Wire.beginTransmission(MPU);
  Wire.write(0x1B);
  Wire.write(0b00001000);  // Trocar esse comando para fundo de escala desejado conforme acima
  Wire.endTransmission();

  // Configura Acelerometro para fundo de escala desejado
  /*
      Wire.write(0b00000000); // fundo de escala em +/-2g
      Wire.write(0b00001000); // fundo de escala em +/-4g
      Wire.write(0b00010000); // fundo de escala em +/-8g
      Wire.write(0b00011000); // fundo de escala em +/-16g
  */
  Wire.beginTransmission(MPU);
  Wire.write(0x1C);
  Wire.write(0b00001000);  // Trocar esse comando para fundo de escala desejado conforme acima
  Wire.endTransmission();  
  string LeitorSerial = "ping"
}

void loop() {
  int ciclos = serial.read()

  if (serial.read()) {
    for (int i=0; i < ciclos; i++){

      // Comandos para iniciar transmissão de dados
        Wire.beginTransmission(MPU);
        Wire.write(0x3B);
        Wire.endTransmission(false);
        Wire.requestFrom(MPU, 14, true); // Solicita os dados ao sensor

        // Armazena o valor dos sensores nas variaveis correspondentes
        AccX = Wire.read() << 8 | Wire.read(); //0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
        AccY = Wire.read() << 8 | Wire.read(); //0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
        AccZ = Wire.read() << 8 | Wire.read(); //0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
        Temp = Wire.read() << 8 | Wire.read(); //0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
        GyrX = Wire.read() << 8 | Wire.read(); //0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
        GyrY = Wire.read() << 8 | Wire.read(); //0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
        GyrZ = Wire.read() << 8 | Wire.read(); //0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

        // Imprime na Serial os valores obtidos
        /* Alterar divisão conforme fundo de escala escolhido:
            Acelerômetro
            +/-2g = 16384
            +/-4g = 8192
            +/-8g = 4096
            +/-16g = 2048

            Giroscópio
            +/-250°/s = 131
            +/-500°/s = 65.6
            +/-1000°/s = 32.8
            +/-2000°/s = 16.4
        */
        Serial.print(GyrX / 65.6);
        Serial.print(",");
        Serial.print(GyrY / 65.6);
        Serial.print(",");
        Serial.print(GyrZ / 65.6);
        Serial.print(",");
        Serial.print( AccX / 8192);
        Serial.print(",");
        Serial.print( AccY / 8192);
        Serial.print(",");
        Serial.println( AccZ / 8192);
      

        // Atraso de 100ms
        delay(10);
  
    }
  }
}