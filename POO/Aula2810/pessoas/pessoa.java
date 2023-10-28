package br.inf.mstech.pessoas;

import br.inf.mstech.Composicao.Endereco;
		
public class Pessoa {
	private String nome;
	private String dataNascimento;
	
	//Endereco Deixa de Ser STRING e passa a ser Classe
	//private String endereco;
	private Endereco endereco;
	
	
	
	private String telsContato;
	
	
	public Pessoa() {
	}
	
	//Metodo sempre vem acompanhado dos parenteses
	public void cadastrar(  String nome, String dataNascimento, Endereco endereco, String telsContato ) {
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

	// Anteriormente era um atributo agora passa a ser uma classe
	//public String getEndereco() {
	//	return endereco;
	//}
	
	public Endereco getEndereco() {
			return endereco;
		}
	
	
	public void setEndereco(Endereco endereco) {
		this.endereco = endereco;
	}

	public String getTelsContato() {
		return telsContato;
	}

	public void setTelsContato(String telsContato) {
		this.telsContato = telsContato;
	}
	
	
	
	
	
	
}