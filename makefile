.PHONY: update get

update:
	git add -A
	git commit -m "Updated: `date +'%Y%m%d %H:%M:%S'`"
	git push

get:
	git fetch
	git pull
