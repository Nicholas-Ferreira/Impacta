package com.archeros.aula

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuInflater
import android.view.MenuItem
import android.widget.Toast
import kotlinx.android.synthetic.main.toolbar.*

class DashboardActivity : DebugActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dashboard)
        setSupportActionBar(toolbar_view)
        supportActionBar?.title = "Roadmap"
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.action_buscar -> Toast.makeText(applicationContext, "1", Toast.LENGTH_SHORT).show()
            R.id.action_atualizar -> Toast.makeText(applicationContext, "2", Toast.LENGTH_SHORT).show()
            R.id.action_config -> Toast.makeText(applicationContext, "3", Toast.LENGTH_SHORT).show()
            android.R.id.home -> {
                var intent = Intent(this, MainActivity::class.java)
                startActivity(intent)
                this.finish()
            }
        }
        return super.onOptionsItemSelected(item)
    }
}