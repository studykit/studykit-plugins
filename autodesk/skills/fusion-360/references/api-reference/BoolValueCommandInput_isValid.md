# BoolValueCommandInput.isValid Property

Parent Object: [BoolValueCommandInput](BoolValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BoolValueCommandInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. |

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. ```` ``` #include <Core/UserInterface/BoolValueCommandInput.h>  // Get the value of the property. boolean propertyValue = boolValueCommandInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |