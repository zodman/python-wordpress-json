import wordpress_json
import io
import tempfile
import base64

PIXEL_GIF_DATA = base64.b64decode("""
R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7
""".strip())

def test_list_post():
    wp = wordpress_json.WordpressJsonWrapper("http://192.168.99.100:8080/wp-json/wp/v2","root","root")
    resp = wp.get_posts()
    assert len(resp)>0
def test_create_post():
    wp = wordpress_json.WordpressJsonWrapper("http://192.168.99.100:8080/wp-json/wp/v2","root","root")
    resp = wp.create_post(data=dict(title="foobar", content="content",excerpt="foobar"))    
    assert "id" in resp

def test_create_media():
    wp = wordpress_json.WordpressJsonWrapper("http://192.168.99.100:8080/wp-json/wp/v2","root","root")
    fopen, fpath = tempfile.mkstemp(suffix=".gif")
    with open(fpath,"wb") as fopen:
        fopen.write(PIXEL_GIF_DATA)
    #assert False, fpath
    files = {'file': ("foo.gif", open(fpath),'image/gif')}
    resp = wp._request('create_media',files=files)  
    assert "source_url" in resp


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-vv', '--with-doctest'])