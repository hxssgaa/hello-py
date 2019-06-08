git checkout $1
git pull
python3 -m ptvsd --host 0.0.0.0 --port 9500 --wait $2