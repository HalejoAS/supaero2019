xopt_sqp  = fmin_slsqp(cost_9,x0,f_eqcons=constraint_9,
                       callback=callback_9,
                       iprint=2, full_output=1)[0]
print '\n *** Xopt SQP  = ',xopt_sqp ,'\n\n\n\n'
