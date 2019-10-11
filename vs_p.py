from fgclient import FgClient
c = FgClient()
c.ap_pitch_off()

kk = 0
error = 0
err_sum = 0
while True:
  kk+=1
  c.tic()
  if kk>10:
    vs_des = 5.0
  else:
    vs_des = 0.0
  vs = c.vertical_speed_fps()
  error = vs_des - vs
  err_sum += error
  c.set_elevator(-0.03*(error) - 0.005*err_sum)
  print(vs)
  c.toc(0.5)
