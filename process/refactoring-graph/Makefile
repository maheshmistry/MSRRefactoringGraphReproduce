build:
	yarn build

deploy: build
	cd build && git init || echo "git ok"
	cd build && git remote add deploy https://github.com/refactoring-graph/refactoring-graph.github.io.git || echo "remote ok"
	cd build && touch README.md
	cd build && echo "# Mirror from  https://github.com/alinebrito/refactoring-graph" > README.md
	cd build && git add .
	cd build && git commit -v --no-edit --amend || git commit -m "deploy" || echo "changes ok"
	cd build && git push deploy master -f
