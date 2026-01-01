# TabCommandInput.isValid Property

Parent Object: [TabCommandInput](TabCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TabCommandInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. |

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. ```` ``` #include <Core/UserInterface/TabCommandInput.h>  // Get the value of the property. boolean propertyValue = tabCommandInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |