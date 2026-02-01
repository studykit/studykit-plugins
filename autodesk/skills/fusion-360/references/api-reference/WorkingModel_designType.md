# WorkingModel.designType Property

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Gets and sets the current design type (DirectDesignType or ParametricDesignType) Changing an existing design from ParametricDesignType to DirectDesignType will result in the timeline and all design history being removed and further operations will not be captured in the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a WorkingModel object. |

"workingModel\_var" is a variable referencing a WorkingModel object. ```` ``` #include <Fusion/Fusion/WorkingModel.h>  // Get the value of the property. DesignTypes propertyValue = workingModel_var->designType();  // Set the value of the property, where value_var is a DesignTypes. bool returnValue = workingModel_var->designType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DesignTypes](DesignTypes.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |