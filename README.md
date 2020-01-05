# Slack Weather

Update your Slack status every 30 minutes, using Github Actions and the Dark Sky API.    

<img src='https://github.com/br-g/slack-weather/blob/master/screenshot.png' alt='screenshot' width='230'/>

## Setup


#### 1) Fork this repository

#### 2) Set parameters

Open `https://github.com/<MY_GITHUB_ID>/slack-weather/settings/secrets` (replace `<MY_GITHUB_ID>`).   
Add the following secrets:

| Name            | Value                                                                                               |
| --------------- |-----------------------------------------------------------------------------------------------------|
| `DARKSKY_TOKEN` | a Dark Sky API token (get one [here](https://darksky.net/dev))                                      |
| `SLACK_TOKEN`   | a Slack token (get one [here](https://api.slack.com/custom-integrations/legacy-tokens#legacy-info)) |
| `LATITUDE`      | your latitude (for example: `48.856613`)                                                            |
| `LONGITUDE`     | your longitude (for example: `2.352222`)                                                            |
| `UNITS`         | `si` (temperatures in celsius) or `us` (temperatures in fahrenheit)                                 |

#### 3) Enable actions

Open `https://github.com/<MY_GITHUB_ID>/slack-weather/actions`(replace `<MY_GITHUB_ID>`).   
Click the green button "I understand my workflows, go ahead and run them".

#### 4) Push something to the master branch

For example, make a minor edit to this README.    
This is a necessary step for triggering the actions.


## Cost

An execution of the Github action takes about 10 seconds.    
With 2 executions per hour (the default value), this adds up to 250 minutes per month.    
As of January 2020, GitHub Free and GitHub Pro provide respectively 2000 and 3000 minutes free.
