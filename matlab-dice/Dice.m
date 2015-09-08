function Dice(n)
    figure
    hold 
    axis off
    rectangle('Po', [0 0 4 4], 'F', 'k', 'Cu', .1)
    spy([1 9 3 
        5 k - mod(n, 2) 5
        3 9 1] < n, 90, 'w')
