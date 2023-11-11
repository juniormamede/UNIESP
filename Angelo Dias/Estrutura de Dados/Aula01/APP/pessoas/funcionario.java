package br.inf.mstech.pessoas;

public class Funcionario extends Pessoa {
	private int matricula;
	private String cargo;
	private double salario;
	private String dataAdmissao;
	
	public void reajusteSalario(double percentual) {
		this.salario = this.salario * percentual;
	}
	
	public void promover(String novoCargo) { 
		this.cargo = novoCargo;
	}

	public int getMatricula() {
		return matricula;
	}

	public void setMatricula(int matricula) {
		this.matricula = matricula;
	}

	public String getDataAdmissao() {
		return dataAdmissao;
	}

	public void setDataAdmissao(String dataAdmissao) {
		this.dataAdmissao = dataAdmissao;
	}

	public String getCargo() {
		return cargo;
	}

	public double getSalario() {
		return salario;
	}
    
	public void cadastrar( int matricula, String cargo, double salario, String dataAdmissao, String nome, String dataNascimento, String endereco, String telsContato  ) {
		this.cargo = cargo;
		this.dataAdmissao = dataAdmissao;
		this.matricula = matricula;
		this.salario = salario;
		setDataNascimento(dataNascimento);
		setEndereco(getEndereco());
		setNome(nome);
		setTelsContato(telsContato);
	}
	
	
	
}
