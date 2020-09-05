package com.archeros.aula

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.login.*

class MainActivity : DebugActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.login)

        btnLogin.setOnClickListener {
            val email = etEmail.text
            val password = etPassword.text

            var intent = Intent(this, DashboardActivity::class.java)
                .putExtra("user_email", email.toString());

            startActivity(intent)
        }
    }
}