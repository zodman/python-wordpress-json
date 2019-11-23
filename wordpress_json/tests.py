import wordpress_json
def test_list_post():
    wp = wordpress_json.WordpressJsonWrapper("http://192.168.99.100:8080/wp-json/wp/v2","root","root")
    resp = wp.get_posts()
    assert len(resp)>0

if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-vv', '--with-doctest'])