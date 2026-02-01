# TextCommandPalette.incomingFromHTML Event

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

This event is fired when the JavaScript associated with the HTML calls the adsk.fusionSendData function. This allows the HTML to communicate with the add-in by passing information to the add-in.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "textCommandPalette_var" is a variable referencing a TextCommandPalette object. # "MyIncomingFromHTMLHandler" is the name of the class that handles the event. onIncomingFromHTML = MyIncomingFromHTMLHandler() textCommandPalette_var.incomingFromHTML.add(onIncomingFromHTML) handlers.append(onIncomingFromHTML) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the incomingFromHTML event. class MyIncomingFromHTMLHandler(adsk.core.HTMLEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.HTMLEventArgs):         # Code to react to the event.         app.log('In MyIncomingFromHTMLHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/TextCommandPalette.h> #include <Core/UserInterface/HTMLEvent.h> #include <Core/UserInterface/HTMLEventHandler.h> #include <Core/UserInterface/HTMLEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the incomingFromHTML event. ``` ````* class MyIncomingFromHTMLEventHandler : public adsk::core::HTMLEventHandler { public:  void notify(const Ptr<HTMLEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyIncomingFromHTMLEventHandler event handler.");  } } \_incomingFromHTML;  *--------- Connect the handler to the event. ---------* ```` ``` // "textCommandPalette_var" is a variable referencing a TextCommandPalette object. // Connect the handler function to the event. Ptr<HTMLEvent> incomingFromHTMLEvent = textCommandPalette_var->incomingFromHTML(); if (!incomingFromHTMLEvent)     return;  bool isOk = incomingFromHTMLEvent->add(&_incomingFromHTML); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [HTMLEvent](HTMLEvent.htm).

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |