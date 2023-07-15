class Block_Controller(object):
    #ブロックが一つ落ちてくるたびに実行されるメソッド
    def GetNextMove(self, nextMove, GameStatus):
        nextMove["strategy"]["direction"] = 0
        nextMove["strategy"]["x"] = 0
        nextMove["strategy"]["y_operation"] = 1
        nextMove["strategy"]["y_moveblocknum"] = 0
        return nextMove
    
    #最後に一度だけ実行されるメソッド。期待される出力値をprintしてください
    def GetLastOutput(GameStatus):
        backboard = GameStatus["field_info"]["backboard"]
        print(backboard)

BLOCK_CONTROLLER = Block_Controller()
