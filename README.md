# countdown

A very simple countdown timer, based on command line input.
Accepts a string, specifying the amount of time to run the timer for before playing an alarm sound upon completion.
Time will be displayed in the format ..HH:MM:SS
The input string can take a variety of time expressions, valid for days, hours, minutes and seconds.

## Example Input Strings

| String | Valid | Notes |
|---|---|---|
2d 3h 7m 2s| Yes | Standard format
2 days 3 hours 7 mins 2 secs | Yes | Mixed shorthands
2D 3H 7M 2S| No | Short form must be lowercase
2dys 3 hrs 7  mins 2     secs | Yes | Various spacings tolerated
3h 2d 2s 7m | Yes | Time need not be in  significance order

