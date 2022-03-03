# phabro-rpios
OS level scripts handling communication and interaction between RaspberryPi and PCB1&amp;2

Handover:
- Well documented code
- 4 separate python scripts
- 1 simple php/js website (local) with py script-based^ interaction

Hardware (used):
- RaspberryPi 4B 8G (RPI)
- 2 custom developed PCBs (PCB1 & PCB2) (attachment)
-- These boards are routing signals (hardware-wise) from peripherals connected on PCB2 over PCB1 to RPI (GPIO [LED WS2812B, buttons, PWM-fan, BMS])

Software (used):
- Raspbian/Debian :latest
- apache2, mysql, php7.x (:latest)
- python 3.x (:latest)
- cronjobs

Necessities:
- Most evaluated methods/libraries
-- Not necessarily latest but most stable releases


TASK A: Python Script 1
- I/O button [GPIO]
- I/O LED [GPIO]
- Reset button [GPIO]
- BMS shutdown [GPIO]
- PWM-FAN control [GPIO]

TASK B: 3 Python Scripts
- 4 custom buttons [GPIO]
- LED WS2812B [GPIO]

TASK C: Rudimentary PHP/JS site displaying state of
- 4 custom buttons [TASK B]

@ the bottom you'lll find an elaborated and detailed task-overview


About the project:
I'm webdesign-freelancer myself and solopreneur on this project; I'd prefer a longer collaboration, this is just the first and smallest chunk of the project and there will follow. Testing waters. Not loosing any time and find the right coworker right away. It is NOT necessary for you to know the other chunks as the SRS is established & split.

What I'm looking for in your application:
- Similiar, accomplished projects
- Short description how you'd solve (methods/libraries) the tasks A/B/C
- Your hourly pay and an estimate of max. hours needed (!)
- Budgetcap TASK A/B/C (!)
- Timetable


TASK Descriptions:
:Pins are marked as P with their actual numerical position (1-40) on the RPI-GPIO header (attachment)
:Tasks are splitted in subtasks/functions (FN#)



TASK A (1 script preferred)
FN1 - I/O Button [P7]
> Sends shutdown-signal to RPI
> Logs the event to a central $LOG-file

FN2 - I/O LED [P35]
> Shows the state of the RPI (active=on, blinking=shutdown/restart, inactive=off)

FN3 - Reset Button [P5]
> Sends restart-signal to RPI / Wakes RPI from halt-state
> Logs the events to a central $LOG-file

FN4 - BMS Shutdown [P36]
> If the signal on the pin goes to '0'/low > send shutdown-signal to RPI
> Logs the event to a central $LOG-file

FN5 - PWM-FAN control [P12, P14(GND)]
> Temperatur controlled PWM-FAN control
>> 39°C=0% / 40°C=10% / 45°C=25% / 50°C=50% / 55°C=75% / 60°C=100%
> Logs temperature-spike with timestamp to $LOG (only if easily feasible)



TASK B (3 scripts preferred)
FN1 - 4 custom buttons (Button 1,2,3,4) [P11, P13, P15, P16]
> These buttons should interact with the website through x library and via js
>> While pressed they interact with the led-strip
>>> Buttons should react on normal push behaviour
>>> Button 1 is the exemption as it needs x sec to react

FN2 - LED WS2812B [P18]
> The first $20% should have $color
> The other $80% should have $color
> The entire led-strip should be dimmed $40% between $hours

> When a button [FN1] is pressed $% light up
>> Button 1 the first $5% of the led-strip
>> Button 2 $5-10% of the led-strip
>> Button 3 $10-15% of the led-strip
>> Button 4 $5-20% of the led-strip
> Buttons 2,3,4 should 'pulse'/light-up its corresponding $% when pressed
> Button 1 should keep 'light-on' its corresponding $% and fill-up* the led-strip starting from $20% to $100% fluidly in x sec in $color

:The $variabels and $LOG should be easy to adjust, on a separate file would be best; declared in the head of the scripts also viable. Please state in your application how you'd do it and insert 'ferdi' so I can filter out participants.


TASK C (PHP/JS site on standard lamp-stack displaying state of Buttons (attachment))
:rudimentary simple website
:buttons change values on site through js /i.e. bg-color
> Each button of TASK B FN1 changes a <div> on the site
> Button 1 also changes another <div> on the bottom which resembles the led-progress*^ and shows %-value
