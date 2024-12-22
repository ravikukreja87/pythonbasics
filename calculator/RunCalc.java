package calculator;

public class RunCalc {

	public static void main(String[] args) {
		
		
		Calculator add = new Calculator();
		add.firstNumber = 10;
		add.secondNumber = 5;
		add.operation = "+";
		add.addition();
		
		add.showResult();
		
		Calculator addAnother = new Calculator();
		addAnother.firstNumber = 20;
		addAnother.secondNumber = 10;
		addAnother.operation = "+";
		addAnother.addition();
		addAnother.showResult();
		
		
	}
}
