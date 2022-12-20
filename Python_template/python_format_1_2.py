"""
    Python program template ver.1.2

    概要
        Pythonでプログラムを作り始める際に必要な処理を記したテンプレートコード
        中規模程度の開発などを行う場合に直ぐにmainを書き始めたり、argparseを用いた引数の処理を行える

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
import logging.config
import sys
import platform
import datetime
import argparse
import json


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

    """ loggin setting"""
    if False:    # jsonでloggingの設定を呼び出す場合:True
        with open(r"config_folder\python_format_logging_conf.json", "r") as logging_config_file:
            logging_config = json.load(logging_config_file)
        logging.config.dictConfig(logging_config)
        logger = getLogger(__name__)
    else:       # コード内に直接loggingの設定を記述する場合    ## 記述量が多くなりがちなのでjsonファイルのようなものにまとめておくのが良い
        logger = getLogger(__name__)    # 現在の実行関数名の取得
        
        log_sh = StreamHandler(sys.stdout)  # 出力先の設定
        log_fmt = Formatter("%(asctime)s - ( %(name)s ) =>> line %(lineno)s\n    [%(levelname)s] : %(message)s", "%Y-%m-%d%H:%M:%S")    # 出力する文字列の設定
        
        log_sh.setLevel(DEBUG)
        log_sh.setFormatter(log_fmt)
        logger.addHandler(log_sh)

    """ program setting display """
    if False:
        information_list = []
        information_list.append(["Python version", sys.version])                 # PythonのVersion
        information_list.append(["OS version", platform.platform()])             # osのversion
        information_list.append(["Date", datetime.datetime.now().isoformat()])   # 実行日時

        display_list(display_data_list=information_list, display_title_str="program information")

    """ main program """
    main()