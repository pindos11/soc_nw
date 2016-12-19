function n_foc(){
	document.getElementById('news_field').value = ''
}


function logoff() {
	value = document.getElementsByTagName('head')[0].id
	var cookie_date = new Date ( 2003, 01, 15 );//куки на прошлое
      document.cookie = 'name' + "=" + escape(value) +
        "; expires=" + cookie_date.toGMTString()
	window.location.href = 'http://localhost:8000/cgi-bin/index.py'
}


function getXmlHttp(){
  var xmlhttp;
  try {
    xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");//если это микрософт браузер
  } catch (e) {
    try {
      xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (E) {
      xmlhttp = false;
    }
  }
  if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
    xmlhttp = new XMLHttpRequest();
  }
  return xmlhttp;
}

function updMsg(user){
	var req = getXmlHttp()//в остальных с запросами та же схема
	current = document.getElementsByTagName('head')[0].id
	req.onreadystatechange = function() {          
		if (req.readyState == 4) {  //если ответ пришел          			
			if(req.status == 200) { //и он 200
                 
				document.getElementById("msg_cont").innerHTML = req.responseText;//текст ответа куда надо
				document.getElementById("msg_field").value = ' '
			}			
		}
	}       
	req.open('POST', 'http://localhost:8000/cgi-bin/messagesAJAX.py', true);  //адрес запроса, это пост, так что только файл
	req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded', 'charset = utf-8')
	
	req.send('name='+current+'^^'+user); //везде разделитель два знака возведения в степень  
}

function updNews(){
	var req = getXmlHttp()
	current = document.getElementsByTagName('head')[0].id
	req.onreadystatechange = function() {          
		if (req.readyState == 4) {            			
			if(req.status == 200) { 
                 
				document.getElementById("news_div").innerHTML = req.responseText;
				document.getElementById("news_field").value = 'Расскажите что-нибудь...'
			}			
		}
	}       
	req.open('POST', 'http://localhost:8000/cgi-bin/getnewsAJAX.py', true);  
	req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded', 'charset = utf-8')
	
	req.send();   
}


function send_news(){
	message = document.getElementById("news_field").value
	sendr = document.getElementsByTagName('head')[0].id
	pic = document.getElementById("dl_picrel").files[0]
	if(typeof pic == 'undefined'){
		var req = getXmlHttp()
		req.onreadystatechange = function() {          
		if (req.readyState == 4) {            			
			if(req.status == 200) { 
                //alert(req.responseText) 
				updNews()
				}			
			}
		}       
		req.open('POST', 'http://localhost:8000/cgi-bin/sendnewsAJAX.py', true);  
		req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded', 'charset = utf-8')
		
		req.send('msg='+sendr+'^^'+message.replace(/</g,'').replace(/>/g,'').replace(/\n/g,'<br />')+'&pic=noimg');   
	}
	else{//в случае, если таки приложено изображение
		reader = new FileReader()
		reader.readAsDataURL(pic)
		reader.onloadend = function(e){//как только считается и переведется
			pic = reader.result
			var req = getXmlHttp()
			req.onreadystatechange = function() {          
			if (req.readyState == 4) {            			
				if(req.status == 200) { 
					//alert(req.responseText)
					updNews()
					}			
				}
			}       
			req.open('POST', 'http://localhost:8000/cgi-bin/sendnewsAJAX.py', true);  
			req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded', 'charset = utf-8')
			//alert(pic)
			req.send('msg='+sendr+'^^'+message.replace(/</g,'').replace(/>/g,'').replace(/\n/g,'<br />')+'&pic='+encodeURIComponent(pic));			
		}
	}
	
	
	
	

}

function send_msg(){
	message = document.getElementById("msg_field").value
	rec = document.getElementById("wspace").user_trget
	sendr = document.getElementsByTagName('head')[0].id
	
	var req = getXmlHttp()
	req.onreadystatechange = function() {          
		if (req.readyState == 4) {            			
			if(req.status == 200) { 
                 
				updMsg(rec)
			}			
		}
	}       
	req.open('POST', 'http://localhost:8000/cgi-bin/sendmsgAJAX.py', true);  
	req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded', 'charset = utf-8')
	
	req.send('msg='+sendr+'^^'+rec+'^^'+message.replace(/</g,'').replace(/>/g,''));   

}




function show_user_info(u_name,name){
	document.getElementById("wspace").style.visibility = 'visible'
	document.getElementById("wspace").user_trget = u_name
	z = name.split(' ')
	document.getElementById("wspace").innerHTML = '<p>'+z[0]+' '+z[1]
}

function show_msgs(user, u_name){
	document.getElementById("messages").style.visibility = 'visible'
	z = u_name.split(' ')
	document.getElementById("m_header").innerHTML='Ваша переписка с '+z[0]+':<hr>'
	updMsg(user)
	//var timerid = setInterval(function(){
	//	updMsg(user);
	//}, 3000);
	
}


function f_add(type) {
//if(type.id == document.getElementsByTagName('head')[0].id){
	//return}
	sendr = document.getElementsByTagName('head')[0].id
	var req = getXmlHttp()  	
	req.onreadystatechange = function() {          
		if (req.readyState == 4) { 
			if(req.status == 200) { 
                //alert(req.responseText) 
				window.location.href = 'http://localhost:8000/cgi-bin/index.py'
			}			
		}
	}   
	req.open('POST', 'http://localhost:8000/cgi-bin/addfriendAJAX.py', true);  
	req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded', 'charset = utf-8')
	
	req.send('usr='+sendr+'^^'+type.id);     
}


function sel(type) {
//if(type.id == document.getElementsByTagName('head')[0].id){
	//return}
	var req = getXmlHttp()  	
	req.onreadystatechange = function() {          
		if (req.readyState == 4) { 
			if(req.status == 200) { 
                //alert(req.responseText) 
				show_user_info(type.id,req.responseText);
				show_msgs(type.id, req.responseText);
			}			
		}
	}   
	req.open('POST', 'http://localhost:8000/cgi-bin/usershowAJAX.py', true);  
	req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded', 'charset = utf-8')
	
	req.send('name='+type.id);     
}
