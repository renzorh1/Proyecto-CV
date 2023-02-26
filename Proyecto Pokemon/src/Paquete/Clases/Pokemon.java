    /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Paquete.Clases;

/**
 *
 * @author L34119
 */
public abstract class Pokemon 
{
    protected String Nombre;
    protected int Nivel;
    protected String FechaDeAdqui;
    protected int PoderInicial;
    protected int PoderMax;
    protected boolean AptoParaEvo;
    protected int Shiny;   

    public Pokemon(String Nombre, int Nivel, String FechaDeAdqui, int PoderInicial) {
        this.Nombre = Nombre;
        this.Nivel = Nivel;
        this.FechaDeAdqui = FechaDeAdqui;
        this.PoderInicial = PoderInicial;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public int getNivel() {
        return Nivel;
    }

    public void setNivel(int Nivel) {
        this.Nivel = Nivel;
    }

    public String getFechaDeAdqui() {
        return FechaDeAdqui;
    }

    public void setFechaDeAdqui(String FechaDeAdqui) {
        this.FechaDeAdqui = FechaDeAdqui;
    }

    public int getPoderInicial() {
        return PoderInicial;
    }

    public void setPoderInicial(int PoderInicial) {
        this.PoderInicial = PoderInicial;
    }

    public int getPoderMax() {
        return PoderMax;
    }

    public void setPoderMax(int PoderMax) {
        this.PoderMax = PoderMax;
    }

    public boolean isAptoParaEvo() {
        return AptoParaEvo;
    }

    public void setAptoParaEvo(boolean AptoParaEvo) {
        this.AptoParaEvo = AptoParaEvo;
    }

    public int getShiny() {
        return Shiny;
    }

    public void setShiny(int Shiny) {
        this.Shiny = Shiny;
    }
    
    
public abstract void  CalcularPoderMaximo();    
public abstract void  VerificarSiEsShiny();

    
    
}
