# RevolveFeatureInput.creationOccurrence Property

Parent Object: [RevolveFeatureInput](RevolveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatureInput.h>

## Description

In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Revolve is created based on geometry (e.g. a profile and/or face(s)) in another component AND (the Revolve) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object. |

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object. ```` ``` #include <Fusion/Features/RevolveFeatureInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = revolveFeatureInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = revolveFeatureInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |