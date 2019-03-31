mkdir $1
python -m pyftpdlib --directory=$1 --port=2121 --write
