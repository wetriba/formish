import tempfile
import os.path
import uuid, magic

class TempFileHandler(object):
    """
    File handler for formish file upload support.
    Allows use of python tempfile module to store file
    """

    def __init__(self, default_url=None,
                 resource_root='/filehandler',urlfactory=None):
        self.default_url = default_url
        self.resource_root = resource_root
        self.urlfactory = urlfactory

    def store_file(self, fs):
        fileno, filename = tempfile.mkstemp(suffix='%s-%s'%(uuid.uuid4().hex,fs.filename))
        fp = os.fdopen(fileno, 'wb')
        fp.write(fs.value)
        fp.close()
        prefix = tempfile.gettempprefix()
        tempdir = tempfile.gettempdir()
        filename = ''.join( filename[(len(tempdir)+len(prefix)+1):] )
        return filename

    def get_url_for_file(self, object):
        if self.urlfactory is not None:
            return self.urlfactory(object)
        if id is None:
            return self.default_url.replace(' ','+')
        else:
            return '%s/%s'%(self.resource_root,object)
        
    def get_path_for_file(self, filename):
        prefix = tempfile.gettempprefix()
        tempdir = tempfile.gettempdir()
        return '%s/%s%s'%(tempdir,prefix,filename)

    def get_mimetype(self, filename):
        prefix = tempfile.gettempprefix()
        tempdir = tempfile.gettempdir()
        mimetype = magic.from_file('%s/%s%s'%(tempdir,prefix,filename),mime=True)
        return mimetype or 'application/octet-stream'


class FileHandlerMinimal(object):
    """
    Example of File handler for formish file upload support.
    """

    resource_root = 'filehandler'

    def __init__(self, default_url=None):
        self.default_url = default_url

    def store_file(self, fs):
        """
        Method to store a file 
        """

    def get_url_for_file(self, data):
        """
        Method to get a url for the defaul file or the latest stored file
        """
        
    def get_path_for_file(self, filename):
        """
        Method to get a path for a file on disk
        """