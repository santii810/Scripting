import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import Encoders

class Email:
    emisor = "smtp.sgomez@gmail.com"
    receptor = "santii810@hotmail.com"
    asunto = "Python Email"
    text = ""
    fileName = ""
    password = 'santi36462'

    def send_mail(self):
        msg = MIMEMultipart()
        msg['From'] = self.receptor
        msg['To'] = self.emisor
        msg['Subject'] = self.asunto

        # adjuntar fichero
        if(self.fileName != ""):
            adjunto = MIMEBase('application', "octet-stream")
            adjunto.set_payload(open(self.fileName, "rb").read())
            Encoders.encode_base64(adjunto)
            adjunto.add_header('Content-Disposition', 'attachment; filename="%s"'
                               % os.path.basename(self.fileName))
            msg.attach(adjunto)

        # Autenticado
        smpt = smtplib.SMTP('smtp.gmail.com', 587)
        smpt.ehlo()
        smpt.starttls()
        smpt.ehlo()
        smpt.login(self.emisor, self.password)

        smpt.sendmail(self.emisor, self.receptor, msg.as_string(), self.text)
        smpt.close()
