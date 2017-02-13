from flask.ext.wtf import Form, validators
from wtforms.fields import TextField, TextAreaField, SubmitField
import wtforms


class ContactForm(Form):
    name = TextField("Name", [wtforms.validators.Required('Please enter your name')])
    email = TextField("Email", [wtforms.validators.Required('Please enter your email'), wtforms.validators.Email()])
    subject = TextField("Subject", [wtforms.validators.Required('Please enter a subject')])
    message = TextAreaField("Message", [wtforms.validators.Required('Please enter a message')])
    submit = SubmitField("Send")
    flash('All fields are required.')
    return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='imauld@gmail.com', recipients=['imauld@gmail.com'])
            msg.body = """From: %s &lt;%s&gt; %s""" % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)