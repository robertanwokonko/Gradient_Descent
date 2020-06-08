import numpy as np

def gradient_descent(x,y):
    """
    Gradient descent is an optimization algorithim thats finds
    the best fit line for a given training data set.

    This function uses an efficient approach
    when finding the best permutation and combination of 
    m & b in your cost function (In this case cost function 
    is Mean Squared Error(MSE))

    When taking the slope of a non-linear graph, use derivatives
    when taking the slope of a linear graph, use the equation of a straight line

    Arguments:
    x - a collection of n p-dimensional feature vectors
    y - a collection of observed responses.
    """

    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learningrate= 0.001

    for i in range(iterations):
        # (y = mx + b)
        y_predicted = m_curr * x + b_curr 
             
        dm = -(2/n)*sum(x*(y-y_predicted))
        db = -(2/n)*sum(y-y_predicted)

        # this step is to move towards your global minmum and update movements
        m_curr = m_curr - learningrate* dm
        b_curr = b_curr - learningrate* db
        print('m {}, b {}, iteration{}'.format(m_curr,b_curr,i))

# test data
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

#function call
gradient_descent(x,y)
