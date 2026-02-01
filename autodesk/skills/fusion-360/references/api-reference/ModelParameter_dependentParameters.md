# ModelParameter.dependentParameters Property

Parent Object: [ModelParameter](ModelParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameter.h>

## Description

Returns a list of parameters that are dependent on this parameter as a result of this parameter being referenced in their equation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameter\_var" is a variable referencing a ModelParameter object. |

"modelParameter\_var" is a variable referencing a ModelParameter object. ```` ``` #include <Fusion/Fusion/ModelParameter.h>  // Get the value of the property. Ptr<ParameterList> propertyValue = modelParameter_var->dependentParameters(); ``` ```` |

## Property Value

This is a read only property whose value is a [ParameterList](ParameterList.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |