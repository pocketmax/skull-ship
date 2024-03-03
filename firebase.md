# Firebase notes BaaS

Everything is sandboxed around projects instead of service like AWS. i.e. all lambdas exist under a project

Alias projects: used to deploy changes to different projects i.e. staging & production
To add an alias project
firebase use —add
firebase use (alias projects name)



Questions
1. Docker support?
2. Flutter support?
3. Server side support?
4. Diff between projects and google cloud platform projects?


How to toggle emulation?
Do the npm packages get deployed or does it remote NPM install?

Firestore
*

Functions: Configure a Cloud Functions directory and its files
Storage: Configure a security rules file for Cloud Storage
Emulators: Set up local emulators for Firebase products
Remote Config: Configure a template file for Remote Config
Realtime Database: Configure a security rules file for Realtime Database and (optionally) provision default instance


GitHub Action deploys for hosting?
https://github.com/features/actions

Vuefire
Firebase: old version

Hosting
What does /__/* point to in hosting?
How to add refs to node_modules folder? You build your project normally and just point the public folder in firebase.json to your dist folder

Tasks
* DONE Host Hello world page
* DONE Add vue3 support via CDN
* DONE Add vue3 support to page via local node_modules
    * Just copy over vue files, build with parcel and config the public dir to /dist
* Add firestore support to page
* Add

Server templating

Firestore
* New Collections based db i.e. cloud mongodb

Diff beween vuefire, firestore, Firebase RTDB and

* Watch general intro videos on what it can do (take notes)
    * Categorized list of features
    * Questions
        * Does it have user authentication?
        * How it handles binary data like images?
        * Usage restrictions to prevent spam bills
        * How it links with other google cloud services
* Write up list of fb tasks for the app


Firebase emulator
* local simulated firebase cloud

Firebase ML
* https://firebase.google.com/docs/ml
* Uses TensorFlow Lite models
* Models are downloaded by devices as needed
* Can evaluate/update models without republishing the app
* Can deploy models from colab notebook
* Make API calls to remote hosted models


Firebase auth
* Drop in UI
* Oauth
* questions
    1. Can it be used stand alone?
    2. Can it handle account grouping i.e. recognizing the same person from their gmail or twitter accounts?


Cloud storage
* For blob data
* Can pause/resume transfers as the app loses/regains mobile connectivity
* Can allow access based on file meta data like size, content type or name
* Questions
    * How diff is this from S3?

Realtime database
* Store and sync local JSON data between devices in real time
* Uses cloud functions to exec backend code that responds to events
* Optimized for offline use

Firebase crashlytics
* Real time crash reporting
* Questions
    * Realtime remote debugger?

Performance monitoring
* Realtime performance monitoring

Firebase test lab
* Browserstack for apps
* Can test on physical and virtual devices

Firebase app distribution
* Distribute app to trusted test users

Firebase in-app messaging
* Send targeted messages to users based on previous, current, future activity i.e. ads

Firebase A/B testing
* Test/track business metrics based changes

Firebase cloud messaging
* Chat
* Looks deprecated

Dynamic Links
* Deep link to parts of your app
* Survives the installation process (what ever that means)

Google analytics
* analytics

