package com.archeros.aula

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Toast
import com.github.kittinunf.fuel.Fuel
import com.github.kittinunf.fuel.json.responseJson
import kotlinx.android.synthetic.main.activity_login.*

class MainActivity : DebugActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        btnLogin.setOnClickListener {
            val ra = etRA.text.toString()
            val password = etPassword.text.toString()

            btnLoginLoading.visibility = View.VISIBLE
            btnLogin.text = ""
            onLogin(ra, password) {
                btnLoginLoading.visibility = View.INVISIBLE
                btnLogin.text = getString(R.string.btn_login)

                if(it){
                    var intent = Intent(this, DashboardActivity::class.java)
                    startActivity(intent)
                    this.finish()
                }
            }
        }
    }


    fun onLogin(ra: String, password: String, callback: (result: Boolean) -> Unit) {
        val url = "https://account.impacta.edu.br/account/enter.php"
        val params = listOf("desidentificacao" to ra, "dessenha" to password)

        Fuel.post(url, params)
            .responseJson { request, response, result ->
                result.fold(success = { json ->
                    if(json.obj().get("success") == true) {
                        callback(true)
                    }else{
                        Toast.makeText(applicationContext, "Login ou senha inválidos, tente novamente.", Toast.LENGTH_SHORT).show()
                        callback(false)
                    }
                    btnLoginLoading.visibility = View.INVISIBLE
                }, failure = { error ->
                    Toast.makeText(applicationContext, "Erro inesperado", Toast.LENGTH_SHORT).show()
                    Log.i("RequestResult", error.toString())
                    callback(false)
                })
            }
    }
}