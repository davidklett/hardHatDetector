import pickle
import requests
##dump the model into a file
##loading the model from the saved file

def predict_hardhat(image):
    with open('model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()
    x = model.predict(image)
    print(type(x))
    hardhat = x[0]
    return hardhat
        
#predict_hardhat('./test/hardhat2.png')
# url = "https://files-monday-com.s3.amazonaws.com/7521235/resources/144800772/hardhat2.png?response-content-disposition=attachment&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MPVJMFXPCFHVJDO%2F20201130%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201130T183852Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=7c0f0bd259f08be3f71988ebcea14ea0ab190083c3a65cbab91c0d0273a36b05"
# with open('model.bin', 'rb') as f_in:
#     model = pickle.load(f_in)
#     f_in.close()

#predict_hardhat('hardhat1.jpg')
