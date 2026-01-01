# AngleValueCommandInput.isMaximumValueInclusive Property

Parent Object: [AngleValueCommandInput](AngleValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/AngleValueCommandInput.h>

## Description

Gets and sets if the value of the input includes the maximum value or is up to the maximum value. For example, if the maximum value is the value of pi (180 degrees) and this property is True, the maximum value can be pi. If this is False, the minimum value must be less than pi. When the maximum value is first defined using the maximumValue property, this property is set to True. The value returned by this property is only meaningful when the hasMaximumValue property returns True.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. |

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. ```` ``` #include <Core/UserInterface/AngleValueCommandInput.h>  // Get the value of the property. boolean propertyValue = angleValueCommandInput_var->isMaximumValueInclusive();  // Set the value of the property, where value_var is a boolean. bool returnValue = angleValueCommandInput_var->isMaximumValueInclusive(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |