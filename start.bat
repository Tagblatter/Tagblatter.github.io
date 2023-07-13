call conda activate base
python rss_daily.py
set HTTP_PROXY=http://127.0.0.1:10809
set HTTPS_PROXY=http://127.0.0.1:10809
git add -A
git commit -m "%DATE%"
git push
