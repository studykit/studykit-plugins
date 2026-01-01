# NavigationEvent.isValid Property

Parent Object: [NavigationEvent](NavigationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEvent\_var" is a variable referencing a NavigationEvent object. |

"navigationEvent\_var" is a variable referencing a NavigationEvent object. ```` ``` #include <Core/UserInterface/NavigationEvent.h>  // Get the value of the property. boolean propertyValue = navigationEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |