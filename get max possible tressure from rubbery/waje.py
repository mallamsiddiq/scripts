import unittest


# the main fuction to get maximum possible bag raid
def trasv_to_max_bag(arr): 
    
    arr_length = len(arr) # store lenth of array
    if arr_length <=1:
        return arr[0] if arr_length>0 else 0                # avoid index out of range
    max_raid_0 = arr[0]                                     # current maximum raid possible at 1st house 
    max_raid_1 = max(arr[1],arr[0])                         # current maximum raid possible at 2nd house 

    for i in (range(2,arr_length)):                         #
        prev_max_raid=max_raid_1                            # keep maximum raid possible at current house
        max_raid_1=max((max_raid_0+arr[i]),max_raid_1)      # evalute and update maximum raid possible current house
        max_raid_0=prev_max_raid                            # keep track of current maximum raid for next house
    return max_raid_1   

# testing section


if __name__=='__main__':
	class WidgetTestCase(unittest.TestCase):

		def checkCase(self,arr,result):
			self.assertEqual(trasv_to_max_bag(arr),result)
			print('TEST {}==>>{}, PASSED'.format(arr,result))

		def test_max_bag(self):
			self.checkCase([2, 5, 1, 3,6, 2, 4],15)
			self.checkCase([2, 10, 14, 8, 1],18)

	unittest.main() 