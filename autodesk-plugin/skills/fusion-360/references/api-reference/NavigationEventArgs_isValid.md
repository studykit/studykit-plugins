# NavigationEventArgs.isValid Property

Parent Object: [NavigationEventArgs](NavigationEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. |

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. ```` ``` #include <Core/UserInterface/NavigationEventArgs.h>  // Get the value of the property. boolean propertyValue = navigationEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |