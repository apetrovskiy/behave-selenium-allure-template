# How to behave with Selenium #

This is a project template for using BDD style tests to test a web application.

The browser is driven by Selenium and performs BDD style steps defined using the [behave library][link0] for Python.

This template is designed to work with Python 3.5 on Windows 7+.



## Installation ##

### Pre-Requisites ###

Have installed at least one of:

+ Chrome
+ Firefox
+ Internet Explorer 

Additionally you must have Python 3.5 installed and set-up on the Path:

+ Install [Python 3.5 or above][link1] for Windows. 
+ Make sure Python is set in the Path (```Control Panel > System > Advanced System Settings >  Environment Variables``` and add ```C:\root\to\Python[version]\Scripts\```)

### Steps ###

1. Open a command prompt in the root of the project and call ```configure-virtual-env.bat```. This will set-up a virtual environment to avoid messing with the global level Python installation. Any errors encountered in the set-up will appear in the output from this script so make sure to read it if there are problems. 

3. Once run you should be able to type ```behave``` and it will run the single sample test. This should open Firefox and navigate to Wikipedia. 

## Configuration ##

### Changing the browser ###

Depending on the browser you have installed you can change the browser the test uses to run by changing the config in ```~\src\Config.ini```:
	
	[selenium]
	driver = Firefox

The possible values are currently:

+ Firefox
+ Chrome
+ Internet Explorer

### Changing cookie clearing behaviour ###

The project is set up to clear cookies from the browser session based on the setting in Config.ini
	
	[selenium]
	driver = Chrome
	clear_cookies = lifetime

The possible values are:

+ step - clears cookies after each individual step is run
+ feature - clears cookies after all scenarios in a feature file are run
+ lifetime - clears cookies only after an entire test run finishes
+ scenario - clears cookies after each full Given/When/Then scenario

### Using custom configuration ###

You can add your own settings to Config.ini and easily access them from your step definitions. For example, in Config.ini:

	[tests]
	url = http://wikipedia.org

Then in steps/wikipedia.py:

	from helpers import configuration
	
	@when("I am on the homepage")
	def step_impl(context):
    		context.browser.get(configuration.get_setting("tests", "url"))

## Known Problems ##

### First Run ###

On the first run the test may fail due to browser configuration. For example you may need to grant Python access to the internet.

Internet Explorer requires all Internet Zones to use the same Protected Mode (all on or off). Use ```Tools (cog image) > Internet Options > Security > Enable Protected Mode``` to configure this.

Additionally Internet Explorer requires the zoom level to be set to 100%. Once the browser has been configured all subsequent runs should be successful.

### Activate Virtual Environment ###

If when running ```behave``` from the command prompt you get the following message:

	'behave' is not recognized as an internal or external command,
	operable program or batch file.

You need to activate the Virtual Environment. From a command prompt:

	C:\git\UglyToad.Python.UITesting>env\Scripts\activate

When the environment has been activated you will see the (env) label at the prompt:

	(env) C:\git\UglyToad.Python.UITesting>

## Use with CI ##

The intention is for this project to be used for continuous integration. 
I have included an example Jenkins configuration ~\tools\config.xml


[link0]:http://pythonhosted.org/behave/index.html
[link1]:https://www.python.org/downloads/