import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

wb = webdriver.Firefox()
xpath = wb.find_element_by_xpath
user = 'escudero.vinicius'
pswd = 'Baruke@01'
urls = ['https://www.youtube.com/playlist?list=PL2DMhvQxwKfvEj_KGBjImFhXWgt9gnyeC','https://www.youtube.com/playlist?list=PL2DMhvQxwKfu0RwKyqT4pRsw0sySbTxXc','https://www.youtube.com/playlist?list=PL2DMhvQxwKftwX2xAKFzyza5cHCSERU3e','https://www.youtube.com/playlist?list=PL2DMhvQxwKfu56Yr_vn36iLKK0ebN1fOY','https://www.youtube.com/playlist?list=PL2DMhvQxwKftilAAYUve7bILebcHX5CSN','https://www.youtube.com/playlist?list=PL2DMhvQxwKft8yejTxLfs_OnmWTN-73VL','https://www.youtube.com/playlist?list=PL2DMhvQxwKfsQg4r3IJWyFXYDkOedfnq4','https://www.youtube.com/playlist?list=PL2DMhvQxwKfsP2pgtDgWNwXXaK7QIzbgr','https://www.youtube.com/playlist?list=PL2DMhvQxwKfsS60UJXymCs00tIEtQwTee','https://www.youtube.com/playlist?list=PL2DMhvQxwKfs9Feov-gmqDYO0l17MoNJt','https://www.youtube.com/playlist?list=PL2DMhvQxwKfuiC44whjiGuRUka0BxAP0k','https://www.youtube.com/playlist?list=PL2DMhvQxwKft_m7vbZVJdghnd1vRbe9sP','https://www.youtube.com/playlist?list=PL2DMhvQxwKftyw8UCUZ2YD_EoUv4c428k','https://www.youtube.com/playlist?list=FLpPIv6wYKtObKsPH2xgMR8Q']

i = 0
wb.get(urls[i])
time.sleep(4)
btn = xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/div[2]/ytd-button-renderer')  # Sign In
btn.click()
time.sleep(1)
btn = xpath('//*[@id="identifierId"]')  # Email
btn.send_keys(user)
btn = xpath('//*[@id="identifierNext"]')  # Next
btn.click()

time.sleep(1)
btn = xpath(
	'/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')  # user
btn.send_keys(pswd)
time.sleep(1)
btn = xpath('//*[@id="passwordNext"]')
btn.click()

i = 1
while urls != '':

	try:
		wb.get(urls[i])
		time.sleep(2)
		btn = xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-playlist-sidebar-renderer/div/ytd-playlist-sidebar-secondary-info-renderer/div/div[2]/ytd-button-renderer/a')#Enable edit
		btn.click()

		time.sleep(1)
		btn = xpath('//*[@id="playlist-settings-editor"]')#Paylist Edit
		btn.click()


		time.sleep(10)
		btn = Select(xpath('/html/body/div[2]/div[4]/div/div[5]/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/span[2]/div[1]/div/div/div[1]/div[3]/form/div[1]/div[1]/div[1]/span/select'))#Drop down list
		btn.select_by_visible_text('Private')#Select Private

		time.sleep(1)
		btn = xpath('/html/body/div[2]/div[4]/div/div[5]/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/span[2]/div[1]/div/div/div[1]/div[5]/button[2]')#save
		btn.click()
		time.sleep(2)
	except NoSuchElementException:
		i = i + 1
		pass

i = i + 1



#https://www.youtube.com/playlist?list=PL2DMhvQxwKfsWNn_SqEoRV4cOpS5pSzir
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfubbH10cLbxbGq29Uxp4btf
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfvh6ltSyXGZEdAuADQJJY_5
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfu9dpX_XeF-7-ShO2wzO3GC
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfvxTzLCNVtpIa0K8u67cfIM
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfvEj_KGBjImFhXWgt9gnyeC
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfu0RwKyqT4pRsw0sySbTxXc
#https://www.youtube.com/playlist?list=PL2DMhvQxwKftwX2xAKFzyza5cHCSERU3e
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfu56Yr_vn36iLKK0ebN1fOY
#https://www.youtube.com/playlist?list=PL2DMhvQxwKftilAAYUve7bILebcHX5CSN
#https://www.youtube.com/playlist?list=PL2DMhvQxwKft8yejTxLfs_OnmWTN-73VL
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfsQg4r3IJWyFXYDkOedfnq4
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfsP2pgtDgWNwXXaK7QIzbgr
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfsS60UJXymCs00tIEtQwTee
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfs9Feov-gmqDYO0l17MoNJt
#https://www.youtube.com/playlist?list=PL2DMhvQxwKfuiC44whjiGuRUka0BxAP0k
#https://www.youtube.com/playlist?list=PL2DMhvQxwKft_m7vbZVJdghnd1vRbe9sP
#https://www.youtube.com/playlist?list=PL2DMhvQxwKftyw8UCUZ2YD_EoUv4c428k
#https://www.youtube.com/playlist?list=FLpPIv6wYKtObKsPH2xgMR8Q
