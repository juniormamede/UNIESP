package br.inf.mstech.pessoas;

public class pessoa {
	private String nome;
	private String dataNascimento;
	private String endereco;
	private String telsContato;
	
	
	public pessoa() {
	}
	
	//Metodo sempre vem acompanhado dos parenteses
	public void cadastrar(  String nome, String dataNascimento, String endereco, String telsContato ) {
		this.nome = nome;
		this.dataNascimento = dataNascimento;
		this.endereco = endereco;
		this.telsContato = telsContato;
		
		
	}
	
	public int obterIdade() {
		int idade = 0;
		//Subtrair Ano Atual da Data de Nascimento informanda
		return idade;
	}

	
	// SOURCE -> GENERATE GETTERS AND SETTERS
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getDataNascimento() {
		return dataNascimento;
	}

	public void setDataNascimento(String dataNascimento) {
		this.dataNascimento = dataNascimento;
	}

	public String getEndereco() {
		return endereco;
	}

	public void setEndereco(String endereco) {
		this.endereco = endereco;
	}

	public String getTelsContato() {
		return telsContato;
	}

	public void setTelsContato(String telsContato) {
		this.telsContato = telsContato;
	}
	
	
	
	
	
	
}