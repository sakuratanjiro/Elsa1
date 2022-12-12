if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository
  git clone https://github.com/sakuratanjiro/sakuraa /sakuraa
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /sakuraa
fi
cd /sakura
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
