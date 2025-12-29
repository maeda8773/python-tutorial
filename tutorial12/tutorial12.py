# 12. 仮想環境とパッケージ

# --- 仮想環境の作成 ---
# 仮想環境の作成・管理に使われるモジュールは、 venv です

# python -m venv tutorial-env # tutorial-env という名前の仮想環境を作成
# source tutorial-env/bin/activate  # 仮想環境を有効化
# deactivate  # 仮想環境を無効化

# --- pip を使ったパッケージ管理 ---
# Pythonのライブラリを入れたり消したりアップデートしたりする便利コマンド

# pip install パッケージ名  # パッケージのインストール
# pip uninstall パッケージ名  # パッケージのアンインストール
# pip install --upgrade パッケージ名  # パッケージのアップデート
# pip list  # インストールされているパッケージの一覧表示
# pip freeze  # インストールされているパッケージとそのバージョンを表示
# pip show パッケージ名  # パッケージの詳細情報を表示
