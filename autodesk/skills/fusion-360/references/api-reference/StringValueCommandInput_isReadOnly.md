# StringValueCommandInput.isReadOnly Property

Parent Object: [StringValueCommandInput](StringValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/StringValueCommandInput.h>

## Description

Gets and sets if the string value is read-only or not. If it is read-only the user cannot edit the text. This property is initialized to False for a newly created StringValueCommandInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object. |

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object. ```` ``` #include <Core/UserInterface/StringValueCommandInput.h>  // Get the value of the property. boolean propertyValue = stringValueCommandInput_var->isReadOnly();  // Set the value of the property, where value_var is a boolean. bool returnValue = stringValueCommandInput_var->isReadOnly(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |