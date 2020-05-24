import time
import progressbar

_widgets = ['[',progressbar.Timer(),']\t',
            progressbar.Percentage(),'\t'
            '[',progressbar.Bar('█'),']\t',
            progressbar.ETA()]

bar = progressbar.ProgressBar(widgets=_widgets)

for i in bar(range(100)):
    time.sleep(0.1)