# NavigationEventArgs.navigationURL Property

Parent Object: [NavigationEventArgs](NavigationEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEventArgs.h>

## Description

The URL that is being navigated to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. |

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. ```` ``` #include <Core/UserInterface/NavigationEventArgs.h>  // Get the value of the property. string propertyValue = navigationEventArgs_var->navigationURL();  // Set the value of the property, where value_var is a string. bool returnValue = navigationEventArgs_var->navigationURL(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |