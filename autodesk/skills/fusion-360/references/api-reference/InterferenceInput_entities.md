# InterferenceInput.entities Property

Parent Object: [InterferenceInput](InterferenceInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceInput.h>

## Description

Gets and set an ObjectCollection containing BRepBody and/or Occurrence entities that will be used when checking for interference. All entities must be in the context of the root component of the top-level design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"interferenceInput\_var" is a variable referencing an InterferenceInput object. |

"interferenceInput\_var" is a variable referencing an InterferenceInput object. ```` ``` #include <Fusion/Fusion/InterferenceInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = interferenceInput_var->entities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = interferenceInput_var->entities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |