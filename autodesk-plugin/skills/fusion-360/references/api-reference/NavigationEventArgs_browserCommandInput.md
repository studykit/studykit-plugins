# NavigationEventArgs.browserCommandInput Property

Parent Object: [NavigationEventArgs](NavigationEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEventArgs.h>

## Description

When the event is fired from a BrowserCommandInput object, this property returns the specific BrowserCommandInput that caused the event to fire. In all other cases this property returns null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. |

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. ```` ``` #include <Core/UserInterface/NavigationEventArgs.h>  // Get the value of the property. Ptr<BrowserCommandInput> propertyValue = navigationEventArgs_var->browserCommandInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [BrowserCommandInput](BrowserCommandInput.htm).

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |