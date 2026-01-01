# Command.incomingFromHTML Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

This event is fired when the JavaScript associated with the HTML displayed in a BrowserCommandInput calls the adsk.fusionSendData function and when the JavaScript responds to the sendInfoToHTML call. The HTMLEventArgs provided by the event indicates which BrowserCommandInput triggered the event.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyIncomingFromHTMLHandler" is the name of the class that handles the event. onIncomingFromHTML = MyIncomingFromHTMLHandler() command_var.incomingFromHTML.add(onIncomingFromHTML) handlers.append(onIncomingFromHTML) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the incomingFromHTML event. class MyIncomingFromHTMLHandler(adsk.core.HTMLEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.HTMLEventArgs):         # Code to react to the event.         app.log('In MyIncomingFromHTMLHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/HTMLEvent.h> #include <Core/UserInterface/HTMLEventHandler.h> #include <Core/UserInterface/HTMLEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the incomingFromHTML event. ``` ````* class MyIncomingFromHTMLEventHandler : public adsk::core::HTMLEventHandler { public:  void notify(const Ptr<HTMLEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyIncomingFromHTMLEventHandler event handler.");  } } \_incomingFromHTML;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<HTMLEvent> incomingFromHTMLEvent = command_var->incomingFromHTML(); if (!incomingFromHTMLEvent)     return;  bool isOk = incomingFromHTMLEvent->add(&_incomingFromHTML); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [HTMLEvent](HTMLEvent.htm).

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |