# InterferenceResult.isCreateBody Property

Parent Object: [InterferenceResult](InterferenceResult.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceResult.h>

## Description

Gets and sets if this interference volume should be created as a model body. Setting this to true doesn't create the body just indicates that a body is desired. Calling the createBodies method on the interferenceResults object will result in the creation of the model body if this property is true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"interferenceResult\_var" is a variable referencing an InterferenceResult object. |

"interferenceResult\_var" is a variable referencing an InterferenceResult object. ```` ``` #include <Fusion/Fusion/InterferenceResult.h>  // Get the value of the property. boolean propertyValue = interferenceResult_var->isCreateBody();  // Set the value of the property, where value_var is a boolean. bool returnValue = interferenceResult_var->isCreateBody(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |