package com.archeros.aula

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import com.github.kittinunf.fuel.Fuel
import com.github.kittinunf.fuel.core.Method
import com.github.kittinunf.fuel.httpGet
import com.github.kittinunf.fuel.json.responseJson
import com.github.kittinunf.result.Result;
import kotlinx.android.synthetic.main.login.*

class MainActivity : DebugActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.login)

        btnLogin.setOnClickListener {
            val ra = etRA.text.toString()
            val password = etPassword.text.toString()

            onLogin(ra, password) {
                var intent = Intent(this, DashboardActivity::class.java)
                startActivity(intent)
                this.finish()
            }
        }
    }


    fun onLogin(ra: String, password: String, callback: () -> Unit) {
        val url = "https://account.impacta.edu.br/account/enter.php"
        val params = listOf("desidentificacao" to ra, "dessenha" to password)

        Fuel.post(url, params)
            .responseJson { request, response, result ->
                result.fold(success = { json ->
                    if(json.obj().get("success") == true) {
                        callback()
                    }else{
                        Toast.makeText(applicationContext, "Login ou senha inválidos, tente novamente.", Toast.LENGTH_SHORT).show()
                    }
                }, failure = { error ->
                    Log.i("RequestResult", error.toString())
                })
            }
    }
}