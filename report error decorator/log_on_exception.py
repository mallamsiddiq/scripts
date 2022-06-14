import logging

def log(utf8_string, tags,err_msg):
	logging.basicConfig(filename='reports with{}.log'.format(tags), level=logging.INFO)
	logging.info('opps!! error. {} on the decorated fuction {}()'.format(err_msg,utf8_string))

def log_on_exception(*tags):
	def inner(orig_func):
		def wrapper(*args,**kwargs):
			try:
				orig_func(*args,**kwargs)
			except Exception as e:
				log(orig_func.__name__,tags,e)
		return wrapper
	return inner
 

@log_on_exception('tag1', 'tag2')
def fn():
    raise Exception('Some message')

if __name__=='__main__':
	fn()
