/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula11;

/**
 *
 * @author senai
 */
public class Bolsista extends Aluno {
    private double bolsa;
    
    public void renovarBolsa(){
        System.out.println("Renovando bolsa.");
    }

    @Override
    public void pagarMensalidade() {
        System.out.println("Pagando mensalidade de bolsista."); 
    }

    public double getBolsa() {
        return bolsa;
    }

    public void setBolsa(int bolsa) {
        this.bolsa = bolsa;
    }
    
}
