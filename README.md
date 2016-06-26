# fftphasealigner
Automatically exported from code.google.com/p/fftphasealigner


Images for illusstrative purposes.
[img]https://abload.de/img/fpa1_tncijm7.jpg[/img]
[img]http://abload.de/img/fpa2_tnj3jbm.jpg[/img]

FFT abstraction levels (ignore the here)
[img]http://abload.de/img/fftdecompositionnsj8t.jpg[/img]

You have a lotta vocals + instros. Trouble is, most of them don't line up & invert cleanly. This is where FPA comes in. The aim is, to use FPA to phase align (or angle align) the instro to the vocal, so that you get a usable result with polarity inversion (& maybe FFT postprocessing) afterwards. It does this by doing a FFT and then aligning every frequency band in $FFT_SIZE and then iFFT. So that all the frequencies are MUST GAY aligned.

I decided to implement this in JSFX/Reaper because it slides easily into my workflow like a piece of bread with butter side down on a hot oven tray which is warm/hot. Unfortunately, it was not totally succesful due to PDC/memory management issues.

There is evidence of it changing the phase. The algorithm is sound (check the specs/pseudocode). But all it does atm is smash transients (although with the amount of CPU it uses there are better ways to smash transients).

I might try again in the future in pythong/C++, and my endeavours with FFT in  pythong are usully far more successful (c above)

So if anywan wants to poke it, go ahead.

There are some things which come excruciatingly close then diverge, like hyperbola pictures on  certain site/s run by the cheezburger network.

DTS Neural DOwnmix (waves edition) aligns phases, then downmixes them. FFTing the original material out is not gonna end very well (i tried).

Pi Mixer by sound radix, it claims to phase/align things. I tried it, and it doesn't really work, because its not multiband. I wasted a while testing this. Voxengo PHA-979 is also not multiband, AND it requires you to know the phase/angle shift (which we don't, and it changes all the time)

There are also manual phase aligners. They still make them,  like waves & SSL X-phase. THIS IS $CURRENT_YEAR. Auto-phase aligners (from say, meldaproduction) exist already.
