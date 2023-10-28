package br.inf.mstech.appMain;

//import br.inf.mstech.pessoas.cliente;
//import br.inf.mstech.pessoas.funcionario;
//import br.inf.mstech.pessoas.pessoa;

//Como vamos usar tudo, seguir orientacao abaixo
import br.inf.mstech.pessoas.*;

public class AplicacaoMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        
	    Funcionario objFuncionario = new Funcionario();
	    Cliente objCliente         = new Cliente();
	    
	    
	    
	    
	    objFuncionario.cadastrar(0001, "Analista", 5000, "02/01/2019", "Mamede", "20/06/2023", "Melvin Jones", "83996858655");
	    
	    objCliente.cadastrar("C001", "DESENVOLVEDOR SENIO", "ANGELO", "18/09/1986", "UNIESP", "839987159753");
	    
	}

}
