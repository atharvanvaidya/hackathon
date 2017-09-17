import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

#raw_query = raw_input("Enter the Product:")
#raw_list = "+".join(raw_query.split())
#query = 's='+str(raw_list)+"#"+str(raw_list)'
#url1 = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='+str(raw_list)+'&rh=i%3Aaps%2Ck%3A'+str(raw_list)
#print url1
#tags = []
total = []
resulttotal = []
fulltotal = []
keyword = ''
while True:
    keyword = raw_input("Enter a Keyword or stop")
    if keyword == 'stop':
        break
    respos = 0.0
    resneg=0.0


    train = [
         ('nice ', 'pos'),
         ('good', 'pos'),
         ('wonderful', 'pos'),
         ('amazing', 'pos'),
         ("pros", 'pos'),
        ('perfect','pos'),
         ('bad', 'neg'),
         ('poor', 'neg'),
         ('horrible', 'neg'),
         ('not good', 'neg'),
         ('very bad', 'neg')
     ]

    cl = NaiveBayesClassifier(train)
    #itemurl = raw_input("Enter the Url of the Review Page of the Searched Item:")
    itemurl = 'https://www.amazon.com/Moto-Plus-5th-Generation-Lockscreen/product-reviews/B01N6NTIRH/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=avp_only_reviews&sortBy=recent&pageNumber='
    for i in range(1,10):
        url = str(itemurl)+str(i)

        request = requests.get(url)
        #request = requests.get('https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='+str(raw_list))
        # Here it comes at the main query searched page

        content = request.content
        soup = BeautifulSoup(content, 'html.parser')
        ratings = soup.find_all('span', {'class': 'a-size-base review-text'})
       
        for line in ratings:
            print str(line)[62:-7]
            total.append(str(line).lower()[61:-7])
        #print len(total)
        blob = TextBlob(str(total).replace(',', '.'))
        #keyword = 'camera'

        for sentence in blob.sentences:
            list_sentence = sentence.split()
            if keyword in list_sentence:
                print list_sentence
                fulltotal.append(str(list_sentence))
                fulltotal.append(str(cl.classify(list_sentence)))                
                print str(cl.classify(list_sentence))
                prob_dist = cl.prob_classify(list_sentence)
                respos += round(prob_dist.prob('pos'), 2)
                resneg +=round(prob_dist.prob('neg'),2)

    if respos>resneg:
        print "good "+str(keyword)
        resulttotal.append(str("Good "+str(keyword)))
        
        print respos
        print resneg
    elif respos<resneg:
        print "bad "+str(keyword)
        resulttotal.append(str("Bad "+str(keyword)))
        print respos
        print resneg
    else:
        print "averge "+str(keyword)
        resulttotal.append(str("Average "+str(keyword)))
#
# if res > 0:
#     print "Good " + str(keyword)
#     print str(res)
# elif res < 0:
#     print "Bad " + str(keyword)
#     print str(res)
# else:
#     print "Average " + str(keyword)
#



#print str(cl.classify("This is an horrible"))

#print str(prob_dist.max())
# print str(round(prob_dist.prob("pos"), 2))
# print str(round(prob_dist.prob("neg"), 2))



f = open('helloworld.html','w')


f.write("""<!DOCTYPE HTML>
<!--
	Visualize by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html>
	<head>
		<title>Visualize by TEMPLATED</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
	<body>

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<span class="avatar"><img src="images/avatar.jpg" alt="" /></span>
						<h1>This is <strong>Visualize</strong>, a responsive site template designed by <a href="http://templated.co">TEMPLATED</a><br />
						and released for free under the Creative Commons License.</h1>
						<ul class="icons">
							<li><a href="#" class="icon style2 fa-twitter"><span class="label">Twitter</span></a></li>
							<li><a href="#" class="icon style2 fa-facebook"><span class="label">Facebook</span></a></li>
							<li><a href="#" class="icon style2 fa-instagram"><span class="label">Instagram</span></a></li>
							<li><a href="#" class="icon style2 fa-500px"><span class="label">500px</span></a></li>
							<li><a href="#" class="icon style2 fa-envelope-o"><span class="label">Email</span></a></li>
						</ul>
					</header>

				<!-- Main -->
					<section id="main">

						<!-- Thumbnails -->
							<section class="thumbnails">
								<div>
									<a href="images/fulls/01.jpg">
										<img src="images/thumbs/01.jpg" alt="" />
										<h3> {0} </h3>
									</a>
									
								</div>
								<div>
									<a href="images/fulls/03.jpg">
										<img src="images/thumbs/03.jpg" alt="" />
										<h3> {1} </h3>
									</a>
									
								</div>
								<div>
									<a href="images/fulls/06.jpg">
										<img src="images/thumbs/06.jpg" alt="" />
										<h3>{2}</h3>
									</a>
									
								</div>
							</section>

					</section>

				<!-- Footer -->
					<footer id="footer">
						<p>&copy; Untitled. All rights reserved. Design: <a href="http://templated.co">TEMPLATED</a>. Demo Images: <a href="http://unsplash.com">Unsplash</a>.</p>
					</footer>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.poptrox.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>""" .format(total,fulltotal,resulttotal))
f.close()
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('file:///var/www/html/hackathon/helloworld.html')
#browser.navigate().to('file:///var/www/html/hackathon/helloworld.html')







