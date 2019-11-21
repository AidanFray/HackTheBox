import os

endpoints = ["search" ,"blog" ,"rss" ,"login" ,"media" ,"files" ,"user" ,"calendar" ,"admin" ,"comment" ,"report" ,"local" ,"pix" ,"tag" ,"group" ,"my" ,"install" ,"lib" ,"portfolio" ,"cache" ,"notes" ,"message" ,"lang" ,"theme" ,"blocks" ,"question" ,"backup" ,"rating" ,"filter" ,"mod" ,"auth" ,"course" ,"error" ,"badges" ,"repository" ,"analytics" ,"availability" ,"webservice" ,"plagiarism" ,"competency"]

for end in endpoints:

    cmd = "wget -r http://10.10.10.153/moodle/" + end

    os.system(cmd)
