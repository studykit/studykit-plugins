# ThickenFeatureInput.creationOccurrence Property

Parent Object: [ThickenFeatureInput](ThickenFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatureInput.h>

## Description

In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Thicken feature is created based on geometry (e.g. a profile and/or face(s)) in another component AND (the Thicken feature) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object. |

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object. ```` ``` #include <Fusion/Features/ThickenFeatureInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = thickenFeatureInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = thickenFeatureInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |