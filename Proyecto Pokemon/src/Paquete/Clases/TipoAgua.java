/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Paquete.Clases;

import java.util.Random;
import javax.swing.JOptionPane;

/**
 *
 * @author L34119
 */
public class TipoAgua extends Pokemon implements EvolucionXNivel
{

    public TipoAgua(String Nombre, int Nivel, String FechaDeAdqui, int PoderInicial) {
        super(Nombre, Nivel, FechaDeAdqui, PoderInicial);
    }

    @Override
    public void CalcularPoderMaximo() 
    {
     Random rand= new Random();
     this.PoderMax = rand.nextInt(1800-900+1)+900;
     this.PoderMax= this.PoderMax + this.PoderInicial;       
        
    }

    @Override
    public void VerificarSiEsShiny()
    {
     Random rand= new Random();   
     this.Shiny = rand.nextInt(100-1+1)+1;
     if(this.Shiny>92)
     {
         JOptionPane.showMessageDialog(null,"EL POKEMON QUE TIENE ES SHINY");
     }
     else
     {
         JOptionPane.showMessageDialog(null,"EL POKEMON QUE TIENE NO ES SHINY");
     }    
        
    }

    @Override
    public void EvolucionarElemen() 
    {
        if (this.Nivel>NivelMin)
        {
            this.AptoParaEvo=true;
        }
        else
        {
            this.AptoParaEvo=false;
        }        
    }
    
}
