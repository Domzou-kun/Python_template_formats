"""
    Python program template ver.1.1

    概要
        Pythonでプログラムを作り始める際に必要な処理を記したテンプレートコード
        argparse+mainの標準テンプレート

    ユーザースニペット
        VS codeなどでは使用頻度の高いプログラムなどを登録しておくことが可能である
        素早く開発や書き始めを行うためにこのようなプログラムを丸ごと登録しておくと便利である

        ユーザースニペットについて
            https://blanche-toile.com/web/vscode-snippets
    
    Version
        1.1 : 解説コメントによる解説有、中規模クラスを目的とした簡易的なテンプレート
        1.2 : 解説コメント無
        2.1 : main文のみ
        3.1 : main+argparse

    その他
        同様の内容をgithubのreadmeに記しております
"""

# -*- coding: utf-8 -*-

from logging import *
import argparse



""" 引数を取得する関数"""
def get_argument():
    
    """ 引数のparser """
    parser = argparse.ArgumentParser(
                prog = 'ProgramName', 
                description = 'What the program does', 
                epilog = 'Text at the bottom of help')
    
    """ 各引数の詳細な設定 """
    parser.add_argument(
                '-a1',                              # 引数の省略形
                '--arg1',                           # 引数name
                help="argument help document",      # 引数に関するヘルプ
                default="default argument of 1",    # デフォルト値
                required=False)                     # 引数の必須指定

    parser.add_argument('-a2', '--arg2', help="argument help document", default="default argument of 2", required=False)    # 一行で書く場合

    return parser.parse_args()

""" display list"""
def display_list(display_data_list, display_title_str: str):
    name_max_string_length = max([len(v[0]) for v in display_data_list])   # nameの最大文字数
    value_max_string_length = max([len(v[1]) for v in display_data_list])  # valueの最大文字数
    
    partition_msg = "="*name_max_string_length + " " + "="*value_max_string_length
    print("\n"+display_title_str)
    print(partition_msg)
    for setting_data in display_data_list:
        name_msg = str(setting_data[0]).rjust(name_max_string_length)      # 引数名
        value_msg = str(setting_data[1]).rjust(value_max_string_length)    # 引数で与えられる値
        print(name_msg + " " + value_msg)
    print(partition_msg)

""" main """
def main():
    pass

if __name__ == "__main__":

    args = get_argument()   # 引数の獲得
    
    """ args list display"""
    if False:               # コマンドライン引数の表示    ## 初期値Falseで非表示設定
        args_setting_list = []
        if args.arg1:
            arg_1 = args.arg1   # 引数1
            args_setting_list.append(["--arg1", arg_1])
        if args.arg2:
            arg_2 = args.arg2   # 引数2
            args_setting_list.append(["--arg2", arg_2])

        display_list(display_data_list=args_setting_list, display_title_str="argument list")
    else:
        arg_1 = args.arg1
        arg_2 = args.arg2   


    """ main program """
    main()