# Webサイトプロジェクト

## フォルダー構成

```
d:/Web/
├── back.py               # Flask バックエンド（エントリーポイント）
├── requirements.txt      # Python パッケージ一覧
├── .gitignore
├── README.md
│
├── templates/            # Jinja2 HTMLテンプレート（Flask が参照）
│   └── index.html
│
├── static/               # Flask の静的ファイル配信ディレクトリ
│   ├── css/
│   │   ├── reset.css
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── images/
│   └── fonts/
│
├── assets/               # 編集用ソース（static/ にコピーして使う）
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
│
├── components/           # 再利用可能なHTMLパーツ（将来用）
├── pages/                # サブページ用テンプレート（将来用）
└── data/                 # JSONなどのデータファイル（将来用）
```

## セットアップ

```powershell
# 依存パッケージのインストール
pip install -r requirements.txt
```

## 開発サーバーの起動

```powershell
python back.py
```

ブラウザで `http://localhost:5000` を開く。

## API エンドポイント

| メソッド | パス         | 説明                     |
|--------|------------|------------------------|
| GET    | `/`         | トップページ               |
| GET    | `/api/hello` | 動作確認用エンドポイント     |
| POST   | `/api/echo`  | 受け取ったJSONをそのまま返す |

## 新しいページの追加方法

1. `templates/` に新しい `.html` ファイルを作成
2. `back.py` に対応するルートを追加

```python
@app.route("/about")
def about():
    return render_template("about.html")
```
