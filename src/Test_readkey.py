import readkey

shared_keypad_queue = queue.Queue()

def fill_queue_keys(keys):
    for key in keys:
        shared_keypad_queue.put(key)

def test_ATMPIN_correct():
    card_no = 123456

    simulated_keys = ['1','2','3','4','5','6','#']
    fill_queue_keys(simulated_keys)
    result = ATMPIN(card_no)
    assert(result == True)

def test_ATMPIN_no_hashtag():
    card_no = 123456
    simulated_keys = ['1','2','3','4','5','6','7']
    fill_queue_keys(simulated_keys)
    result = ATMPIN(card_no)
    assert (result == False)
    
def test_ATMPIN_Len():
    card_no =123456
    simulated_keys = ['1','2','3','4','5','6','#','8']
    fill_queue_keys(simulated_keys)
    result = ATMPIN(card_no)
    assert (result == False)
    
