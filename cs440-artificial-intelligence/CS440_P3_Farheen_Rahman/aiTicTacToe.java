import java.util.*;
public class aiTicTacToe {

	public int player; //1 for player 1 and 2 for player 2
	private positionTicTacToe myNextMove;
	private List<List<positionTicTacToe>> winningLines = initializeWinningLines();
	private int getStateOfPositionFromBoard(positionTicTacToe position, List<positionTicTacToe> board)
	{
		//a helper function to get state of a certain position in the Tic-Tac-Toe board by given position TicTacToe
		int index = position.x*16+position.y*4+position.z;
		return board.get(index).state;
	}
	public positionTicTacToe myAIAlgorithm(List<positionTicTacToe> board, int player)
	{
		//TODO: this is where you are going to implement your AI algorithm to win the game. The default is an AI randomly choose any available move.
		minimax(board, 4, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY, 1);
		return myNextMove;

	}

//Finds the best next move for the inputted player based on the inputted board
private int minimax(List<positionTicTacToe> board, int depth, double alpha, double beta, int player) {
	//When depth is 0, do the static evaluation
		if (depth == 0) {
			return heuristicScore(board, player, depth);
		}
		// Player 1 is our maximizing player
		if(player == 1) {
			//set initial value to negative infinity 
			double maxEval = Double.NEGATIVE_INFINITY;
			for(int i = 0; i<board.size();i++){
				if(getStateOfPositionFromBoard(board.get(i), board) != 0) continue;
				//create a copy of the board to use for recursion
				List<positionTicTacToe> newBoard = deepCopyATicTacToeBoard(board);
				//perform recursion on opposite player
				if(player==1) {
					makeMove(newBoard, newBoard.get(i), 1);}
				else {
					makeMove(newBoard, newBoard.get(i), 2);}
				//recursively call minimax on the opposing player until depth reached is 0
				int eval = minimax(newBoard, depth-1, alpha, beta, 2);
				//if the number returned is greater than -inf, then set the next position on the game board
				if(eval>maxEval) {
					myNextMove = new positionTicTacToe(board.get(i).x, board.get(i).y, board.get(i).z);}
				//between the resulting value and -inf, find the max
				maxEval = Math.max(maxEval, eval);
				//the new alpha will be updated the current alpha value and the resulting value
				alpha = Math.max(alpha, eval);
				// this is where we prune, because we choose not to evaluate further
				if(beta <= alpha) {break;}
			}
			//return the score of this branch
			return (int)maxEval;
		} else {
			double minEval = Double.POSITIVE_INFINITY;
			for(int i = 0; i<board.size();i++){
				if(getStateOfPositionFromBoard(board.get(i), board) != 0) continue;
				//create a copy of the board to use for recursion
				List<positionTicTacToe> newBoard = deepCopyATicTacToeBoard(board);
				//perform recursion on opposite player
				if(player==1) {
					makeMove(newBoard, newBoard.get(i), 2);}
				else {
					makeMove(newBoard, newBoard.get(i), 1);}
				//resursively call minimax on opposing player until depth reached is 0
				int eval = minimax(newBoard, depth-1, alpha, beta, 1);
				//if the number returned is less than +inf, then set the next position on the game board
				if(eval<minEval) {
					myNextMove = new positionTicTacToe(board.get(i).x, board.get(i).y, board.get(i).z); }
				//between the resulting value and +inf, find the min
				minEval = Math.min(minEval, eval);
				//the new beta will be updated between the current alpha value and the resulting value
				beta = Math.min(beta, eval);
				// this is where we prune, because we choose not to evaluate further
				if(beta <= alpha) {break;}
				myNextMove = myAIAlgorithmRand(board, 1);
		}
		//return the score of the branch
		return (int) minEval;}
}

public positionTicTacToe myAIAlgorithmRand(List<positionTicTacToe> board, int player) {
	do {
		Random rand = new Random();
		int x = rand.nextInt(4);
		int y = rand.nextInt(4);
		int z = rand.nextInt(4);
		myNextMove = new positionTicTacToe(x,y,z);
	}while(getStateOfPositionFromBoard(myNextMove,board)!=0);
	return myNextMove;
}

//creates a copy of the board, was given (used in minimax)
private static List<positionTicTacToe> deepCopyATicTacToeBoard(List<positionTicTacToe> board)
{
	List<positionTicTacToe> copiedBoard = new ArrayList<positionTicTacToe>();
	for(int i=0;i<board.size();i++){
		copiedBoard.add(new positionTicTacToe(board.get(i).x,board.get(i).y,board.get(i).z,board.get(i).state)); }
	return copiedBoard;
}

//Changes the state of the board based on the player inputted at the position inputted
public void makeMove(List<positionTicTacToe> board, positionTicTacToe position, int player)
{
	for(int i=0;i<board.size();i++){
		if(board.get(i).x==position.x && board.get(i).y==position.y && board.get(i).z==position.z){
			board.get(i).state = player; }
	}
}

//Returns a score for the given board and player
public int heuristicScore(List<positionTicTacToe> board, int player, int depth) {
	for (List<positionTicTacToe> line: winningLines) {
		for(positionTicTacToe winningPosition: line) {
			//Checks for when there is a winning state for each player and returns a score based on that
			int state = getStateOfPositionFromBoard(winningPosition, board);
			if(state==1) {return 10 - depth;}
			else if(state == 2){return -10 + depth;}
		}
	}
	return 0;
}



	private List<List<positionTicTacToe>> initializeWinningLines()
	{
		//create a list of winning line so that the game will "brute-force" check if a player satisfied any 	winning condition(s).
		List<List<positionTicTacToe>> winningLines = new ArrayList<List<positionTicTacToe>>();

		//48 straight winning lines
		//z axis winning lines
		for(int i = 0; i<4; i++)
			for(int j = 0; j<4;j++)
			{
				List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
				oneWinCondtion.add(new positionTicTacToe(i,j,0,-1));
				oneWinCondtion.add(new positionTicTacToe(i,j,1,-1));
				oneWinCondtion.add(new positionTicTacToe(i,j,2,-1));
				oneWinCondtion.add(new positionTicTacToe(i,j,3,-1));
				winningLines.add(oneWinCondtion);
			}
		//y axis winning lines
		for(int i = 0; i<4; i++)
			for(int j = 0; j<4;j++)
			{
				List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
				oneWinCondtion.add(new positionTicTacToe(i,0,j,-1));
				oneWinCondtion.add(new positionTicTacToe(i,1,j,-1));
				oneWinCondtion.add(new positionTicTacToe(i,2,j,-1));
				oneWinCondtion.add(new positionTicTacToe(i,3,j,-1));
				winningLines.add(oneWinCondtion);
			}
		//x axis winning lines
		for(int i = 0; i<4; i++)
			for(int j = 0; j<4;j++)
			{
				List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
				oneWinCondtion.add(new positionTicTacToe(0,i,j,-1));
				oneWinCondtion.add(new positionTicTacToe(1,i,j,-1));
				oneWinCondtion.add(new positionTicTacToe(2,i,j,-1));
				oneWinCondtion.add(new positionTicTacToe(3,i,j,-1));
				winningLines.add(oneWinCondtion);
			}

		//12 main diagonal winning lines
		//xz plane-4
		for(int i = 0; i<4; i++)
			{
				List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
				oneWinCondtion.add(new positionTicTacToe(0,i,0,-1));
				oneWinCondtion.add(new positionTicTacToe(1,i,1,-1));
				oneWinCondtion.add(new positionTicTacToe(2,i,2,-1));
				oneWinCondtion.add(new positionTicTacToe(3,i,3,-1));
				winningLines.add(oneWinCondtion);
			}
		//yz plane-4
		for(int i = 0; i<4; i++)
			{
				List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
				oneWinCondtion.add(new positionTicTacToe(i,0,0,-1));
				oneWinCondtion.add(new positionTicTacToe(i,1,1,-1));
				oneWinCondtion.add(new positionTicTacToe(i,2,2,-1));
				oneWinCondtion.add(new positionTicTacToe(i,3,3,-1));
				winningLines.add(oneWinCondtion);
			}
		//xy plane-4
		for(int i = 0; i<4; i++)
			{
				List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
				oneWinCondtion.add(new positionTicTacToe(0,0,i,-1));
				oneWinCondtion.add(new positionTicTacToe(1,1,i,-1));
				oneWinCondtion.add(new positionTicTacToe(2,2,i,-1));
				oneWinCondtion.add(new positionTicTacToe(3,3,i,-1));
				winningLines.add(oneWinCondtion);
			}

		//12 anti diagonal winning lines
		//xz plane-4
		for(int i = 0; i<4; i++)
			{
				List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
				oneWinCondtion.add(new positionTicTacToe(0,i,3,-1));
				oneWinCondtion.add(new positionTicTacToe(1,i,2,-1));
				oneWinCondtion.add(new positionTicTacToe(2,i,1,-1));
				oneWinCondtion.add(new positionTicTacToe(3,i,0,-1));
				winningLines.add(oneWinCondtion);
			}
		//yz plane-4
		for(int i = 0; i<4; i++)
			{
				List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
				oneWinCondtion.add(new positionTicTacToe(i,0,3,-1));
				oneWinCondtion.add(new positionTicTacToe(i,1,2,-1));
				oneWinCondtion.add(new positionTicTacToe(i,2,1,-1));
				oneWinCondtion.add(new positionTicTacToe(i,3,0,-1));
				winningLines.add(oneWinCondtion);
			}
		//xy plane-4
		for(int i = 0; i<4; i++)
			{
				List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
				oneWinCondtion.add(new positionTicTacToe(0,3,i,-1));
				oneWinCondtion.add(new positionTicTacToe(1,2,i,-1));
				oneWinCondtion.add(new positionTicTacToe(2,1,i,-1));
				oneWinCondtion.add(new positionTicTacToe(3,0,i,-1));
				winningLines.add(oneWinCondtion);
			}

		//4 additional diagonal winning lines
		List<positionTicTacToe> oneWinCondtion = new ArrayList<positionTicTacToe>();
		oneWinCondtion.add(new positionTicTacToe(0,0,0,-1));
		oneWinCondtion.add(new positionTicTacToe(1,1,1,-1));
		oneWinCondtion.add(new positionTicTacToe(2,2,2,-1));
		oneWinCondtion.add(new positionTicTacToe(3,3,3,-1));
		winningLines.add(oneWinCondtion);

		oneWinCondtion = new ArrayList<positionTicTacToe>();
		oneWinCondtion.add(new positionTicTacToe(0,0,3,-1));
		oneWinCondtion.add(new positionTicTacToe(1,1,2,-1));
		oneWinCondtion.add(new positionTicTacToe(2,2,1,-1));
		oneWinCondtion.add(new positionTicTacToe(3,3,0,-1));
		winningLines.add(oneWinCondtion);

		oneWinCondtion = new ArrayList<positionTicTacToe>();
		oneWinCondtion.add(new positionTicTacToe(3,0,0,-1));
		oneWinCondtion.add(new positionTicTacToe(2,1,1,-1));
		oneWinCondtion.add(new positionTicTacToe(1,2,2,-1));
		oneWinCondtion.add(new positionTicTacToe(0,3,3,-1));
		winningLines.add(oneWinCondtion);

		oneWinCondtion = new ArrayList<positionTicTacToe>();
		oneWinCondtion.add(new positionTicTacToe(0,3,0,-1));
		oneWinCondtion.add(new positionTicTacToe(1,2,1,-1));
		oneWinCondtion.add(new positionTicTacToe(2,1,2,-1));
		oneWinCondtion.add(new positionTicTacToe(3,0,3,-1));
		winningLines.add(oneWinCondtion);

		return winningLines;

	}
	public aiTicTacToe(int setPlayer)
	{
		player = setPlayer;
	}
}
