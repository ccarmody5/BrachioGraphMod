from brachiograph import BrachioGraph
import logging, time, datetime, sys

test_filename = "test.json"
startTime = time.localtime()

# angles in degrees and corresponding pulse-widths for the two arm servos
servo_1_angle_pws1 = [
    [-162, 2470],
    [-144, 2250],
    [-126, 2050],
    [-108, 1860],
    [ -90, 1690],
    [ -72, 1530],
    [ -54, 1350],
    [ -36, 1190],
    [ -18, 1010],
    [   0,  840],
    [  18,  640],
]

servo_2_angle_pws2 = [
    [  0,  660],
    [ 18,  840],
    [ 36, 1030],
    [ 54, 1180],
    [ 72, 1340],
    [ 90, 1490],
    [108, 1640],
    [126, 1830],
    [144, 2000],
    [162, 2200],
    [180, 2410],
]

try:
    filename = sys.argv[1]
except:
    filename = test_filename

bg = BrachioGraph(inner_arm=8,outer_arm=9,bounds=(-6,5,6,15),filename=filename)

def main():
    try:
        bg.plot_file("images/" + filename)
    except:
        logging.error('ERROR', exc_info=True)
        logging.info(runTime(startTime))
        print('ERROR - Program Exiting!')
        exit()

    logging.info('File Complete!')
    logging.info(str(runTime(startTime)) + '\n')

''' ***********************************************************************************************************************'''
''' ****************************************************** run time *******************************************************'''
''' ***********************************************************************************************************************'''
'''
' Get program run time
'''
def runTime(startTime):
    logging.debug('runTime()')
    
    t1 = time.mktime(startTime)
    t2 = time.mktime(time.localtime())

    return datetime.timedelta(seconds=t2-t1)
	
main = main()