

install:
	- virtualenv -p python3.8 venv   
	- ( \
       . venv/bin/activate; \
       pip3 install -U -r requirements.txt;  \
    )

run:
	- ( \
       . venv/bin/activate; \
       jupyter notebook \
    )

