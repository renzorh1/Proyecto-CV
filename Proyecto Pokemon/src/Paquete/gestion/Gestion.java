/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Paquete.gestion;

import Paquete.Clases.Pokemon;
import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 *
 * @author renzo
 */
public class Gestion 
{
    ArrayList<String> Pokebolas;
    private Pokemon[] arreglo;
    private int puntero;

    public Gestion() 
    {
        Pokebolas = new ArrayList<String>();
        arreglo = new Pokemon[10];
        puntero=0;        
    }

    public Pokemon[] getArreglo() {
        return arreglo;
    }

    public void setArreglo(Pokemon[] arreglo) {
        this.arreglo = arreglo;
    }

    public int getPuntero() {
        return puntero;
    }

    public void setPuntero(int puntero) {
        this.puntero = puntero;
    }
    
    
    public void Ingresar(Pokemon ref)
    {
        if(puntero<arreglo.length)
        {
            arreglo[puntero]=ref;
            puntero++;
        }
        
    }
       
    /*public void Eliminar(String Nombre)
    {
        for(int i=0;i<puntero;i++)
        {
            if(arreglo[i].getNombre().equalsIgnoreCase(Nombre))
            {
                for(int j=i;j<puntero-1;j++)
                {
                    arreglo[j]=arreglo[j+1];
                }
                arreglo[puntero-1]=null;
                puntero--;
            }
        }
    }*/
    public void Eliminar(int Pos)
    {
        for(int i=0;i<puntero;i++)
        {
            if(i==Pos)
            {
                for(int j=i;j<puntero-1;j++)
                {
                    arreglo[j]=arreglo[j+1];
                }
                arreglo[puntero-1]=null;
                puntero--;
            }
        }
    }
    public void EvolucionarPokemon(String Nombre, String NombreEvo)
    {
        try{
        int a = 0;
        for(int i=0;i<puntero;i++)
        {
        
            if(arreglo[i].getNombre().equalsIgnoreCase(Nombre))
            {   if(arreglo[i].isAptoParaEvo()==true)
                {
                JOptionPane.showMessageDialog(null, "FELICIDADES, su pokémon ha evolucionado");
                arreglo[i].setNombre(NombreEvo);
                arreglo[i].setNivel(1);
                arreglo[i].setPoderMax(500);
                arreglo[i].setAptoParaEvo(false);
                a++;
                break;
                }
                if(arreglo[i].isAptoParaEvo()==false)
                {
                JOptionPane.showMessageDialog(null, "Su pokémon no es apto para evolucionar :(");
                a++;
                }
            }
            
            }
        if(a==0){
            JOptionPane.showMessageDialog(null, "Qué extraño pokémon, no está en tus registros");
        }
        }
        catch(Exception e){
              JOptionPane.showMessageDialog(null, "Ops, ocurrió un error, inténtelo denuevo"+e.getMessage());
          }
        
    }
    
    public void BuscarMayorPoder()
    {
        int auxPoderMayor = arreglo[0].getPoderMax();
        for(int i=0; i<puntero;i++)
        {
            if(arreglo[i].getPoderMax()>auxPoderMayor)
            {
                auxPoderMayor = arreglo[i].getPoderMax();
            }
        }
        
        for(int i=0;i<puntero;i++)
        {
            if(arreglo[i].getPoderMax()==auxPoderMayor)
            {
                JOptionPane.showMessageDialog(null, "El Pokémon con mayor poder es "+ arreglo[i].getNombre()+" con un total de: "+auxPoderMayor);
            }
        }
    }
    public void VerPokebolas()
    {
        Pokebolas.add("Pokebola Roja");
        Pokebolas.add("Pokebola Azul");
        for(int i=0; i<Pokebolas.size();i++)
        {
            JOptionPane.showMessageDialog(null,"cuenta con: "+Pokebolas.get(i));
        }
    }


        
    
    
    
    
    
}
