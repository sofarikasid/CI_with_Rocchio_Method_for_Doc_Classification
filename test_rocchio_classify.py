from rocchio_classify import * 

def test_Rocchio_Classify_train():
    output = ({'sport': 2287.7827694079697,'tech': 2992.481913061464,'business': 2642.007948511889,'politics': 2921.910847373684,'entertainment': 1941.8346994530714})
    expected_output=Rocchio_Classify_train(train, train_label)
    assert output == expected_output[0]

def test_run_rocchio():
    output= 'business'
    assert output == run_roochio(Rocchio_Classify_train, train, train_label, test, set_index=True, k=0)
