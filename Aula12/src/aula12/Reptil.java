package aula12;

public class Reptil extends Animal {
    private String corEscama;

    @Override
    public void locomover() {
        System.out.println("Rastejando");
    }

    @Override
    public void alimentar() {
        System.out.println("Comendo Vegetais");
    }

    @Override
    public void emitirSom() {
        System.out.println("Som de reptil");
    }

    @Override
    public double getPeso() {
        return this.peso;
    }

    @Override
    public void setPeso(double peso) {
        this.peso = peso;
    }

    @Override
    public int getIdade() {
        return this.idade;
    }

    @Override
    public void setIdade(int idade) {
        this.idade = idade;
    }

    @Override
    public int getMembros() {
        return this.membros;
    }

    @Override
    public void setMembros(int membros) {
        this.membros = membros;
    }
    
}
