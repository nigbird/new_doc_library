from .models import Document
from django.core.mail import EmailMessage

def save_documents(validated_data):
    """
    Save multiple documents to the database.

    Parameters
    ----------
    validated_data : dict
        A dictionary containing the validated data, including the title and files.

    Returns
    -------

    list
        A list of Document instances that were created.
    """
    title = validated_data['title']
    files = validated_data['files']
    documents = []
    for file in files:
        document = Document.objects.create(title=title, file=file)
        documents.append(document)
    return documents

def send_file_email(sender_email, recipient_email, subject, message, file_path, file_name):
    """
    Send an email with the specified file attached.

    Parameters
    ----------
    sender_email : str
        The email address of the sender.
    recipient_email : str
        The email address of the recipient.
    subject : str
        The subject of the email.
    message : str
        The body of the email.
    file_path : str
        The path to the file to be attached.
    file_name : str
        The name of the file to be attached.

    Returns
    -------
    None
    """
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=sender_email,
        to=[recipient_email],
    )
    email.attach_file(file_path)
    email.send()
