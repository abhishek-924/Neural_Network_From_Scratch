from uwimg import *
import time
import sys
# import pandas as pd

def softmax_model(inputs, outputs):
    l = [make_layer(inputs, outputs, SOFTMAX)]
    return make_model(l)

def neural_net(inputs, outputs):
    # print (inputs)
    l = [make_layer(inputs, 16, RELU),
    		# make_layer(32, 16,RELU),
		#make_layer(16, 8, RELU),
            make_layer(16, outputs, SOFTMAX)]


    # for i in range(len(l)):
    # 	print_matrix(l[i].w)


    # Put these layers w varibale in a dataframe
    # for i in range len(l):
    # df =  pd.Dataframe(l[0].w)
    # df.to_csv('layer1.csv')

    # return 
    return make_model(l)

def save_to_file(filepath, process_to_run):

	orig_stdout = sys.stdout
	with open('filepath', 'w') as f:
		sys.stdout = f

		process_to_run

		sys.stdout = orig_stdout
		f.close()

def neural_on_mnist_dataset():
	start_time = time.time()
	print("loading data...")
	train_file_path = "mnist.train"
	labels_path = "mnist.labels"
	test_file_path = "mnist.test"

	train = load_classification_data(c_char_p(train_file_path.encode('utf-8')), c_char_p(labels_path.encode('utf-8')), 1)
	test  = load_classification_data(c_char_p(test_file_path.encode('utf-8')),c_char_p(labels_path.encode('utf-8')) , 1)
	print("Loading Data done")
	print()

	print("training model...")
	batch = 128
	iters = 3000
	rate = .01
	momentum = .9
	decay = .0005

	m = neural_net(train.X.cols, train.y.cols)            
	# print(train.X.cols, train.y.cols)						# 785, 10
	train_model(m, train, batch, iters, rate, momentum, decay)
	print("Training done")
	training_time = time.time()
	print('Training Ttime took {}'.format(training_time - start_time))

	testing_time_start = time.time()
	print("evaluating model...")
	print("training accuracy: %f", accuracy_model(m, train))
	print("test accuracy:     %f", accuracy_model(m, test))
	testing_time_ends = time.time()

	print('Testing took {}'.format(testing_time_ends - testing_time_start))

	print('Total Time Taken = {}'.format(testing_time_ends - start_time))

if __name__ == "__main__":
	save_to_file("results/mnist_Relu_Activation", neural_on_mnist_dataset())
	# train_file_path = "mnist.train"
	# labels_path = "mnist.labels"
	# test_file_path = "mnist.test"
	# train = load_classification_data(c_char_p(train_file_path.encode('utf-8')), c_char_p(labels_path.encode('utf-8')), 1)
	# test  = load_classification_data(c_char_p(test_file_path.encode('utf-8')),c_char_p(labels_path.encode('utf-8')) , 1)

	# print_matrix(neural_net(train.X.cols, train.y.cols)[0])
	
