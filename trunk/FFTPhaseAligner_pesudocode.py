FFT Phase Aligner

use $pi?

fftsize=4096


fft of 1&2, 3&4, stored in fft1-4

get magnitude of in1&2, store in array

#compute mags of 12

#it seems that most FFT JSFX plugins in R combine ch1&2 into one blob to be fft'd (as an optimization?)
#it may be fine for their purposes, but since i'm shifting phase, that may not be a good idea. Also, i try to keep FFTs of different channels separate for clarity.

for(i in fftsize):
	Magnitudes12[i]=sqrt(re^2+im^2)

	Magnitudes1[i]=sqrt(fft1[i*2]^2+fft1[i*2+1])#JS ver, FFT in JSFX is even=Re , odd=Im?
	Magnitudes2[i]=sqrt(fft2[i*2]^2+fft2[i*2+1])#JS ver, FFT in JSFX is even=Re , odd=Im?
	Magnitudes3[i]=sqrt(fft3[i*2]^2+fft3[i*2+1])#JS ver, FFT in JSFX is even=Re , odd=Im?
	Magnitudes4[i]=sqrt(fft4[i*2]^2+fft4[i*2+1])#JS ver, FFT in JSFX is even=Re , odd=Im?

get angle of in3&4, store in Angles34

#compute angles of 34
for (i in fftsize):
	Angles34[i]=arcsin(im/Magnitudes34[i])
	if(im<0):
		Angles34[i]=Angles34[i]*-1
	!!!RADIANS HANDLING

#Reconstruct in1&2 using Magnitudes12 & Angles34 
for (i in fftsize):
	Reconstructed12[i]=Magnitudes12[i]+Angles34[i]



ifft 1&2