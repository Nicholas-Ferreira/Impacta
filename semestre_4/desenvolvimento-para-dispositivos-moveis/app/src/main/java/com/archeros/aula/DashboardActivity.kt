package com.archeros.aula

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast

class DashboardActivity : DebugActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dashboard)

        val args = intent.extras
        val email = args?.getString("user_email")

        Toast.makeText(applicationContext, "$email", Toast.LENGTH_SHORT).show()
    }
}