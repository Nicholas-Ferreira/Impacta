package com.archeros.aula

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.login.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.login)

        btnLogin.setOnClickListener {
            val email = etEmail.text
            val password = etPassword.text


            tvResult.text = "E-mail: $email Senha: $password"
            Toast.makeText(applicationContext, "Salve", Toast.LENGTH_SHORT).show()
        }
    }
}