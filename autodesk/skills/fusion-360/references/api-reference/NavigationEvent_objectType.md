# NavigationEvent.objectType Property

Parent Object: [NavigationEvent](NavigationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEvent\_var" is a variable referencing a NavigationEvent object.  ```` ``` # Get the value of the property. propertyValue = navigationEvent_var.objectType ``` ```` |

"navigationEvent\_var" is a variable referencing a NavigationEvent object. ```` ``` #include <Core/UserInterface/NavigationEvent.h>  // Get the value of the property. string propertyValue = navigationEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |