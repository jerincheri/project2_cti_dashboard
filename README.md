Run these if using kali
COPY THE GIT LINK
gitclone *link*

GO INSIDE THE PROJECT FOLDER
cd project2_cti_dashboard

CHECK IF REQUIREMENTS ARE LISTED ,,IF YOU SEE THEN INSTALL THEM
ls
pip install -r requirements.txt

RUN THE SERVER
uvicorn main:app --reload

