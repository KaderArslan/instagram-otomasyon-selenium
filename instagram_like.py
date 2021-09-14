from selenium import webdriver
import time

users = 0           #işlem yapılacak kullanıcılar
file_size = 0       #dosya boyutu
users_counter = 0   #kullanıcı sayacı
first_post = 0      #hata kontrolleri
second_error = 0
like_error = 0
post_error = 0
like2_error = 0
post2_error = 0
url_error = 0       
like_limit = 0      #beğeni sınırı
like_counter = 0    #beğeni sayacı 

start_time = time.strftime('%X')
print("Start Time= " + start_time)

second_time = time.strftime('%S')
print("Başlangıç saniyesi= " + second_time)


"""#Create a file in the directory where it is located
username_password_file = open("username_password.txt", "w")
users_file = open("users.txt", "w")
no_likes_file = open("no_likes_file.txt", "a")"""

no_likes_file = open("no_likes_file.txt", "w")

with open("users_file.txt", "r", encoding='utf-8') as users_file:  # @ ile başlayan kullanıcılar hesaplanır
    for i in open("users_file.txt", "r", encoding='utf-8'):
        user_name = users_file.readline()
        if (user_name.startswith("@")) == 1:
            users = users + 1
print("@ users : ")
print(users)

with open("users_file.txt", "r", encoding='utf-8') as _:  # dosya boyutu hesaplanır
    for i in open("users_file.txt", "r", encoding='utf-8'):
        file_size = file_size + 1
print("file size : ")
print(file_size)

browser = webdriver.Chrome()
browser.get("https://www.instagram.com")
time.sleep(1)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
with open("username_password_file.txt", "r", encoding='utf-8') as username_password_file:  # kullanıcı adı ve şifresi username_password_file dosyasından alınır
    username.send_keys(username_password_file.readline())
    time.sleep(2)
    password.send_keys(username_password_file.readline())
    time.sleep(1)

login_to_instagram = browser.find_element_by_xpath("//*[contains(text(),'Giriş Yap')]")
login_to_instagram.click()
time.sleep(5)


with open("users_file.txt", "r", encoding='utf-8') as users_file:  # users_file dosyasını açar okur ve kapatır
    for i in range(file_size):
        username_ = users_file.readline()
        space = username_.find(" ")
        if (username_.startswith("@")) == 1:
            username_ = username_[1:space]
            try:
                url = "https://www.instagram.com/" + username_.replace('@', '')
                url_error = 1
            except:
                url_error = 0
                print("url hatası")
                print("https://www.instagram.com/" + username_.replace('@', '') + " Like Error")
                no_likes_file.write("@"+username_+"\n")
            if(url_error == 1):
                url = "https://www.instagram.com/" + username_.replace('@', '')
                browser.get(url)
                time.sleep(1)
                
            private_account= None
            try:  # gizli kullanıcı kontrolü yapar
                #private_account = browser.find_element_by_tag_name("article h2").get_attribute("innerHTML")
                private_acoount = browser.find_element_by_xpath("//*[contains(text(),'Bu Hesap Gizli')]")
                if (private_acoount != None):
                    continue
            except:
                #print("gizli hesap hatası")
                first_error = 0
                
            try:
                first_post = browser.find_element_by_tag_name("article a")
                first_error = 1
            except:
                print("birinci post hatası")
                first_error = 0
                
            if (first_error == 1):
                try:
                    first_post = browser.find_element_by_tag_name("article a")
                    post_error = 1
                except:
                    print("first_post hatası")
                    post_error = 0
                    print("https://www.instagram.com/" + username_.replace('@', '') + " Like Error")
                    no_likes_file.write("@"+username_+"\n")
                if(post_error == 1):
                    first_post = browser.find_element_by_tag_name("article a")
                    first_post.click()
                    time.sleep(2)
                try:
                    post_like = browser.find_element_by_tag_name('article section:first-child span:first-child button')
                    like_error = 1
                except:
                    print("post1_like hatası")
                    like_error = 0
                    print("https://www.instagram.com/" + username_.replace('@', '') + " Like Error")
                    no_likes_file.write("@"+username_+"\n")
                if(like_error == 1):
                    post_like = browser.find_element_by_tag_name('article section:first-child span:first-child button')
                    like_control = post_like.find_element_by_tag_name("svg:first-child").get_attribute("aria-label")
                    if (like_control == "Beğen"):
                        post_like.click()
                        like_counter = like_counter + 1
                        time.sleep(1)
                    elif (like_control == "Beğenmekten Vazgeç"):
                        post_like.click()
                        like_counter = like_counter + 1
                        time.sleep(1)
                        post_like.click()
                        like_counter = like_counter + 1
                        time.sleep(1)
            if first_error != 1:
                print("https://www.instagram.com/" + username_.replace('@', '') + " Like Error")
                no_likes_file.write("@"+username_+"\n")
            try:
                #second_post = browser.find_element_by_css_selector("//*[contains(text(),'Sonraki')]")
                #second_post = browser.find_element_by_element("<a class=' _65Bje coreSpriteRightPaginationArrow' tabindex='0'>Sonraki</a>")
                second_post = browser.find_element_by_css_selector("body>div._2dDPU.CkGkG>div.EfHg9>div>div>a") # > bir sonraki gonderiye gider    
                second_error = 1
            except:
                print("ikinci post hatası")
                second_error = 0
                
            if (second_error == 1):
                try:
                    second_post = browser.find_element_by_css_selector("body>div._2dDPU.CkGkG>div.EfHg9>div>div>a")
                    post2_error = 1
                except:
                    post2_error = 0
                    time.sleep(5)
                    print("second_post hatası")
                    print("https://www.instagram.com/" + username_.replace('@', '') + " Like Error")
                    no_likes_file.write("@"+username_+"\n")
                if(post2_error==1):
                    second_post = browser.find_element_by_css_selector("body>div._2dDPU.CkGkG>div.EfHg9>div>div>a")
                    second_post.click()
                    time.sleep(1)
                    try:
                        post_like = browser.find_element_by_tag_name('article section:first-child span:first-child button')
                        like2_error = 1
                    except:
                        like2_error = 0
                        print("post2_like hatası")
                        print("https://www.instagram.com/" + username_.replace('@', '') + " Like Error")
                        no_likes_file.write("@"+username_+"\n")
                    if(like2_error == 1):
                        post_like = browser.find_element_by_tag_name('article section:first-child span:first-child button')
                        like_control = post_like.find_element_by_tag_name("svg:first-child").get_attribute("aria-label")
                        if (like_control == "Beğen"):
                            post_like.click()
                            like_counter = like_counter + 1
                            time.sleep(1)
                        elif (like_control == "Beğenmekten Vazgeç"):
                            post_like.click()
                            like_counter = like_counter + 1
                            time.sleep(1)
                            post_like.click()
                            like_counter = like_counter + 1
                            time.sleep(1)
                        time.sleep(1)
            if(like_counter ==
no_likes_file.close()
               
browser.close();
            
