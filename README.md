# Nights Away Forms Generator

Are you a Scout Leader who's tired of all the paperwork required 
for a nights away event? Then this is the app for you! 

nightsawayforms takes all the boring, repetitive tasks and automates 
them for you. It asks a set of simple questions and uses your answers 
to fill in the details. 

Use nightsawayforms as part of your camp planning to take the pain away 
and let you focus on the fun. 

This is not an official Scout Association product. We're just keen 
Scout Leaders who wanted to automate the paperwork process when 
organising nights away events. 

Detailed documentation is in the "docs" directory.

## Quick start

1. Run nightsawayforms to begin. 

2. It will ask you a series of questions. It will offer to store group 
   details in a config file in the config directory to save time in 
   future uses. 

3. The first time it runs, nightsawayforms will write default settings 
   to the config directory. These are: 
   - equipment.json for group equipment
   - kitList.json for personal kit lists
   - risks.json for risk assessments
 
   A copy of the Nights Away Notification (NAN) form will be copied 
   here from the Scout Association website for local working. A resized 
   logo will also be stored here for use by headers. 

4. Advanced users may wish to edit these settings files. You can do this 
   directly with any programme capable of editing json data. See the 
   documentation on details of special categories and dynamic content. 

5. Enjoy your camping trips! 

## Included forms

nightAwayForms generates most of the suite of paperwork required to complete 
a Scout Association nights away permit and for running any nights away activity. 
Based on the user's input, this app will generate a:
   - programme
   - menu
   - kit list to issue to young people
   - risk assessment
   - group equipment list (request form)
   - health and emergency contact form 

A blank Nights Away Notification (NAN) form is also deployed to the camp 
directory, so it's easier for you to fill in and send off. 

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct. 

This app is written in python 3.6. 

## Authors

* **PoignantWizard** - *Initial work* 

## License

This project is licensed under the 3-Clause BSD License - see the [LICENSE.md](LICENSE.md) file 
for details. 