package aula12;

public abstract class Animal {
    protected double peso;
    protected int idade;
    protected int membros;
    
    public abstract void locomover();
    public abstract void alimentar();
    public abstract void emitirSom();

    public abstract double getPeso();
    
    public abstract void setPeso(double peso);

    public abstract int getIdade();

    public abstract void setIdade(int idade);

    public abstract int getMembros();

    public abstract void setMembros(int membros);
    
    
}
