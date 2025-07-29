# shellcheck shell=bash

task.format() {
	pipx run ruff format ./**/kofler*.py
}
