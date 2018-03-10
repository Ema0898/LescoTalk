package com.example.ema0898.lescotalk;

import android.content.Intent;
import android.os.Handler;
import android.speech.tts.TextToSpeech;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    public static TextToSpeech textToSpeech;
    int textToSpeechResult;

    boolean pressedTwice;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textToSpeech = new TextToSpeech(MainActivity.this, new TextToSpeech.OnInitListener() {
            @Override
            public void onInit(int i) {
                if (i == TextToSpeech.SUCCESS) {
                    textToSpeechResult = textToSpeech.setLanguage(Locale.getDefault());
                } else {
                    Toast.makeText(getApplicationContext(), R.string.textToSpeechInitError, Toast.LENGTH_SHORT).show();
                }

            }
        });

        Thread myThread = new Thread(new SocketThread2());
        myThread.start();
    }

    /*public String getIP() {
        ConnectivityManager cm = (ConnectivityManager) getApplicationContext().getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo activeNetwork = cm.getActiveNetworkInfo();
        WifiManager wm = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);

        WifiInfo connectionInfo = wm.getConnectionInfo();
        int ipAddress = connectionInfo.getIpAddress();
        String ipString = Formatter.formatIpAddress(ipAddress);

        return ipString;
    }*/

    @Override
    public void onBackPressed() {

        if (pressedTwice) {
            Intent intent = new Intent(Intent.ACTION_MAIN);
            intent.addCategory(Intent.CATEGORY_HOME);
            intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
            startActivity(intent);
            finish();
            System.exit(0);
        }

        pressedTwice = true;

        Toast.makeText(getApplicationContext(), R.string.exitMessage, Toast.LENGTH_SHORT).show();

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                pressedTwice = false;
            }
        }, 3000);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();

        if (textToSpeech != null) {
            textToSpeech.stop();
            textToSpeech.shutdown();
        }
    }
}

class SocketThread2 implements Runnable {

    Socket socket;
    ServerSocket serverSocket;
    InputStreamReader inputStreamReader;
    BufferedReader bufferedReader;

    String message;

    @Override
    public void run() {

        try {
            // IP CASA = "192.168.0.27"
            // IP TEC = "172.18.243.179"
            // IP APARTA = "192.168.100.28"

            socket = new Socket("192.168.100.28", 8081);
            Log.e("SOCKET_FLAG", "Socket Created");

            while (true) {
                inputStreamReader = new InputStreamReader(socket.getInputStream());
                bufferedReader = new BufferedReader(inputStreamReader);
                message = bufferedReader.readLine();
                Log.e("MSG", message);
                MainActivity.textToSpeech.speak(message, TextToSpeech.QUEUE_FLUSH, null);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

