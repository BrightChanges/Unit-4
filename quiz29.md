### Quiz 29


#### Solution

##### Flow Diagram:
![](https://github.com/BrightChanges/Unit-4/blob/main/IMG_0320.jpg)

##### Codes:

```.py

# You are trying to repair an LED strip made of N LEDs. You test M sections of the strip.
# For each one (inclusive range) write down the LEDs that were tested, and the result.
# Using your test results, output a string representing the condition of your LED strip.
# First LED is 0.

class quiz29():

    def __init__(self, N, M, results):
        self.N = N
        self.M = M
        self.results = results

    def LED(self):

        out = []
        out_string = ""

        for i in range(self.N):
            out.append("?")

        for i in range(len(self.results)):

            validator_output = ""

            LED_string = self.results[i].split(":")
            LED_range = LED_string[0].split("-")

            LED_range_start = LED_range[0]
            LED_range_end = LED_range[1]

            Validator = LED_string[1].split("-")

            #VERY IMPORTANT LINE OF CODE BELOW:
            #It helps convert an element in a list to a string
            #,which we can then use for logical comparison
            #later on
            Validator = str(Validator[0])


            if Validator == "PASS":
                validator_output = "V"

            elif Validator == "FAIL":
                validator_output = "X"


            for x in range(int(LED_range_start), int(LED_range_end) + 1):
                out[x] = validator_output

        for i in range(len(out)):
            out_string += out[i]

        print(out_string)


test1 = quiz29(10, 2, ["3-4:PASS", "6-7:PASS"])
test1.LED()

test2 = quiz29(10, 2, ["1-2:PASS", "5-6:PASS"])
test2.LED()

test3 = quiz29(8, 3, ["1-1:PASS", "3-3:FAIL", "7-7:FAIL"])
test3.LED()

test4 = quiz29(12, 3, ["1-5:PASS", "0-0:FAIL", "6-11:PASS"])
test4.LED()

```

##### Testing:

![](https://github.com/BrightChanges/Unit-4/blob/main/Screen%20Shot%200003-04-09%20at%2017.53.52.png)
