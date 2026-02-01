# AsBuiltJointInput.occurrenceOne Property

Parent Object: [AsBuiltJointInput](AsBuiltJointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointInput.h>

## Description

Specifies the first of two occurrences the joint is between.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJointInput\_var" is a variable referencing an AsBuiltJointInput object. |

"asBuiltJointInput\_var" is a variable referencing an AsBuiltJointInput object. ```` ``` #include <Fusion/Components/AsBuiltJointInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = asBuiltJointInput_var->occurrenceOne();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = asBuiltJointInput_var->occurrenceOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |