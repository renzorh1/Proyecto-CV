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
public class TipoFantasma extends Pokemon implements EvolucionXPiedra
{
    boolean piedra;

    public TipoFantasma(boolean piedra, String Nombre, int Nivel, String FechaDeAdqui, int PoderInicial) {
        super(Nombre, Nivel, FechaDeAdqui, PoderInicial);
        this.piedra = piedra;
    }
    


    @Override
    public void CalcularPoderMaximo() 
    {
     Random rand= new Random();
     this.PoderMax = rand.nextInt(2600-500+1)+500;
     this.PoderMax= this.PoderMax + this.PoderInicial;        
    }

    @Override
    public void VerificarSiEsShiny() 
    {
     Random rand= new Random();   
     this.Shiny = rand.nextInt(100-1+1)+1;
     if(this.Shiny>97)
     {
         JOptionPane.showMessageDialog(null,"EL POKEMON QUE INGRESÓ ES SHINY");
     }
     else
     {
         JOptionPane.showMessageDialog(null,"EL POKEMON QUE INGRESÓ NO ES SHINY");
     }
    }


    @Override
    public void EvolucionarEspecial()
    {
        if(this.PoderMax>=PoderRequerido && piedra == true)
        {
            this.AptoParaEvo=true;
        }
        else
        {
            this.AptoParaEvo=false;
        }        
    }   
}
