from fgclient import FgClient
c = FgClient()
c.ap_pitch_vs()
c.ap_roll_off()
kk = 0
error = 0
err_sum = 0
kp = 0.005
ki = 0
kd = 0.05
dt = 0.5
first_hdg = c.heading_deg()
last_hdg = first_hdg
while True:
  kk+=1
  c.tic()
  if kk>1:
    head_des = first_hdg + 15
  else:
    head_des = first_hdg
  head = c.heading_deg()

  error = head_des - head
  err_sum += error

  err_deriv = (head - last_hdg)/dt 
  last_hdg = head
  c.set_aileron(kp*(error) - ki*err_sum - kd*err_deriv)
  print(head)
  c.toc(dt)
