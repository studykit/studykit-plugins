# HTMLEventArgs.returnData Property

Parent Object: [HTMLEventArgs](HTMLEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/HTMLEventArgs.h>

## Description

Set this property to return data back to the JavaScript that's associated with the HTML.

## Syntax

* [Python](#Python)
* [C++](#C++)

"hTMLEventArgs\_var" is a variable referencing a HTMLEventArgs object. |

"hTMLEventArgs\_var" is a variable referencing a HTMLEventArgs object. ```` ``` #include <Core/UserInterface/HTMLEventArgs.h>  // Get the value of the property. string propertyValue = hTMLEventArgs_var->returnData();  // Set the value of the property, where value_var is a string. bool returnValue = hTMLEventArgs_var->returnData(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |