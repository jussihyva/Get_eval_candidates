# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkauppi <jkauppi@student.hive.fi>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/06 17:31:12 by jkauppi           #+#    #+#              #
#    Updated: 2022/08/06 17:31:16 by jkauppi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

.PHONY: all
all: install_python
	@echo "Done"

.PHONY: install_python
install_python:
	@pip3 install -r requirements_python

.PHONY: run
make run:
	python3 Python/get_eval_candidates.py
