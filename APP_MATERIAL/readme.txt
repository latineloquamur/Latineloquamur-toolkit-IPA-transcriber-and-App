APP
The Phonetic Dictionary mobile application project is built using Flutter [https://flutter.dev/].

Flutter is an app SDK (Software Development Kit) for building high-performance apps for iOS & Android from a single codebase, using Dart programming language. In the future, it will become the native framework of Google’s Fuchsia OS, so a project developed in Flutter will work on three platforms: iOS, Android, and Fuchsia [https://en.wikipedia.org/wiki/Google_Fuchsia].

The architecture of the app follows a well-known BLoC pattern. BLoC stands for Business Logic Components. The gist of BLoC is that everything in the app should be represented as a stream of events: widgets submit events; other widgets will respond.

The application works offline, all words are persisted locally on the device making use of SQLite database. 
