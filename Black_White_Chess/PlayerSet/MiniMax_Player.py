import sys; sys.path.append('../')
import random
from Black_White_Chess.PlayerSet.player import Player
# import copy
import time


class MiniMaxPlayer(Player):
    """
    随机玩家, 随机返回一个合法落子位置
    """

    def __init__(self, color):
        """
        继承基类玩家，玩家初始化
        :param color: 下棋方，'X' - 黑棋，'O' - 白棋
        """
        super().__init__(color)

    # other color
    def flipColor(self):
        return 'X' if self.color == 'O' else 'O'

    # min
    def min_value(self, board):
        action_list = list(board.get_legal_actions(self.flipColor()))
        if len(action_list) == 0:
            # print('-----------------------------')
            return board.count(self.color)

        minScore = 1000
        for each in action_list:
            # min最大值
            flipSet = board._move(each, self.flipColor())
            score = self.max_value(board)
            board.backpropagation(each, flipSet, self.flipColor())

            # 更新最优解
            if minScore > score:
                minScore = score
        return minScore

    # max
    def max_value(self, board, flag=False):
        action_list = list(board.get_legal_actions(self.color))
        if len(action_list) == 0:
            # print('+++++++++++++++++++++++++++++')
            return board.count(self.color)

        maxScore = -1000
        for each in action_list:
            # min最大值
            flipSet = board._move(each, self.color)
            score = self.min_value(board)
            board.backpropagation(each, flipSet, self.color)
            # 更新最优解
            if maxScore < score:
                maxScore = score
        return maxScore

    # minimax搜索
    def minimax_decision(self, board):
        bestAction = None
        maxScore = -1000

        action_list = list(board.get_legal_actions(self.color))
        for each in action_list:
            # min最大值
            flipSet = board._move(each, self.color)
            score = self.min_value(board)
            board.backpropagation(each, flipSet, self.color)
            # 更新最优解
            if maxScore < score:
                maxScore = score
                bestAction = each

        return bestAction

    def random_choice(self, board):
        # 用 list() 方法获取所有合法落子位置坐标列表
        action_list = list(board.get_legal_actions(self.color))
        # 如果 action_list 为空，则返回 None,否则从中选取一个随机元素，即合法的落子坐标
        if len(action_list) == 0:
            return None
        else:
            return random.choice(action_list)

    def get_move(self, board):
        """
        根据当前棋盘状态获取最佳落子位置
        :param board: 棋盘
        :return: action 最佳落子位置, e.g. 'A1'
        """
        if self.color == 'X':
            player_name = '黑棋'
        else:
            player_name = '白棋'
        print("请等一会，对方 {}-{} 正在思考中...".format(player_name, self.color))
        sum = board.count(self.flipColor()) + board.count(self.color)
        print('{}', sum)
        if sum < 45:
            action = self.random_choice(board)
        else:
            action = self.minimax_decision(board)
        # while True:
        #     x = input('is END?')
        #     if x == 'END':
        #         break
        return action