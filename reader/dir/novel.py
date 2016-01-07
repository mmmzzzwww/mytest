# -*- coding: utf-8 -*- 
  
import urllib2 
import re 
import thread 
import chardet 
from Tkinter import *
import tkFont
from ScrolledText import ScrolledText
now_url=0

novel_list = {u'无尽神功':["http://www.5800.cc/5200/0/268/","203818.html"],
u'一等家丁':["http://www.5800.cc/5200/0/3/","771.html"],
u'傲世九重天':["http://www.5800.cc/5200/0/5/","861.html"],
u'绝世唐门':["http://www.5800.cc/5200/0/549/","10074807.html"],
u'天才相师':["http://www.5800.cc/5200/0/21/","3817.html"],
u'明末传奇':["http://www.5800.cc/5200/73/73819/","9379577.html"],
u'时空走私':["http://www.5800.cc/5200/73/73697/","9353689.html"],
u'天才医生':["http://www.5800.cc/5200/0/22/","3973.html"],
u'凡人修仙传':["http://www.5800.cc/5200/0/52/","16260.html"],
u'杀神':["http://www.5800.cc/5200/0/28/","7129.html"],
u'神级天赋':["http://www.5800.cc/5200/1/1789/","1110412.html"],
u'校花的贴身高手':["http://www.5800.cc/5200/0/27/","6800.html"],
u'鬼吹灯':["http://www.5800.cc/5200/0/435/","354485.html"],
u'神墓':["http://www.5800.cc/5200/6/6925/","2606286.html"],
u'全能奇才':["http://www.5800.cc/5200/0/24/","27235.html"],
u'莽荒纪':["http://www.5800.cc/5200/0/559/","645246.html"],
u'仙逆':["http://www.5800.cc/5200/0/29/","7143.html"],
u'斗破苍穹':["http://www.5800.cc/5200/0/95/","36022.html"],
u'异界流氓天尊':["http://www.5800.cc/5200/8/8937/","2522326.html"],
u'吞噬星空':["http://www.5800.cc/5200/0/32/","7460.html"],
u'盘龙':["http://www.5800.cc/5200/3/3548/","1811748.html"],
u'九鼎记':["http://www.5800.cc/5200/0/330/","247668.html"],
u'西游记':["http://www.5800.cc/5200/4/4931/","1981517.html"],
u'水浒传':["http://www.5800.cc/5200/7/7662/","2242521.html"],
u'红楼梦':["http://www.5800.cc/5200/7/7667/","2242952.html"],
u'三国志':["http://www.5800.cc/5200/4/4103/","1898243.html"],
u'初刻拍案惊奇':["http://www.5800.cc/5200/4/4105/","1898348.html"],
u'二刻拍案惊奇':["http://www.5800.cc/5200/4/4106/","1898388.html"],
u'哈利波特':["http://www.5800.cc/5200/7/7684/","2244118.html"],
u'假如给我三天光明':["http://www.5800.cc/5200/39/39360/","5715373.html"],
u'围城':["http://www.5800.cc/5200/7/7279/","2215485.html"],
u'边城':["http://www.5800.cc/5200/51/51945/","6376677.html"],
u'红高粱':["http://www.5800.cc/5200/50/50236/","6328919.html"],
u'百年孤独':["http://www.5800.cc/5200/51/51148/","6352797.html"],
u'暴风雨':["http://www.5800.cc/5200/39/39395/","5716078.html"],
u'钢铁是怎样炼成的':["http://www.5800.cc/5200/7/7327/","2219189.html"],
u'悲惨世界':["http://www.5800.cc/5200/16/16747/","3742295.html"],
u'罗密欧与朱丽叶':["http://www.5800.cc/5200/39/39383/","5715994.html"],
u'基督山伯爵':["http://www.5800.cc/5200/7/7673/","2243371.html"],
u'':[],
u'':[],
}

bookmark =[]
class Book_Spider: 
  def __init__(self): 
    self.pages = [] 
    self.page = 1
    self.flag = 1
    self.rnx = "10074807.html"
    self.url = "http://www.5800.cc/5200/0/549/"
    self.nx =  "10074807.html"
    self.last_url = self.url
    self.last_nx = self.nx
  
  # 将抓取一个章节 
  def GetPage(self):
    last2_nx=self.last_nx
    self.last_url= self.url
    self.last_nx = self.nx
    myUrl = self.url+self.nx
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent } 
    req = urllib2.Request(myUrl, headers = headers) 
    myResponse = urllib2.urlopen(req) 
    myPage = myResponse.read() 
    
    charset = chardet.detect(myPage) #检测编码
    charset = charset['encoding'] 
    if charset == 'utf-8' or charset == 'UTF-8': 
      myPage = myPage 
    else: 
      myPage = myPage.decode('gb2312','ignore').encode('utf-8') 
    unicodePage = myPage.decode("utf-8") 
  
    # 找出 id="content"的div标记 
    try: 
      #抓取标题 
      my_title = re.search('<h1>(.*?)</h1>',unicodePage,re.S) #多行匹配 re.S
      my_title = my_title.group(1) 
    except: 
      print u'标题 HTML 变化，请重新分析！'
      return 0
      
    try: 
      #抓取章节内容 
      my_content = re.search('<div id="content">(.*?)<br/',unicodePage,re.S) 
      my_content = my_content.group(1) 
    except: 
      print u"内容 HTML 变化，请重新分析！"
      return 0
      
    my_content = my_content.replace("<br />","\n") 
    my_content = my_content.replace(" "," ")
    my_content = my_content.replace("&nbsp;"," ")
    #用字典存储一章的标题和内容 
    onePage = {'title':my_title,'content':my_content,'next':self.nx,'last_url':self.last_url,'last_nx':self.last_nx,'l_nx':last2_nx} 
    try: 
      #找到页面下方的连接区域 
      foot_link = re.search('<div class="read_left">(.*)read02',unicodePage,re.S) 
      foot_link = foot_link.group(1)
      su_link = re.search('<DIV.*?class=bt3>(.*?)<div',foot_link,re.S) 
      su_link = su_link.group(1)      
      #在连接的区域找下一页的连接，根据网页特点为第三个 
      nextUrl = re.findall(u'<A.*?href="(.*?)".*?>(.*?)</A>',su_link,re.S)
      dir_url = nextUrl[1][0]
      last2_nx =nextUrl[0][0]
      nextUrl = nextUrl[2][0]
      if(dir_url == nextUrl): 
        self.flag = 0
      self.nx = nextUrl
      onePage = {'title':my_title,'content':my_content,'next':self.nx,'last_url':self.last_url,'last_nx':self.last_nx,'l_nx':last2_nx}
    except: 
      print u"底部链接变化，请重新分析!"
      return 0
    onePage = {'title':my_title,'content':my_content,'next':self.nx,'last_url':self.last_url,'last_nx':self.last_nx,'l_nx':last2_nx}    
    return onePage 
  def downloadPage(self):
    self.nx=self.rnx
    global name
    f_txt = open(name+".txt",'w+') 
    i=0
    a=len(self.pages)
    while self.flag: 
      try: 
        if i<a:
            myPage = self.pages[i]
            i=i+1
        else:
            myPage = self.GetPage()
        if myPage == 0: 
            print u'抓取失败！'
            self.flag = 0
  
        title = myPage['title'].encode('utf-8') 
        content = myPage['content'].encode('utf-8') 
  
        f_txt.write(title + '\n\n') 
        f_txt.write(content) 
        f_txt.write('\n\n\n') 
  
        print u"已下载 ",myPage['title'] 
  
      except: 
        print u'无法连接服务器！'
        self.flag = 0
          
    f_txt.close() 
  # 用于加载章节 
  def LoadPage(self): 
    while self.flag: 
      if(len(self.pages) - self.page < 3): 
        try: 
          myPage = self.GetPage() 
          if myPage == 0: 
            print u'抓取失败！'
            self.flag = 0
          self.pages.append(myPage) 
        except: 
          print u'无法连接网页！'
          self.flag = 0
    
  def Start(self):
    # 新建一个线程 
    thread.start_new_thread(self.LoadPage,())         
myBook = Book_Spider() 
thread.start_new_thread(myBook.GetPage,())
def last_page():
    global t,l
    if l['l_nx'] !="index.html":
        t.delete(0.0, END)        
        myBook.nx = l['l_nx']
        l=myBook.GetPage()
        t.insert(INSERT,l['title'])
        t.insert(INSERT,'\n------------------------------\n')
        t.insert(INSERT, l['content'])
        m2.add(t)
def search():
    global name,l,m2
    if name in novel_list.keys():
         myBook.url = novel_list[name][0]
         myBook.rnx = novel_list[name][1]
         myBook.nx  = novel_list[name][1]
         l = myBook.GetPage()
         t.delete(0.0, END)
         t.insert(INSERT,l['title'])
         t.insert(INSERT,'\n------------------------------\n')
         t.insert(INSERT, l['content'])
         m2.add(t)
    else:
         t.delete(0.0, END)
         t.insert(INSERT,u"没有找到"+name+u"这本书！！！！")
         m2.add(t)
def next_page():
    global t,l
    t.delete(0.0, END)
    l = myBook.GetPage()
    t.insert(INSERT,l['title'])
    t.insert(INSERT,'\n------------------------------\n')
    t.insert(INSERT, l['content'])
    m2.add(t) 
def download():    
    myBook.downloadPage()
def ChangeColor():
    global t,l
    if t['bg']=='white':
        t.delete(0.0, END)
        t['bg']='gray'
        t.insert(INSERT,l['title'])
        t.insert(INSERT,'\n------------------------------\n')
        t.insert(INSERT, l['content'],)
        m2.add(t)
    elif t['bg']=='gray':
        t.delete(0.0, END)
        t['bg']='green'
        t.insert(INSERT,l['title'])
        t.insert(INSERT,'\n------------------------------\n')
        t.insert(INSERT, l['content'],)
        m2.add(t)
    elif t['bg']=='green':
        t.delete(0.0, END)
        t['bg']='Navajo White'
        t.insert(INSERT,l['title'])
        t.insert(INSERT,'\n------------------------------\n')
        t.insert(INSERT, l['content'],)
        m2.add(t)
    else:
        t.delete(0.0, END)
        t['bg']='white'
        t.insert(INSERT,l['title'])
        t.insert(INSERT,'\n------------------------------\n')
        t.insert(INSERT, l['content'],)
        m2.add(t)
r=0
def BookMark():
    global r,m7
    def skip():
        global t,l
        t.delete(0.0,END)
        myBook.url = bookmark[i][3]
        myBook.nx = bookmark[i][4]
        l=myBook.GetPage()
        t.insert(INSERT,l['title'])
        t.insert(INSERT,'\n------------------------------\n')
        t.insert(INSERT, l['content'])
        m2.add(t)
    for i in range(r,len(bookmark)):
        bookmark[i][0]=Button(m7,bg='Navajo White',text=bookmark[i][1]+bookmark[i][2],command = skip)
        m7.add(bookmark[i][0])
        r = len(bookmark)
    emb=Button(m7,bg='Navajo White',text='')
    m7.add(emb)
def addmark():
    global t,name,l
    bookmark.append([len(bookmark),name,l['title'],l['last_url'],l['last_nx']])
def changesize1():
    global helv36,t,l,a
    a = a+5
    helv36 = tkFont.Font(size=a,weight="normal",slant='roman')
    print(a)    
    t.delete(0.0, END)
    t['font']=helv36
    t.insert(INSERT,l['title'])
    t.insert(INSERT,'\n------------------------------\n')
    t.insert(INSERT, l['content'],)
    m2.add(t)
def changesize2(): 
    global helv36,t,l,a
    if a>5:
        a = a-5
        print(a)
        helv36 = tkFont.Font(size=a,weight="normal",slant='roman')
        t['font']=helv36        
        t.delete(0.0, END)
        t.insert(INSERT,l['title'])
        t.insert(INSERT,'\n------------------------------\n')
        t.insert(INSERT, l['content'],)
        m2.add(t)
name = u"绝世唐门"
root = Tk()
root.title("小说阅读器1.0")
root.geometry('800x600')
m1=PanedWindow(height=600,width=800)
m1.pack()

m2=PanedWindow(m1,height=600,width=600,orient=VERTICAL)
m1.add(m2)
m3=PanedWindow(m1,height=600,width=200,orient=VERTICAL)
m1.add(m3)

m4=PanedWindow(m2,height=50,width=600)
m2.add(m4)
m5=PanedWindow(m2,height=50,width=600)
m2.add(m5)
m6=PanedWindow(m3,height=100,width=200,orient=VERTICAL)
m3.add(m6)
m7=PanedWindow(m3,height=500,width=200,orient=VERTICAL,bg='Navajo White')
m3.add(m7)
l = myBook.GetPage()    
e = StringVar()
entry = Entry(m4,bg='Lemon Chiffon',validate='key', textvariable=e, width=50,font=20)
def pri(event=None):
    global name
    name = e.get()
entry.bind('<Return>',pri)
m4.add(entry)
a = 15
helv36 = tkFont.Font(size=a,weight="normal",slant='roman')
b3=Button(m4,text='搜索',command = search,bg='Navajo White')
m4.add(b3)
b6=Button(m5,text='添加书签',command = addmark,bg='Navajo White')
m5.add(b6)
t = ScrolledText(m2,font=helv36,bg='Navajo White',height=400,width=600)
t.insert(INSERT,'小说正文')

m2.add(t)
b4=Button(m5,text='护眼模式',command = ChangeColor,bg='Navajo White')
m5.add(b4)
b2=Button(m5,text='下载',command = download,bg='Navajo White')
m5.add(b2)
b10=Button(m5,text="A+",command=changesize1,bg='Navajo White')
b11=Button(m5,text="A-",command=changesize2,bg='Navajo White')
m5.add(b10)
m5.add(b11)
b12=Button(m5,text='上一章',command = last_page,bg='Navajo White')
m5.add(b12)
b1=Button(m5,text='下一章',command = next_page,bg='Navajo White')
m5.add(b1)
b5 =Button(m6,text="我的书签",command = BookMark,bg='Navajo White')
m6.add(b5)
root.mainloop()
