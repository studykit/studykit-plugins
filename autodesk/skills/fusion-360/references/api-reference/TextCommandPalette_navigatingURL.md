# TextCommandPalette.navigatingURL Event

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

This event is fired when a navigation event occurs on the page. This allows the add-in to determine how this navigation should be handled by the browser.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "textCommandPalette_var" is a variable referencing a TextCommandPalette object. # "MyNavigatingURLHandler" is the name of the class that handles the event. onNavigatingURL = MyNavigatingURLHandler() textCommandPalette_var.navigatingURL.add(onNavigatingURL) handlers.append(onNavigatingURL) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the navigatingURL event. class MyNavigatingURLHandler(adsk.core.NavigationEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.NavigationEventArgs):         # Code to react to the event.         app.log('In MyNavigatingURLHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/TextCommandPalette.h> #include <Core/UserInterface/NavigationEvent.h> #include <Core/UserInterface/NavigationEventHandler.h> #include <Core/UserInterface/NavigationEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the navigatingURL event. ``` ````* class MyNavigatingURLEventHandler : public adsk::core::NavigationEventHandler { public:  void notify(const Ptr<NavigationEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyNavigatingURLEventHandler event handler.");  } } \_navigatingURL;  *--------- Connect the handler to the event. ---------* ```` ``` // "textCommandPalette_var" is a variable referencing a TextCommandPalette object. // Connect the handler function to the event. Ptr<NavigationEvent> navigatingURLEvent = textCommandPalette_var->navigatingURL(); if (!navigatingURLEvent)     return;  bool isOk = navigatingURLEvent->add(&_navigatingURL); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [NavigationEvent](NavigationEvent.htm).

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |