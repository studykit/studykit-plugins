# HTMLEventArgs.data Property

Parent Object: [HTMLEventArgs](HTMLEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/HTMLEventArgs.h>

## Description

The data string sent from the JavaScript associated with HTML displayed in the palette. The string can represent any type of data in any format but JSON is commonly used to pass more complex data.

## Syntax

* [Python](#Python)
* [C++](#C++)

"hTMLEventArgs\_var" is a variable referencing a HTMLEventArgs object. |

"hTMLEventArgs\_var" is a variable referencing a HTMLEventArgs object. ```` ``` #include <Core/UserInterface/HTMLEventArgs.h>  // Get the value of the property. string propertyValue = hTMLEventArgs_var->data(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |