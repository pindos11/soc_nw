S_DOCTYPE = "<!DOCTYPE html>"
NW_NAME = "stankin-nw"
HELLO_MSG = "stankin-nw – универсальное средство для\
 общения и поиска друзей и одноклассников,\
которым ежедневно пользуются десятки миллионов человек.(нет)"
WRONG_LOGPWD = "Неверный пароль или логин."
import sqlite3, time
def set_title(title):
    return("<title>"+title+"</title>")

def set_tag(name,args):#creates an unclosed html tag
    name = name.upper()
    Out = "<"+name
    if(name=="FORM"):
        Out+=' '+'accept-charset="utf-8"'+' ' #if it is form - sets charset
    for i in args:
        if(type(args[i]) is str):
            if(i=='clas'):
               Out+=" "+i+"s"+" = \""+str(args[i])+"\""#if class specified for html entity
            else:
                Out+=" "+i+" = \""+str(args[i])+"\""#if value is string
        elif(type(args[i]) is int):
            Out+=" "+i+" = "+str(args[i])
    Out+=">"
    return Out

def close_tag(name):#closes tag with given name
    name = name.upper()
    return "</"+name+">"

def make_elem(tag_name,content,**args):#makes element
    Out = []
    Out.append('\n'+set_tag(tag_name,args))#opens tag
    Out.append(content)#adds given content
    Out.append(close_tag(tag_name))#closes this tag
    return(Out)

def make_tops(u_name):#makes top divs, the line with user's name and exit button
    exit_img = '\n'.join(make_elem('img','',src='../imgs/exit.gif',width=20,height=20,onclick='logoff()'))
    tcont = '\n'.join(make_elem('p',u_name+exit_img,clas='user_n'))
    topdivs = '\n'.join(make_elem('div',tcont,id = 'top1'))
    topdivs += '\n'.join(make_elem('div','',id = 'top2'))    
    return topdivs

def make_head(u_name,login):#makes head: sets charset, links scripts and css? sets users login as id for head 
    headC = set_title(u_name+' - '+NW_NAME)+'\n'
    headC+='<meta charset="windows-1251">'
    headC+='<link rel=stylesheet type=text/css href=../mstyle.css media=all />'
    headC+='\n'.join(make_elem('script','',src='../mscripts.js',charset='CP1251'))

    head = '\n'.join(make_elem('head',headC,id=login))
    return head

def make_users_list(u_name):#makes list of users that are not friends for current user
    db = sqlite3.connect('users.db')
    cur = db.cursor()
    cur.execute('SELECT name,fname,sname FROM users WHERE name !=?',(u_name,))
    f_list = cur.fetchall()
    nofriends = 1
    try:
        cur.execute('SELECT friends FROM friends WHERE name =?',(u_name,))
        friends_list = cur.fetchone()[0]
        nofriends = 0
    except:
        nofriends = 1
    fl = []
    for user in f_list:
        if(nofriends==0):
            if(friends_list.rfind(user[0])==-1):
                add_f_b = '\n'.join(make_elem('img','',src='../imgs/add.png',onclick='f_add(event.currentTarget)',id= user[0],clas='add_f_b',width=15))
                fl.append('\n'.join(make_elem('a',user[1]+' '+user[2]+add_f_b,id = user[0],clas='u_list_name')))
        else:
                add_f_b = '\n'.join(make_elem('img','',src='../imgs/add.png',onclick='f_add(event.currentTarget)',id= user[0],clas='add_f_b',width=15))
                fl.append('\n'.join(make_elem('a',user[1]+' '+user[2]+add_f_b,id = user[0],clas='u_list_name')))
    return 'Все пользователи:'+'<hr>'+'<br>'.join(fl)

def make_friends_list(u_name):#makes list of users that are friends for current user
    db = sqlite3.connect('users.db')
    cur = db.cursor()
    fl = []
    try:
        cur.execute('SELECT friends FROM friends WHERE name =?',(u_name,))
        f_list = cur.fetchone()[0]
        for user in f_list.split('^^'):
            cur.execute('SELECT fname,sname FROM users WHERE name =?',(user,))
            zname = ' '.join(cur.fetchone())
            fl.append('\n'.join(make_elem('a',zname,onclick = 'sel(event.currentTarget)',id = user,clas='u_list_name')))
    except:
        fl=['никого нету','дружите сильнее']
    return 'Друзья:'+'<hr>'+'<br>'.join(fl)
	
	
def make_news_div():#makes div, containing news input dorm and all news on this site
    news = ''
    m_field = '\n'.join(make_elem('textarea','Расскажите что-нибудь...',id = 'news_field',maxlength=200,onfocus='n_foc()'))
    m_button='\n'.join(make_elem('button','Отправить',onclick='send_news()',clas='send_btn'))
    picrelated='\n'.join(make_elem('input','',type='file',id='dl_picrel',accept='image/jpeg'))
    news_inp_field = '\n'.join(make_elem('div',m_field+'<br>'+m_button+picrelated,clas='news'))
    news+=news_inp_field
    db = sqlite3.connect('users.db')
    cur = db.cursor()
    cur.execute('SELECT * FROM news')
    allnews = cur.fetchall()
    allnews.reverse()
    for i in allnews:
        cur.execute('SELECT fname,sname FROM users WHERE name =?',(i[0],))
        zname = ' '.join(cur.fetchone())
        p_time = time.strftime('   %d/%m/%y, %H:%M',time.localtime(i[3]))
        top = '\n'.join(make_elem('a',zname+'<div class = "n_date">'+p_time+'</div>'))
        top+= '\n'.join(make_elem('hr',''))
        cont = '\n'.join(make_elem('p',i[1],clas='pnews'))
        cont = top+cont
        if(i[2]!='noimg'):
            cont+='\n'.join(make_elem('img','',src=i[2],width=100))
        news += '\n'.join(make_elem('div',cont,clas='news'))
    db.close()
    return(news)

def make_news_page(u_name):#makes main page, with messages, news, users and friends
    db = sqlite3.connect('users.db')
    cur = db.cursor()
    cur.execute('SELECT fname,sname FROM users WHERE name =?',(u_name,))
    zname = ' '.join(cur.fetchone())
    head = make_head(zname,u_name)
    topdivs = make_tops(zname)
    db.close()
    news_div = '\n'.join(make_elem('div',make_news_div(),id = 'news_div'))
    users = '\n'.join(make_elem('div',make_users_list(u_name),clas='u_list'))
    friends = '\n'.join(make_elem('div',make_friends_list(u_name),clas='f_list'))
    workspace = '\n'.join(make_elem('div','ffff',id='wspace'))
    m_header = '\n'.join(make_elem('p','Ваша переписка с ',id = 'm_header'))
    msg_cont = '\n'.join(make_elem('div','',id='msg_cont'))
    m_field = '\n'.join(make_elem('input','',id = 'msg_field'))
    m_button='\n'.join(make_elem('button','Отправить',onclick='send_msg()',clas='send_btn'))+'<br>'
    messages = '\n'.join(make_elem('div',m_header+msg_cont+m_field+m_button,id='messages'))
	
    body = '\n'.join(make_elem('body',topdivs+news_div+users+friends+workspace+messages))    
    return('\n'.join(make_elem('html',head+body)))




#LOGIN

def make_login_form(is_hi):#makes login form and writes greeting or 'incorrect login/password'
    if(is_hi==1):
        hi = '\n'.join(make_elem('p',HELLO_MSG))
    else:
        hi = '\n'.join(make_elem('p',WRONG_LOGPWD,clas='warn'))
    inp_name = '\n'.join(make_elem('input','Логин<br>',name='user'))
    inp_pass = '\n'.join(make_elem('input','Пароль<br>',type='password',name='pwd'))
    inp_login = '\n'.join(make_elem('input','',type='submit'))
    fcont = inp_name+inp_pass+inp_login
    login_form = '\n'.join(make_elem('form',fcont,action='login.py',enctype='application/x-www-form-urlencoded',method='POST'))
    forgot = '<br>'+'\n'.join(make_elem('a','Регистрация',href='register.py',clas='link'))
    div_login = '\n'.join(make_elem('div',hi+login_form+forgot,clas='login'))
    return div_login


def make_login_page(is_hi):#makes page with lofin form, head etc
    head = make_head('Гость','heh')
    tops = make_tops('Гость')
    div_login = make_login_form(is_hi)
    body = '\n'.join(make_elem('body',tops+div_login))
    html = '\n'.join(make_elem('html',head+body))
    return(html)

#REGISTER

def make_reg_form(wrong):#makes register form if wrong==1 it writes 'this login is not vacant'
    if(wrong):
        msg = '\n'.join(make_elem('p','Этот логин занят', clas = 'warn'))
    else:
        msg = ''
    inp_login = '\n'.join(make_elem('input','Логин<br>',name='user',required = '1',pattern='[A-Za-z_]{3,}'))#login must be longer than 3 symbols, and should content latin symbols and '_'
    inp_pass = '\n'.join(make_elem('input','Пароль<br>',type='password',name='pwd',required = '1'))
    devider = '\n'.join(make_elem('p','Личные данные:<br>'))
    inp_name = '\n'.join(make_elem('input','Ваше имя<br>',name = 'fname'))
    inp_sname = '\n'.join(make_elem('input','Ваша фамилия<br>', name = 'sname'))
    o_sex = '\n'.join(make_elem('p','Ваш пол:<br>'))
    inp_sex = '\n'.join(make_elem('input','М',type='radio',name='sex',value='male'))
    inp_sex+= '\n'.join(make_elem('input','Ж',type='radio',name='sex',value='female'))
    inp_logon = '\n'.join(make_elem('input','',type = 'submit'))
    
    fcont = msg+inp_login+inp_pass+devider+inp_name+inp_sname+o_sex+inp_sex+inp_logon
    
    reg_form = '\n'.join(make_elem('form',fcont,action='reg_save.py',\
                                   enctype='application/x-www-form-urlencoded',\
                                   method='POST'))#sends you to reg_save.py
    div_register = '\n'.join(make_elem('div',reg_form,clas='login'))
    return(div_register)
    
def make_reg_page(wrong):#makes register page with head, register form etc
    head = make_head('Регистрация','heh')
    tops = make_tops('Новый пользователь')
    div_reg = make_reg_form(wrong)
    body = '\n'.join(make_elem('body',tops+div_reg))
    html = '\n'.join(make_elem('html',head+body))
    return(html)
