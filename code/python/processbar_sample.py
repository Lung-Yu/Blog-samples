import time
import progressbar

_widgets = ['[',progressbar.Timer(),']\t',
            progressbar.Percentage(),'\t'
            '[',progressbar.Bar('█'),']\t',
            progressbar.ETA()]

bar = progressbar.ProgressBar(widgets=_widgets)


# for i in bar(range(100)):
#     time.sleep(0.1)

def run_processbar_by_samples(RUN_SAMPLE_COUNT):
    bar.maxval = RUN_SAMPLE_COUNT
    bar.start()

    for i in range(RUN_SAMPLE_COUNT):
        # to do something
        time.sleep(0.01)
        bar.update(i+1)

    bar.finish()

def main():
    run_processbar_by_samples(999)

if __name__ == "__main__":
    main()