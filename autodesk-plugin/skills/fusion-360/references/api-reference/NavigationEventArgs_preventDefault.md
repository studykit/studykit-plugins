# NavigationEventArgs.preventDefault Property

Parent Object: [NavigationEventArgs](NavigationEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEventArgs.h>

## Description

If True, the default handling of this navigation event will not continue. If False, the default value, the default handling of this navigation event will continue.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. |

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. ```` ``` #include <Core/UserInterface/NavigationEventArgs.h>  // Get the value of the property. boolean propertyValue = navigationEventArgs_var->preventDefault();  // Set the value of the property, where value_var is a boolean. bool returnValue = navigationEventArgs_var->preventDefault(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |