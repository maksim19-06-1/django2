from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse

from scipy.optimize import linprog
import time
import numpy as np
import matplotlib.pyplot as plt

def home(request):

    start = time.time()
    C = (0.2,0.3) 
    A = [[-7,-3],[-5,-4],[-9,-2]] 
    b = [-1100,-900,-700] 
    x0_bounds = (0, None)
    x1_bounds = (0, None)
    res = linprog(C, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
    print(res)
    stop = time.time()
    print ("Time :")
    print(stop - start)


    x =  np.arange(0, res.x[0], 1)
    y =  (1100-7*x)/3

    plt.figure(figsize=(16, 8),dpi=100)
    axes = plt.gca()
    axes.set_xlim([0,res.x[0]+5])
    axes.set_ylim([-20,400])

    plt.plot(x,y)
    plt.fill_between(x,y, alpha=0.2)
    plt.text(20, 290, '7*x1+3*x2>=1100', rotation=-30 % 360)

    x2 =  np.arange(0, res.x[0], 1)
    y2 =  (900-5*x)/4
    plt.plot(x2,y2)
    plt.fill_between(x2,y2, alpha=0.2)
    plt.text(50, 150, '5*x1+4*x2>=900', rotation=-20 % 360)

    x3 =  np.arange(0, res.x[0], 1)
    y3 =  (700-9*x)/2
    plt.plot(x3,y3)
    plt.fill_between(x3,y3, alpha=0.2)
    plt.text(20, 210, '9*x1+2*x2>=700', rotation=-40 % 360)

    plt.plot(x, (C[0]*C[1]-np.abs(C[0])*x)/np.abs(C[1]), '--')
    plt.annotate('Level curve', xy=(2, 0), xytext=(2.5, 10), size='x-large', style="italic", arrowprops=dict(facecolor="gray",arrowstyle="fancy"))
    plt.plot(res.x[0], res.x[1], 'ro')
    plt.annotate('Xmin', xy=(res.x[0], 0), xytext=(res.x[0]-30, 100), size='x-large', style="italic", arrowprops=dict(facecolor="gray",arrowstyle="fancy"))


    x2=x[0:131]
    x3=x[130:185]
    plt.fill_between(x2, 400,(1100-7*x2)/3, color='#C0C0C0')
    plt.fill_between(x3, 400,(900-5*x3)/4, color='#C0C0C0')


    import os
    
    plt.title('Parts production problem', fontsize=15)
    plt.xlabel('x1', fontsize=12)
    plt.ylabel('X2', fontsize=12, color='black')
    #plt.savefig("D:/dj_en/first/lect1/static/images/paint.png", dpi=300)
    #plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/paint.png'), dpi=300)

  
    template_name=loader.get_template('index.html')
    args = {}
    args['v1'] = res.x[0]
    args['v2'] = res.x[1]
    args['v3'] = res.fun
    return TemplateResponse(request, template_name, args)


# Create your views here.
