# AngleValueCommandInput.minimumValue Property

Parent Object: [AngleValueCommandInput](AngleValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/AngleValueCommandInput.h>

## Description

Gets and sets minimum value, if any, that the value can be. The value is in radians. When getting this property you should first check the hasMinimumValue property to see if this property applies. Also, the isMinimumValueInclusive indicates if the minimum includes this value or will be up to this value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = angleValueCommandInput_var.minimumValue  # Set the value of the property. angleValueCommandInput_var.minimumValue = propertyValue ``` ```` |

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. ```` ``` #include <Core/UserInterface/AngleValueCommandInput.h>  // Get the value of the property. double propertyValue = angleValueCommandInput_var->minimumValue();  // Set the value of the property, where value_var is a double. bool returnValue = angleValueCommandInput_var->minimumValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |