# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.web
import sqlite3 as sql
import string
import os

# Helpers
class Base(tornado.web.RequestHandler):
    login = ''
    BaseUrl = 'http://static.ecglobalpanelcorp.com/'
    def get_current_user(self):
        return self.get_secure_cookie('auth')
        
    def AbreSessao(self, l):
        if not self.get_secure_cookie('auth'):
            self.set_secure_cookie('auth', l)
        return True
    
    def ChecaUsuario(l, s, self):
        #self.login = l
        return True
        '''
        con = sql.connect('files.db')
        cur = con.cursor()
        sql = 'SELECT COUNT(*) FROM `users` WHERE login = `%s` AND senha = `%s`;' % (l, s)
        cur.execute(sql)
        print len(cur.fetchall())
        if len(cur.fetchall()) == 1:
            con.close()
            self.l = l
            return True
        '''
        
    def Header(self):
        return '''
<!DOCTYPE html>
<html lang="en"><!-- Source is http://themes.vivantdesigns.com/neueadmin2/dashboard.html -->
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>File Manager - eCGroup</title>

        <link rel="stylesheet" media="screen" href="static/estilo/reset.css" />
        <link rel="stylesheet" media="screen" href="static/estilo/grid.css" />
        <link rel="stylesheet" media="screen" href="static/estilo/style.css" />
        <link rel="stylesheet" media="screen" href="static/estilo/messages.css" />
        <link rel="stylesheet" media="screen" href="static/estilo/forms.css" />
        <link rel="stylesheet" media="screen" href="static/estilo/tables.css" />

        <!--[if lt IE 8]>
        <link rel="stylesheet" media="screen" href="static/estilo/ie.css" />
        <![endif]-->

        <!--[if lt IE 9]>
        <script type="text/javascript" src="static/estilo/html5.js"></script>
        <script type="text/javascript" src="static/estilo/PIE.js"></script>
        <script type="text/javascript" src="static/estilo/IE9.js"></script>
        <script type="text/javascript" src="static/estilo/excanvas.js"></script>
        <![endif]-->

        <!-- jquerytools -->
        <script type="text/javascript" src="static/estilo/jquery.tools.min.js"></script>
        <script type="text/javascript" src="static/estilo/jquery.cookie.js"></script>
        <script type="text/javascript" src="static/estilo/jquery.ui.min.js"></script>
        <script type="text/javascript" src="static/estilo/jquery.tables.js"></script>
        <script type="text/javascript" src="static/estilo/jquery.flot.js"></script>

        <script type="text/javascript" src="static/estilo/global.js"></script>

        <!-- THIS SHOULD COME LAST -->
        <!--[if lt IE 9]>
        <script type="text/javascript" src="static/estilo/ie.js"></script>
        <![endif]-->   
        '''
    def Footer(self):
        return '''   
    <footer>
        <div id="footer-inner" class="container_8 clearfix">
            <div class="grid_8">
                <span class="fr"><a href="#">Documentation</a> | <a href="#">Feedback</a></span>Last account activity from 127.0.0.1 - <a href="#">Details</a> | &copy; 2010. All rights reserved. Theme design by VivantDesigns
            </div>
        </div>
    </footer>
</body>
</html>'''
        
    def CssLogin(self):
        return '''
        <style>
        * { margin: 0px; padding: 0px; } 
        body { font-family: sans-serif; font-size: 11px; background: #fff; } 
        div { padding: 20px; } 
        a { text-decoration: none; color: inherit; } 
        a:hover { border-bottom: 3px solid #888; } 
        #conteudo { clear: both; margin: 0px auto; } 
        .menu { width: 100px; height: 20px; margin: 10px 5px 0px 5px; display: inline-block; text-align: center; padding: 20px 5px; color: #888; font-weight: bold; font-size: 18px; } 
        input, select { margin: 5px 15px; padding: 5px 10px; } 
        textarea { margin: 5px 15px; padding: 15px; width: 380px; height: 180px; } 
        #tela_login { padding: 20px 20px 20px 100px; margin: 100px auto; width: 200px; height: 200px; border: 1px silver dotted; background: #fff url(static/escudo.png) no-repeat 20px 50px; } 
        .links { margin: 20px; background: url(../img/link.png) no-repeat; padding: 3px 35px; display: inline-block; }
        </style>
        '''
    
    def TelaLogin(self):
        return self.Header()+'''
        
        
<script> 
$(document).ready(function(){
    $.tools.validator.fn("#username", function(input, value) {
        return value!='Username' ? true : {     
            en: "Por Favor, preencha este campo."
        };
    });
    
    $.tools.validator.fn("#password", function(input, value) {
        return value!='Password' ? true : {     
            en: "Por Favor, preencha este campo."
        };
    });

    var form = $("#form").validator({ 
    	position: 'bottom left', 
    	offset: [5, 0],
    	messageClass:'form-error',
    	message: '<div><em/></div>' // em element is the arrow
    });
});
</script> 
</head>
<body class="login">
    <div class="login-box main-content">
      <header>
          <ul class="action-buttons clearfix fr">
              <li><a href="#" class="button button-gray"><span class="help"></span>Perdi minha senha</a></li>
          </ul>
          <h2>File Admin - Login</h2>
      </header>
    	<section>
    		<!--div class="message notice">Enter any letter and press Login</div-->
			<br />
			<p>
	    		<form id="form" action="/login" method="post" class="clearfix">
				<input type="text" id="login"  class="large" value="" name="login" required="required" placeholder="Usuário" />
                <input type="password" id="senha" class="large" value="" name="senha" required="required" placeholder="Senha" />
                <button class="large button button-gray fr" type="submit">Login</button>
			<br />
			<br />
			<br />
			</p>
		</form>
    	</section>
    </div>
</body>
        '''+self.Footer()

    def TelaUpload(self):
        return self.Header()+'''
<body>
    <div id="wrapper">
        <header>
            <div class="clearfix">

                <div class="clear"></div>
                <nav>
                    <ul class="clearfix">
                        <li class="active"><a href="dashboard.html">Dashboard</a></li>
                        <li><a href="forms.html">Enviar Arquivo</a></li>
                        <li class="fr action">
                            <a href="documentation/index.html" class="button button-orange help" rel="#overlay"><span class="help"></span>Sair</a>
                        </li>
                        
                        <!--li class="fr"><a href="#" class="arrow-down">administrator</a>
                            <ul>
                                <li><a href="#">Account</a></li>
                                <li><a href="#">Users</a></li>
                                <li><a href="#">Groups</a></li>
                                <li><a href="#">Sign out</a></li>
                            </ul>
                        </li-->
                    </ul>
                </nav>
            </div>
        </header>
        
        <section>
            <div class="container_8 clearfix">                

                <!-- Main Section -->

                <section class="main-section grid_8">

                    <!-- Statistics Section -->
                    <div class="main-content">
                        <header>
                            <ul class="action-buttons clearfix fr">
                                <li><a href="#" class="button button-gray no-text"><span class="wrench"></span></a></li>
                                <li><a href="documentation/index.html" class="button button-gray no-text help" rel="#overlay"><span class="help"></span></a></li>
                            </ul>
                            <h2>
                                Arquivos
                            </h2>
                        </header>
                        
                        
                        <section class="container_6 clearfix">
                                <div class="grid_4 clearfix">
                                    <header class="clearfix">
                                    <h3>Lista de Arquivos</h3>
                                    </header>
                                    <p>
                                        Copie o link do ícone.
                                    </p>
                                    '''+self.TelaArquivos()+'''
                                </div>

                                <!-- Progress Bars -->
                                <div class="grid_2">
                                    <h3>Enviar Arquivo</h3>
                                    <form action="/upload" method="POST" enctype="multipart/form-data" >
                                        <label for="arquivo">Arquivo</label>
                                        <input type="file" id="arquivo" name="arquivo" />
                                        <br />
                                        <input type="hidden" id="login" name="login" /><br /> <br /> 
                                        <input type="submit" value="Enviar" />
                                    </form>
                                    <!--h3>Estatísticas</h3>
                                    <table class="simple full">
                                        <tr>
                                            <td style="width: 30%">Quantidade de Arquivos</td><td style="width: 10%" class="ar">20/100</td><td style="width: 60%"><div class="progress progress-orange"><span style="width: 20%"><b>20%</b></span></div></td>
                                        </tr>
                                        <tr>
                                            <td>Espaço Utilizado</td><td class="ar">40/100</td><td><div class="progress progress-orange"><span style="width: 40%"><b>40%</b></span></div></td>
                                        </tr>
                                    </table-->
                                </div>
                                <!-- End Progress Bars -->
                        </section>
                    </div>
                    <!-- End Statistics Section -->
                </section>
                <!-- Main Section End -->
            </div>
        </section>
    </div>'''

    def TelaArquivos(self):
        con = sql.connect('files.db')
        cur = con.cursor()
        s = 'SELECT * FROM `files`;'
        cur.execute(s)
        s = cur.fetchall()
        r = ''
        for x in s:
            if len(x[5]) > 12 :
                n = x[5][0:12]+'...'
            else:
                n = x[5]
            r += '''<section>
                <div class="grid_1 alpha">
                <div class="widget black ac">
                <header><h2>'''+n+'''</h2></header>
                <section><img src="static/mimes/mp3.png" /></section>
            </div>
            </div>
            </section>'''
        con.close()
        return str(r)
    
    def GuardaArquivoBanco(self, u, t, n):
        con = sql.connect('files.db')
        cur = con.cursor()
        sql_str = 'INSERT INTO `files` (`url`, `dono`, `tipo`, `nome`) VALUES (\'%s\', \'%s\', \'%s\', \'%s\');' % (u, self.login, t, n)
        if cur.execute(sql_str):
            con.commit()
            con.close()
            return True
    
    def EscreveArquivo(self):
        f = open(self.request.files['arquivo'][0]['filename'], 'w')
        f.write(self.request.files['arquivo'][0]['body'])
        f.close()
        return True
    
    def getEmpresa(self):
        pass

    
# Views
class MainHandler(Base):
    @tornado.web.authenticated
    def get(self):
        self.write(self.TelaUpload())

class UploadHandler(Base):
    @tornado.web.authenticated
    def post(self):
        if self.EscreveArquivo() : 
            if self.GuardaArquivoBanco(self.BaseUrl, string.split(self.request.files['arquivo'][0]['filename'], '.')[1], self.request.files['arquivo'][0]['filename']):
                self.redirect('/')

class LoginHandler(Base):
    def get(self):
        self.write(self.TelaLogin())
    
    def post(self):
        self.login = self.get_argument('login')
        s = self.get_argument('senha')
        if self.ChecaUsuario(self.login, s):
            self.AbreSessao(self.login)
            self.redirect('/')

# Settings
settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'cookie_secret': '61hfghfghf5gEmGeJJFuYh7hfghf2fghfgh1o/Vo=',
    'login_url': '/login',
}

# Router
application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/login', LoginHandler),
    (r'/upload', UploadHandler),
], **settings)


# App
if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
